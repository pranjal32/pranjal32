#!/usr/bin/env python3
"""Fetches and caches external profile SVG assets into the workflow dist directory."""

from __future__ import annotations

import argparse
import json
import os
import pathlib
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Cache external profile assets")
    parser.add_argument("--config", required=True, help="Path to JSON config file")
    parser.add_argument("--output-dir", required=True, help="Directory to write assets into")
    parser.add_argument("--workers", type=int, default=4, help="Max concurrent downloads")
    parser.add_argument("--retries", type=int, default=3, help="Retries per asset")
    parser.add_argument("--timeout", type=int, default=20, help="HTTP timeout in seconds")
    return parser.parse_args()


def load_assets(config_path: pathlib.Path) -> list[dict[str, str]]:
    data = json.loads(config_path.read_text(encoding="utf-8"))
    assets = data.get("assets")
    if not isinstance(assets, list) or not assets:
        raise ValueError("Config must contain a non-empty 'assets' list.")
    return assets


def fetch_asset(
    name: str,
    url: str,
    output_dir: pathlib.Path,
    retries: int,
    timeout: int,
) -> tuple[str, bool, str]:
    target = output_dir / name
    target.parent.mkdir(parents=True, exist_ok=True)

    headers = {"User-Agent": "pranjal32-profile-cache/1.0"}
    for attempt in range(1, retries + 1):
        try:
            request = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(request, timeout=timeout) as response:
                payload = response.read()
            target.write_bytes(payload)
            return (name, True, f"cached ({len(payload)} bytes)")
        except (urllib.error.URLError, TimeoutError) as exc:
            if attempt >= retries:
                return (name, False, str(exc))
            time.sleep(min(2 ** (attempt - 1), 5))
    return (name, False, "unexpected error")


def main() -> int:
    args = parse_args()
    config_path = pathlib.Path(args.config)
    output_dir = pathlib.Path(args.output_dir)
    assets = load_assets(config_path)

    failures = 0
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futures = []
        for asset in assets:
            name = str(asset["name"]).strip()
            url = str(asset["url"]).strip()
            if not name or not url:
                raise ValueError("Each asset must include non-empty 'name' and 'url'.")
            if os.path.isabs(name) or ".." in pathlib.PurePosixPath(name).parts:
                raise ValueError(f"Unsafe asset name: {name}")
            futures.append(
                pool.submit(
                    fetch_asset,
                    name=name,
                    url=url,
                    output_dir=output_dir,
                    retries=max(1, args.retries),
                    timeout=max(1, args.timeout),
                )
            )

        for future in as_completed(futures):
            name, ok, detail = future.result()
            print(f"[{'OK' if ok else 'FAIL'}] {name}: {detail}")
            if not ok:
                failures += 1

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())

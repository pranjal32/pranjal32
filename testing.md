---
layout: default
title: UAD-ng Setup and Debloat Guide (Detailed)
nav_title: UAD-ng Guide (Detailed)
---

# How to Uninstall Pre-installed Apps Using UAD-ng

If you want to remove pre-installed apps from your Android phone without using complex command-line tools, **Universal Android Debloater Next Generation (UAD-ng)** is the safest and easiest solution. This tool provides a graphical user interface (GUI) to manage apps on your device.

---

## Prerequisites

Before starting, ensure you have the following:

1.  **A PC** (Windows, macOS, or Linux).
2.  **A USB Cable** to connect your phone.
3.  **An Android Phone** with Developer Options enabled.

---

## Step 1: Prepare Your Phone

You must enable USB Debugging to allow your PC to communicate with your phone.

1.  Open **Settings** on your phone.
2.  Go to **About Phone**.
3.  Tap **Build Number** 7 times rapidly until it says, "You are now a developer!"
4.  Return to the main **Settings** menu.
5.  Search for and open **Developer Options**.
6.  Locate and toggle on **USB Debugging**.
7.  Connect your phone to your PC. If a prompt appears on your phone screen asking to "Allow USB Debugging," check **"Always allow from this computer"** and tap **OK**.

---

## Step 2: Download UAD-ng

1.  Visit the official [UAD-ng GitHub Releases page](https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation/releases).
2.  Download the executable file appropriate for your operating system (e.g., `uad_gui-windows.exe` for Windows).

---

## Step 3: Remove Unwanted Apps

1.  **Launch the tool:** Run the file you downloaded.
2.  **Detection:** UAD-ng will automatically detect your connected device and load a list of all installed packages.
3.  **Search:** Use the search bar at the top to look for the app you want to remove (e.g., "YouTube").
4.  **Action:** Select the app, and click the **Uninstall** button.
    *   *Tip:* If you are unsure about an app, choose **Disable** instead. This hides the app without fully removing it, making it safer to reverse later.

---

## Visual Reference & Support

For a visual walkthrough of the interface and additional troubleshooting, please refer to the official resources:

*   [UAD-ng Getting Started Wiki](https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation/wiki/Getting-started)
*   [UAD-ng Video Walkthrough](https://www.youtube.com/watch?v=2ZUWlv43QFc)

---

## Important Warnings

*   **Safety First:** Only remove apps labeled as **"Recommended"** if you are a beginner. Removing "Essential" system apps can cause your phone to become unstable or enter a bootloop.
*   **Backups:** Always back up your important data before using debloating tools.
*   **Factory Reset:** If you perform a factory reset, the apps will reappear. You will need to run UAD-ng again to remove them.

---
layout: default
title: Home
---

# Hi, I'm Pranjal

Tech enthusiast from Chandigarh, India. I build personal projects, explore low-level systems, and document practical workflows.

<div class="terminal-chip">STATUS // ALWAYS BUILDING SOMETHING</div>

<img class="hero-typing" src="https://raw.githubusercontent.com/pranjal32/pranjal32/output/profile-assets/typing.svg" alt="Typing headline animation">

## Focus right now

<div class="signal-grid">
  <div class="signal-card">
    <h3>Learning</h3>
    <p>New technologies and modern tooling.</p>
  </div>
  <div class="signal-card">
    <h3>Building</h3>
    <p>Personal projects across software and hardware.</p>
  </div>
  <div class="signal-card">
    <h3>Exploring</h3>
    <p>OS internals, virtualization, networking, and low-level systems.</p>
  </div>
</div>

## Latest articles

{% assign article_pages = site.pages | where: "layout", "default" | sort: "title" %}
<div class="article-grid">
{% for article in article_pages %}
  {% if article.url != '/' and article.title %}
  <a class="article-card" href="{{ article.url | relative_url }}">
    <h3>{{ article.title }}</h3>
    <p>{{ article.excerpt | strip_html | strip_newlines | truncate: 110 }}</p>
  </a>
  {% endif %}
{% endfor %}
</div>

## Profile metrics

<div class="metrics-grid">
  <img src="https://raw.githubusercontent.com/pranjal32/pranjal32/output/profile-assets/stats.svg" alt="GitHub stats">
  <img src="https://raw.githubusercontent.com/pranjal32/pranjal32/output/profile-assets/top-langs.svg" alt="Top languages">
  <img src="https://raw.githubusercontent.com/pranjal32/pranjal32/output/profile-assets/streak.svg" alt="Contribution streak">
  <img src="https://raw.githubusercontent.com/pranjal32/pranjal32/output/profile-assets/activity-graph.svg" alt="Contribution graph">
</div>

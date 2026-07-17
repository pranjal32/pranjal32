---
layout: default
title: Home
---

# Welcome

This site collects technical guides and write-ups.

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

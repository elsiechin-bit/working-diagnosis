---
title: Field Guide
layout: topic
description: Sixteen clinical areas, slowly growing. What to recognise, what to do, and what to tell patients.
---

A working index of the clinical pillars. Each section is a small, slowly-growing collection of conditions, written from a NZ general-practice perspective. Some are well-tended, others are stubs in progress. Tap any pillar to start reading.

<nav class="pillar-list" aria-label="Clinical pillars">
  <ul>
    {% for item in site.nav %}
      {% if not item.divider and item.row and item.row <= 5 %}
        <li><a href="{{ item.url }}">{{ item.label }}</a></li>
      {% endif %}
    {% endfor %}
  </ul>
</nav>

---
title: The Library
layout: topic.njk
description: A clinician's library of NZ general practice. Conditions by specialty, with patient handouts to send home.
specialty: Library
---

The full catalog of clinical pillars and topics. Pick a specialty to drill in.

<ul class="topic-list">
  {% for item in site.nav %}
    {% if not item.divider and item.row and item.row >= 1 and item.row <= 5 %}
      <li><a href="{{ item.url }}">{{ item.label }}</a></li>
    {% endif %}
  {% endfor %}
</ul>

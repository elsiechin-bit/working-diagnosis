---
title: Experiments
layout: topic.njk
pageType: experiments
description: Work-in-progress tools and ideas. Passphrase required.
eleventyExcludeFromCollections: true
---

<p class="topic-dek">Work in progress. Things that are not yet ready for the wider site live here.</p>

<p>This page exists so the link in the GP Tools sidebar has somewhere to land. Add experiments here as new <code>experiments/[slug]/index.md</code> files - they will be gated by the same passphrase automatically, since the gate script triggers on any URL starting with <code>/experiments/</code>.</p>

<h2>Notes for future-you</h2>

<ul>
  <li>Passphrase is set in <code>assets/workshop-gate.js</code> (still named <em>workshop-gate</em> for git-history continuity, but it now gates <code>/experiments/</code>)</li>
  <li>To change the passphrase, follow the <code>HOW TO CHANGE THE PASSPHRASE</code> instructions at the top of that file</li>
  <li>The gate is client-side only - it hides content from a casual visitor, but anyone who views source can fetch the underlying HTML. Treat as soft-gating, not security</li>
</ul>

<script src="/assets/workshop-gate.js"></script>

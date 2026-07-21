---
layout: post
date: 2026-03-20
title: "I Built an Obsidian Plugin to Surface My Most-Edited Notes"
excerpt: "An Obsidian plugin that automatically counts meaningful edits and helps you identify the notes you revisit most. Here's the thought process behind building it."
comments: true
lang: en
genre: Practical
thumbnail: /assets/images/obsidian_logo.png
stage: 3
read_minutes: 3
---

An Obsidian plugin that automatically counts meaningful edits and helps you keep track of the notes you revisit most. It's been working well enough on my end, so I'm releasing it as a beta.

### Starting Point: Finding the "Heavy" Notes

After using Obsidian for over 3 years, my notes had grown considerably.
When I opened the graph view, every note appeared at roughly the same size. Link count does affect node size, but that reflects "how connected" a note is — not "how actively I'm thinking about it."
It became a chance to revisit what a valuable note really means to me. The answer: notes I keep opening, adding to, and rewriting. In other words, **notes with a high edit count**.

This was a good starting point.

### Starting with Existing Plugins

I began by looking for existing solutions.

[Extended Graph](https://github.com/ElsaTam/obsidian-extended-graph) can scale node sizes based on frontmatter values. On the display side, this was exactly what I wanted — but it doesn't automatically measure edit count. And manually updating frontmatter every time didn't seem practical.

[Obsidian Git](https://github.com/Vinzent03/obsidian-git) manages your vault with Git. You could track per-file change frequency via `git log`, but enabling auto-commit pollutes the log. Backups are nice, but how would you weight existing notes?

[Activity Heatmap](https://github.com/zakhij/obsidian-activity-heatmap) and [Sidebar Heatmap](https://forum.obsidian.md/t/new-plugin-sidebar-heatmap/98528) visualize "volume of change" and "daily activity" respectively — neither was a direct fit for weighting notes by cumulative edit count.

### Approach: Detecting Meaningful Edits via Character Diff

Simply incrementing a counter on every save wouldn't make sense. Fixing a typo and rewriting an entire paragraph are fundamentally different.

So I went with **character count diff with a threshold**. The plugin snapshots the character count when you open a note, then evaluates the diff when you switch files or after a period of inactivity (default: 3 minutes).
If the difference is 50 characters or more, it increments `edit_count` in the frontmatter.

Since this is highly personal, the threshold is configurable.

```yaml
---
edit_count: 5
---
```

The key here is that it's entirely self-contained within Obsidian. No Git, no external tools — the only thing held in memory is the initial character count of the open file, so it's lightweight.
And since it just modifies frontmatter in the file, it aligns with the [file over app](https://stephango.com/file-over-app) principle.

### How I Use It (For Now)

On Obsidian 1.9.10+, you can use the core Bases feature to create a table sorted by `edit_count` — no third-party dependency like Dataview needed. "I've been working on this note a lot" or "my thinking is concentrated in this area" becomes visible at a glance, so I keep it pinned as a pane on screen.

### Still in Beta

The plugin is currently available as a beta release, installable via [BRAT](https://github.com/TfTHacker/obsidian42-brat).
I've been using it daily in my own vault without any major issues, but it hasn't been tested enough in other environments to warrant an official release. 

Feedback is welcome on [GitHub](https://github.com/DaisukeMiyazaki/obsidian-edit-count).

### Looking Back

I can now measure a note's significance not just by its link count, but by how many times I've put my hands on it. 
Neither metric is "right" — having a different viewpoints simply reveals things you wouldn't otherwise notice. 

The trail of thinking lives not in how much you wrote, but in how many times you rewrote. This plugin turned that intuition into something backed by numbers.

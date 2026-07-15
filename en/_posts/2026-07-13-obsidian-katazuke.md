---
layout: post
date: 2026-07-13
title: "I Built an Obsidian Plugin to Tidy Up Notes That Once Mattered but Gathered Dust"
excerpt: "Notes I once thought were important, now quietly gathering dust. Before adding new connections, let go of the old ones. The story of an Obsidian plugin I built to help with that kind of tidying."
comments: true
lang: en
genre: Practical
thumbnail: /assets/images/obsidian_logo.png
---

I built an Obsidian plugin that finds and helps you tidy up the notes you once thought were important but that have quietly gathered dust. It's out now as an official community plugin.

### Hard to spot in the graph view

As a vault grows, so do its notes and backlinks.
When links pile up and cross-connect, the graph view turns a note into a catch-all that seems connected to everything. There's plenty of information, but that abundance is exactly what keeps you from reaching the note you actually want.

A node with many lines stands out. But you can't tell from its look whether it's an index you meant to build or an unconscious pile-up.

And connections you organized a while ago can stop being appropriate as time passes. Whether they still hold today is not something the graph view shows you.

### Let go before you add

When you grow a note, you naturally think only in terms of adding — drawing relations, adding links, deepening your thinking.

But there's a step worth being aware of before that.
Before adding connections, first reduce the ones you don't need.
It's the subtractive mindset of discarding a note that has become too tangled.

What this does resembles tidying a room.
Before you place something new, first let go of the old. Wanting to do the same with notes is what set this off — and it's where the plugin's name comes from. (*Katazuke* means "tidying up" in Japanese.)

Earlier I built [a plugin that enlarges the notes I edit most](/en/2026/03/20/obsidian-edit-count/). That one surfaces the notes I keep my hands on — like the favorite belongings in a room. Because you reach for them often, they never gather dust.

This time it's about the things I thought were important but that ended up gathering dust anyway. Maybe it's a similar feeling.

### Surfacing old, over-connected notes in one command

What matters in tidying is a question like: have I used this in the last month? Using that as a guide, I gave more weight to old notes and over-connected notes.

```
score = number of a note's links × (1 + days untouched / 1 month)
```

Intentional notes are excluded. Some notes are important and allowed to gather dust — and as long as it's intentional, that's fine.

Links to attachments like images and videos aren't counted. What I want to see is the connections between notes.

### A quick tidy, or a proper one

Tidying is a special event, almost a festival — something I learned from Marie Kondo's book. So I prepared two modes: one as a small ritual, and one for when you settle in, closer to that festival in how it's used. And so you can start right away, each is a single command straight from Obsidian's command palette.

Face one note. It surfaces just the single top note. Good for a daily habit or a spare moment.

Or face a handful. It surfaces the top few. Marie Kondo's style of tidying leans more this way.

It's not about mechanically reordering everything and gazing at the result. You face them one at a time, by your own hand, starting from the top.

### After tidying up

Being in a tidied room feels good. You're surrounded by what you love, and whatever you need, you can pull it out right away, wherever it is.

Facing your notes is, by nature, also the work of locking many ideas away across many places — which makes it all the more important to forget well when the time comes.

The reason you can keep adding things, keep adding notes, is that you believe you'll be able to pull them out later when you need them. Only when there's a system that lets you forget with peace of mind can you truly stockpile in your own room.

If everything is neatly tidied, reaching the notes you treasure will be quicker. I hope Katazuke helps you face notes that matter more to you.

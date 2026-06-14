---
layout: post
title: "The Indentation Project, Part 1: Designing a 6-Mat Room That Has to Be Four Rooms"
date: 2026-04-09
lang: en
genre: practical
excerpt: "A 6-tatami room (about 9.7㎡) has to be storage, display, workspace, and sofa all at once — and nothing off-the-shelf fits floor-to-ceiling or comes apart when the lease ends. So I modeled the whole frame in Fusion 360 and joined it with Kreg pocket holes."
thumbnail: /assets/images/indentation/IMG_1857.jpg
comments: true
---

*The Indentation Project is a series. I built this in 2024 and I'm writing it up now. This Part 1 covers the design and the wall-to-ceiling frame. The build photos live in the [ver1 gallery](https://mdaisuke.net/en/2025/01/20/The-indentation-Project-ver1/).*

## The problem: one room, four jobs

A 6-tatami room (about 9.7㎡) has to hold craft materials, display the things you make, give you a surface to work on, and still seat you on a sofa at the end of the day. Pile four jobs onto one room and every off-the-shelf option falls short.

Shelving from IKEA or Nitori eats floor area without ever reaching the ceiling, so the most valuable space in a small apartment — the top third of the wall — stays empty. Buy units piecemeal and the dimensions and finishes never line up; the room reads as a patchwork. And none of it can absorb the sofa. A sofa is a thing you *place*; a shelf is a thing you *stand up*. The moment they sit in the room as separate objects, 9.7㎡ splits into four half-rooms that fight each other.

What the room needed was a single built-in skeleton that used the full height of the wall and pulled the sofa into the same structure. And because it's a rental, the whole thing had to come back apart at move-out without marking the walls. That was the first constraint, and it shaped everything after it.

![The wall-to-ceiling frame with the sofa built into the same structure](https://mdaisuke.net/assets/images/indentation/IMG_1857.jpg)

## Modeling the whole thing in Fusion 360 before buying a single board

I modeled the entire structure in Fusion 360 before buying any lumber. Two goals: **use the full height of the wall while adding zero floor footprint**, and lock every part's dimensions before a single cut.

The frame is almost entirely 2x2. The one exception is the center beam under the sofa platform, which carries a seated person's weight, so that's 2x4. Several of the shelves are cantilevered — supported on one or two sides only — to keep the indentation cavities open and the whole thing visually light.

The deepest design rule was **no glue on any frame joint — full disassembly by design**. Every joint had to break down into pieces small enough to carry out of a rental without touching the walls. Designing for that from the first sketch is the decision that pays off later, in a way I didn't fully see at the time.

![The Fusion 360 model of the full structure](https://mdaisuke.net/assets/images/indentation/indentation%20ver1.png)

## Why Kreg pocket holes

I joined the frame with Kreg pocket-hole joinery: two angled holes drilled into each board end, screwed from a hidden face. No visible hardware, and a strong joint.

The real reason was that pocket holes **scale**. A structure like this needs hundreds of identical joints. Cutting a traditional joint hundreds of times isn't realistic — but clamping a jig and drilling two holes is the same motion at the same accuracy, however many times you repeat it. Push the design toward "smallest repeatable unit" and assembly *and* disassembly both run on that unit.

![Pocket holes drilled into the 2x2 ends — the indentations the project is named for](https://mdaisuke.net/assets/images/indentation/IMG_1747.jpg)

## Building the frame

Assembly went in three stages: the sofa base first, then the verticals, then the horizontal beams. You don't stack bottom to top — you fix the load-bearing base, stand the verticals into it, and tie them together with the horizontals. From across the room, it already looked finished at this point.

## What went wrong

Two things worth recording.

First, the design had a middle partition in the upper-left shelf section. On screen it looked tidy. Assembled, that one board cramped the space and blocked anything tall from going in. Correct on the drawing, in the way on the wall. I took it out.

Second, drilling the pocket holes scattered wood chips across the whole apartment. I'd set up to contain them. Drill a few hundred holes anyway and the sawdust travels well past wherever you thought the mess would stay. Sweeping up afterward, I thought: the steps that never make it onto the drawing are exactly the ones that make the real mess.

![The Kreg jig and drill, and the sawdust that went everywhere](https://mdaisuke.net/assets/images/indentation/IMG_1646.jpg)

## What I learned

**Model first — but expect the model to be wrong in the ways that matter.** Fusion 360 meant almost no wasted material. But there will always be a partition-shaped surprise: right on screen, in the way in the room. The model was a perfect tool for fixing the shopping list and an incomplete tool for guaranteeing how the thing feels to use.

**Designing for disassembly from the start propagates downstream.** I sized the verticals as smallest-repeatable-units for the sake of move-out. That decision comes back in Part 2: when I build the under-sofa drawer, the leftover offcuts turn out to be sized almost exactly to its interior. Modular design pays out in places the original design never intended.

Put the same trap in code terms: **a model that builds is not the same as a model that works.** The tests can be green and still be testing the wrong function. There's another design pass between "the drawing closes" and "the room runs."

![The frame assembled — the skeleton standing, before any surfaces or drawers](https://mdaisuke.net/assets/images/indentation/IMG_1986.jpg)

The frame held the sofa and the skeleton stood. But the shelves had no surfaces yet, the space under the sofa was still a hollow cavity, and there was nowhere to set a single book down. In ver2 I add the top boards and a drawer — and run straight into **a drawer that fit so perfectly it wouldn't open.** Static fit and fit-for-the-hand turned out to be two different things. That's Part 2.

---

*The full ver1 build gallery is [here](https://mdaisuke.net/en/2025/01/20/The-indentation-Project-ver1/).*

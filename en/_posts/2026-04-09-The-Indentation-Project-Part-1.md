---
layout: post
date: 2026-04-09
title: "The Indentation Project, Part 1: Designing a Wall-to-Ceiling Frame for a 6-Tatami Room"
excerpt: "When a single room has to be storage, display, workspace, and sofa all at once, no off-the-shelf furniture fits. So I opened Fusion 360 and designed my own."
comments: true
lang: en
lang-ref: indentation-part-1
genre: practical
thumbnail: /assets/images/indentation/IMG_1857.jpg
---

## The problem

Our apartment has a 6-tatami room — about 9.7 square meters. That single room needed to be four things at once: a storage space for craft materials, a display shelf for finished pieces and inspiration objects, a workspace for making things, and a living area with a sofa where we could actually relax.

No piece of furniture at IKEA or Nitori does all four. Modular shelving systems come close, but they either eat floor space a small room can't spare, or stop well short of the ceiling, wasting the vertical meters that are the only real resource in a Japanese apartment. A custom order from a furniture shop would cost more than our sofa. And none of the off-the-shelf options could integrate the sofa into the structure itself — they'd sit beside it, competing for the same floor.

So the project started with a question: could I design a single piece of furniture that wraps around the walls, reaches the ceiling, holds a sofa on top of its base, and still be disassembled when we move?

## Designing in Fusion 360

I modeled the whole structure in Fusion 360 before buying a single piece of lumber. The design principle was straightforward: use the full height of the wall to maximize storage without consuming any additional floor footprint. The sofa would sit on a raised platform — part of the frame itself — with drawer storage hidden underneath.

![Fusion 360 design](/assets/images/indentation/indentation ver1.png)

The CAD model let me work through a few constraints before committing:

- **Lumber dimensions**: The entire frame would be built from 2x2 lumber, except for the sofa platform's center beam, which needed 2x4 to handle the load. Everything had to be standard sizes available at the local home center.
- **Disassembly**: Each vertical section was designed as the smallest reusable unit, so the structure could be broken down and reassembled in a different apartment. No glue on the frame joints.
- **Sofa fit**: I modeled the exact sofa dimensions to verify clearance before building anything.

Modeling first also meant I could count every piece of lumber and every joint in advance. This turned out to be important — the project would require drilling hundreds of pocket holes, and knowing the exact count kept the work from feeling infinite.

## The Kreg jig decision

The hardest design choice was the joinery. Screwing 2x2 lumber together with regular screws is a recipe for splitting. The pieces are too narrow; the screw heads show; there's no room for error.

I went with Kreg pocket-hole joinery. The Kreg jig drills angled holes at the end of each piece, and the screws fasten from the inside of the joint — invisible from the outside, and strong enough to hold the frame rigid. It was the most expensive single tool purchase in the project, but it solved three problems at once: hidden fasteners, structural strength, and repeatability across hundreds of identical joints.

Two holes per end, four per joint when both pieces connect. Multiply that by every horizontal beam, every shelf support, every vertical section. Drilling alone took an entire day.

## Building the frame

With all the lumber cut and drilled, assembly went in three stages.

**Stage 1: The sofa base.** Three rectangular frames that would sit on the floor, supporting the sofa above and creating drawer space below. The center frame used 2x4 lumber because the span was wide enough that 2x2 felt unreliable under a person's weight.

**Stage 2: The verticals.** Wall-height sections built as self-contained units. Each one could stand on its own, making it possible to build them flat on the floor and then tilt them into position. This is where the "smallest reusable unit" principle paid off — I could test each section individually before committing it to the whole.

**Stage 3: The horizontals.** Beams connecting the vertical sections into one continuous structure. This is the moment the frame snaps into shape. One day I was looking at a collection of separate ladders; by the end of the afternoon, it was furniture.

## What went wrong

Two things.

**The top-left shelf didn't work as designed.** The original plan had a middle partition dividing the upper-left section into two smaller shelves. Once I saw it assembled, it looked cramped, and it blocked taller items from fitting. I pulled the partition and left it as one open shelf. This was a small change, but it was the first time the physical build diverged from the CAD model — a reminder that no amount of modeling replaces standing in front of the thing and seeing how it feels.

**The sofa base had play.** After placing the sofa on the platform, I could feel a slight wobble in the wooden frame beneath it. The frame was structurally sound, but the connection between the base and the floor wasn't tight enough. I needed a mechanism to lock the frame to the sofa base — something I hadn't designed for. This became a carry-over problem for ver2.

The floor was also covered in wood chips. I'd set up a desk to catch shavings and a bucket for disposal, but pocket-hole drilling throws fine chips in every direction. In a 6-tatami room, there's nowhere for them to go except the floor, your clothes, and somehow the kitchen.

## What I learned

**Model first, but expect the model to be wrong in ways that matter.** The Fusion 360 design saved me from buying the wrong amount of lumber and from building joints that wouldn't fit. It did not tell me that the top-left partition would look bad, or that the sofa base would need a locking mechanism. CAD catches dimensional errors. It doesn't catch experiential ones. Both types of error exist in every project, and you need different tools for each.

**Pocket-hole joinery scales.** For a project with this many joints, the Kreg jig transformed what would have been days of careful screw placement into a repeatable, mechanical process. The upfront cost — both money and the learning curve — was paid back by the hundredth hole. If you're building anything with more than a dozen 2x2 joints, it's worth it.

**Design for disassembly from day one.** We rent. We'll move. Building the verticals as independent units means the whole structure can come apart in an afternoon and go back together in a new room. This constraint actually improved the design — it forced me to think in modules, which made assembly easier too.

After ver1, the room had a frame. It had a sofa sitting on a platform. My wife was happy. But it didn't have storage drawers, it didn't have a top surface for the shelves, and it didn't have lighting. All of that would come in the next versions.

---

*This is the first part of the Indentation Project series. [Part 2](/en/2025/01/20/The-indentation-Project-ver2/) covers the top boards, drawer construction, and storage system. You can also see the [photo gallery for ver1](/en/2025/01/20/The-indentation-Project-ver1/) for the full build documentation.*

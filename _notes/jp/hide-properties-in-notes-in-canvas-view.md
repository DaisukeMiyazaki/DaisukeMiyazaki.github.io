---
layout: note
date: 2026-09-17
title: "Hide properties in notes in Canvas view"
lang: jp
permalink: /jp/notes/hide-properties-in-notes-in-canvas-view/
thumbnail:
---

[canvasだけでプロパティを消す方法を学んだ](https://www.reddit.com/r/ObsidianMD/comments/1mugnn6/hide_properties_in_notes_in_canvas_view/?show=original)。ノートを空間的に有効に使うにはどうしても邪魔になる一方で、個別のノートを開いているときには有効に活用できるプロパティ。メインの設定からプロパティを非表示にしてしまうと、canvasと個別ノートそれぞれに適用されてしまうのでこれで回避できる。

```
.markdown-embed .metadata-container,
 .markdown-embed-content .metadata-container {
   display: none !important;
 }
```

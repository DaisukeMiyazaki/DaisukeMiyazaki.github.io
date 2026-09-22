---
layout: note
date: 2026-09-22
title: "LLMの端的な出力はproviderの利益に反する"
lang: jp
permalink: /jp/notes/2026-09-22-0820-llm-provider-generation-too-long/
thumbnail:
---

LLMの記述は常に冗長になりやすいが、冗長であればあるほど出力token数が増えるのでLLM providerにとって利益となる。逆に端的に短く出力することは利益になりずらい。どれだけプロンプトを改良しても、人間のように端的な出力にはならないのかもしれない。

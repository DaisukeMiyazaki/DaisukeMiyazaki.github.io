---
layout: post
date: 2026-06-25
title: "論文は読むよりまず聞きたい——でも自動ポッドキャストでは物足りなかった"
excerpt: "自動生成のポッドキャストはどんなテキストも自然な音声にしてくれる。でも具体例が薄く、まともな質問もない。だから具体例を厚くし、プロのインタビュアーの型で質問役を設計したパイプラインを作った——一次情報への入口として。"
comments: true
lang: jp
lang-ref: papers-into-podcasts
genre: 実用
thumbnail:
---

## 興味はあっても腰を据えて読めない論文たち

どこかで見かけて「興味はある」のに積まれたままの論文や長文記事がある。好奇心はある。でも、腰を据えて読む集中の時間は、なかなか取れない。読むのは能動的な作業で、その枠を確保するのが難しい。

一方であるのは受動的な時間のほうだ。移動中、散歩、窓の外をぼーっと眺めている数分は意識しなくても訪れる。むしろそういう瞬間がベストで、聞くのは読むのと違ってそこにすっぽり収まる。だから私が欲しいのは、斜め読み用の要約や書き起こしではない。手を空けたまま、ただ聞くだけで入ってくるくらいに平たく噛み砕かれたものである。

## 自動ポッドキャストはほぼ解決してくれる

実は既存のGoogleのツールはこの大半をすでにやってくれる。NotebookLMの音声概要（Audio Overview）や Deep Research の音声機能は、テキストの塊を2人のホストによる自然なポッドキャスト調の会話に変えてくれる。日々の聞き物として、情報収集として、取れない読書時間を取り戻す手段として、これは本当に良い。声は人間らしく、トーンも決まっている。

ただ、しばらく使うと限界が見えてくる。具体例が薄かったり、尺も自分でコントロールできない。説明はするが、腑に落ちさせてはくれない。包括的でなかったりするのだ。名ホストがゲストから鮮やかで具体的な例を引き出す本物のポッドキャストと並べると、自動版は平板に感じる。論文が何を言っているかは伝わるのに、刺さってはこない。

## だから自動版が飛ばす部分を作った

汎用版が弱いのは2つ——具体例と質問である。ここを作り込んだ。
まず大きな2つの役割に分けて台本を作成する。

**説明役の本業は「翻訳」である**。 抽象的な主張には必ず具体例か比喩を添える。専門用語が出たらその場でほどく。裸の専門用語は1つも残さない。

**質問役はリスナーの代理人である**。 「最高のポッドキャスト・インタビュアー10人」のリストを調べ[^interviewers]、各人が語る技術を読み、理解を前に進めるハードスキルだけを敢えて抜き出した。短く問う、直前の発言を受けて掘る、リスナーがつまずくその場所を代弁する、網羅でなく核心へ寄せる、具体例を要求する。温かさ・ラポール・ユーモアそのものといったソフトスキルは、この文脈では台本にノイズが入ったり、エージェント相手の文脈では幻覚を引き起こす恐れがあり意図的に捨てた。

パイプラインはいたって簡単である。PDFを取り込み、抽出し、論理を地図にし、具体例つきで平易に噛み砕き、15〜30分に尺を見積もり、2声の対話に書き起こし、原文と突き合わせて検証する。そのうえで [Gemini 3.1 Flash TTS](https://ai.google.dev/gemini-api/docs/speech-generation) が自然な声を与える——ここは自動ポッドキャストがすでに得意な部分なので、機械に任せている。

音声化はこの小さなスクリプトにまとめてある（声を固定し、間を入れ、モデルの上限に合わせてチャンク分割）: [gemini_tts.py](https://gist.github.com/DaisukeMiyazaki/5fb8e0333d7fe940aa9262b4d790eeb2)。

## どこで失敗したか

初期にはgemini-2.5を使ったがテンポが速すぎた。とんとん拍子で、2つの声が息継ぎもなく打ち合う。効率的に聞こえて、聞いていて疲れる。直し自体は小さいがターンの間に「間」を入れ、落ち着いた話し方にし、急がないよう演出指示を足す。**間が要る**ことに大きく気づいた。

驚くべきことに、Gemini 3.1 Flash TTSではこの間だったり話してのトーン--いわゆるソフトスキルに相当しそうな部分をモデル側が補ってくれている。2.5と聴き比べて差は明らかであった。

## まとめ

このツールの役割は「噛み砕いて、**一次情報に触れやすくする**」ことだ。要約や音声は、本来なら一生開かなかった論文への入口であって、原文の代わりではない。「知っておきたい」程度なら、ただ概要を読むよりもグッと理解が進む。けれど引っかかった論文なら、聞いて終わりにせず原文にあたり、自分の言葉で噛み砕く——その消化は自分でやらないといけない。[散歩の話](/jp/2025/09/16/sanpou-issue/)で書いたように、AIが代わりに生み出せない「一次の気づき」は、結局そこからしか出てこないと思う。


このツールにも限界があり、台本を作らせ、具体例をきいてもわからないこともある。それは台本作りにフォーマット化された問いではなく自分の言葉で agent に聞く。例えば自分の場合、論文そのものをコンテキストに置いたまま、必要なら図にも起こしてもらったりする。そしてその解消をObsidian にまとめていく。地道だが一点ずつ潰していくことで、聞いただけの話が少しずつ自分の血肉に変わっていく。[理解を委任してはいけない](/jp/2025/07/03/understanding-delegation/)。

なお、生成した音声も台本も権利上ここでは公開していない（音声は台本の読み上げで、中身は同じ二次的著作物だ）。元論文の著作権者の許諾なく配布するのは避け、あくまで自分の個人利用にとどめている。同じ仕組みを使う場合も、各自が正当に入手した文献を自分の範囲で噛み砕く用途に留めてほしい。

[^interviewers]: 出典: Frank Racioppi「[The Ten Best Interviewers In Podcasting](https://podalization.substack.com/p/the-ten-best-interviewers-in-podcasting)」(Ear Worthy / Pod-Alization, 2023)。この記事を起点に、各ホスト本人の発言・ブログ・インタビューを調査して整理した。各ホストの一次ソース: [Michael Barbaro](https://www.pressclubinstitute.org/2020/07/20/terry-gross-and-michael-barbaro-share-interview-tips-and-techniques/)、[David Pogue](https://pogueman.substack.com/p/pogues-top-ten-interview-tips)、[Audie Cornish](https://www.cjr.org/special_report/qa-nprs-audie-cornish-on-the-intimacy-of-interviewing.php)、[Elaine Appleton Grant](https://soundjudgment.substack.com/p/interviews-are-the-foundation-of)、[Robert Peterpaul](https://vocal.media/interview/the-art-of-kindness-podcast-a332g0iko)、[Mike Carruthers](https://www.somethingyoushouldknow.net/about/)、[Evan Stern](https://tinkmedia.co/interviews/evan-stern)、[Matt Gilhooly](https://veritysangan.com/podcast-archive/ep-58-getting-curious-and-hosting-amazing-guest-interviews-with-matt-gilhooly/)、[Jordan Harbinger](https://www.podcastjunkies.com/jordan-harbinger-interview-2/)、[Zale Mednick](https://booktime584.wordpress.com/2023/04/04/preconceivedinterview/)。

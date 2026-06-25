---
layout: post
date: 2026-06-25
title: "論文は読むよりまず聞きたい——でも自動ポッドキャストでは物足りなかった"
excerpt: "自動生成のポッドキャストはどんなテキストも自然な音声にしてくれます。でも具体例が薄く、まともな質問もありません。だから具体例を厚くし、一時情報への入り口として、プロのインタビュアーの型で質問役を設計したパイプラインを作りました。"
comments: true
lang: jp
lang-ref: papers-into-podcasts
genre: 実用
thumbnail:
---

## 興味はあっても腰を据えて読めない論文たち

どこかで見かけて「興味はある」のに積まれたままの論文や長文記事があります。好奇心はあります。でも、腰を据えて読む集中の時間は、なかなか取れません。読むのは能動的な作業で、その枠を確保するのが難しいのです。

一方であるのは、受動的な時間のほうです。移動中、散歩、窓の外をぼーっと眺めている数分は、意識しなくても訪れます。むしろそういう瞬間がベストで、聞くのは読むのと違ってそこにすっぽり収まります。だから私が欲しいのは、斜め読み用の要約や書き起こしではありません。手を空けたまま、ただ聞くだけで入ってくるくらいに平たく噛み砕かれたものです。

## 自動ポッドキャストはほぼ解決してくれる

実は、既存のGoogleのツールはこの大半をすでにやってくれます。NotebookLMの音声概要（Audio Overview）や Deep Research の音声機能は、テキストの塊を2人のホストによる自然なポッドキャスト調の会話に変えてくれます。日々の聞き物として、情報収集として、取れない読書時間を取り戻す手段として、これは本当に良いです。声は人間らしく、トーンも決まっています。

ただ、しばらく使うと限界が見えてきます。具体例が薄かったり、尺も自分でコントロールできなかったりします。説明はしてくれますが、腑に落ちさせてはくれません。包括的でないこともあります。名ホストがゲストから鮮やかで具体的な例を引き出す本物のポッドキャストと並べると、自動版は平板に感じます。論文が何を言っているかは伝わるのに、刺さってはこないのです。

## だから自動版が飛ばす部分を作った

汎用版が弱いのは2つ——具体例と質問です。ここを作り込みました。まず、大きな2つの役割に分けて台本を作成します。

**説明役の本業は「翻訳」です**。 抽象的な主張には必ず具体例か比喩を添えます。専門用語が出たらその場でほどきます。裸の専門用語は1つも残しません。

**質問役はリスナーの代理人です**。 「最高のポッドキャスト・インタビュアー10人」のリストを調べ[^interviewers]、各人が語る技術を読み、理解を前に進めるハードスキルだけを敢えて抜き出しました。短く問う、直前の発言を受けて掘る、リスナーがつまずくその場所を代弁する、網羅でなく核心へ寄せる、具体例を要求する——といった型です。温かさ・ラポール・ユーモアそのものといったソフトスキルは、この文脈では台本にノイズが入ったり、エージェント相手では幻覚を引き起こす恐れがあるため、意図的に捨てました。

パイプラインはいたって簡単です。PDFを取り込み、抽出し、論理を地図にし、具体例つきで平易に噛み砕き、15〜30分に尺を見積もり、2声の対話に書き起こし、原文と突き合わせて検証します。そのうえで [Gemini 3.1 Flash TTS](https://ai.google.dev/gemini-api/docs/speech-generation) が自然な声を与えてくれます——ここは自動ポッドキャストがすでに得意な部分なので、機械に任せています。

音声化は、この小さなスクリプトにまとめてあります（声を固定し、間を入れ、モデルの上限に合わせてチャンク分割しています）: [gemini_tts.py](https://gist.github.com/DaisukeMiyazaki/5fb8e0333d7fe940aa9262b4d790eeb2)。

## どこで失敗したか

初期にはgemini-2.5を使いましたが、テンポが速すぎました。とんとん拍子で、2つの声が息継ぎもなく打ち合います。効率的に聞こえて、聞いていて疲れます。直し自体は小さく、ターンの間に「間」を入れ、落ち着いた話し方にし、急がないよう演出指示を足しました。**間が要る**ことに、大きく気づかされました。

驚くべきことに、Gemini 3.1 Flash TTSでは、この「間」や話し手のトーン——いわゆるソフトスキルに相当しそうな部分を、モデル側が補ってくれています。2.5と聴き比べると、差は明らかでした。

## まとめ

このツールの役割は、「噛み砕いて、**一次情報に触れやすくする**」ことです。要約や音声は、本来なら一生開かなかった論文への入口であって、原文の代わりではありません。「知っておきたい」程度なら、ただ概要を読むよりもグッと理解が進みます。けれど引っかかった論文なら、聞いて終わりにせず原文にあたり、自分の言葉で噛み砕く——その消化は自分でやらないといけません。[散歩の話](/jp/2025/09/16/sanpou-issue/)で書いたように、AIが代わりに生み出せない「一次の気づき」は、結局そこからしか出てこないと思います。

このツールにも限界があり、台本を作らせ、具体例をきいてもわからないことがあります。そういうときは、フォーマット化された問いではなく、自分の言葉で agent に聞きます。例えば私の場合、論文そのものをコンテキストに置いたまま、必要なら図にも起こしてもらったりします。そして、その解消を Obsidian にまとめていきます。地道ですが、一点ずつ潰していくことで、聞いただけの話が少しずつ自分の血肉に変わっていきます。[理解を委任してはいけない](/jp/2025/07/03/understanding-delegation/)。

なお、生成した音声も台本も、権利上ここでは公開していません（音声は台本の読み上げで、中身は同じ二次的著作物です）。元論文の著作権者の許諾なく配布するのは避け、あくまで自分の個人利用にとどめています。同じ仕組みを使う場合も、各自が正当に入手した文献を、自分の範囲で噛み砕く用途に留めていただければと思います。

[^interviewers]: 出典: Frank Racioppi「[The Ten Best Interviewers In Podcasting](https://podalization.substack.com/p/the-ten-best-interviewers-in-podcasting)」(Ear Worthy / Pod-Alization, 2023)。この記事を起点に、各ホスト本人の発言・ブログ・インタビューを調査して整理しました。各ホストの一次ソース: [Michael Barbaro](https://www.pressclubinstitute.org/2020/07/20/terry-gross-and-michael-barbaro-share-interview-tips-and-techniques/)、[David Pogue](https://pogueman.substack.com/p/pogues-top-ten-interview-tips)、[Audie Cornish](https://www.cjr.org/special_report/qa-nprs-audie-cornish-on-the-intimacy-of-interviewing.php)、[Elaine Appleton Grant](https://soundjudgment.substack.com/p/interviews-are-the-foundation-of)、[Robert Peterpaul](https://vocal.media/interview/the-art-of-kindness-podcast-a332g0iko)、[Mike Carruthers](https://www.somethingyoushouldknow.net/about/)、[Evan Stern](https://tinkmedia.co/interviews/evan-stern)、[Matt Gilhooly](https://veritysangan.com/podcast-archive/ep-58-getting-curious-and-hosting-amazing-guest-interviews-with-matt-gilhooly/)、[Jordan Harbinger](https://www.podcastjunkies.com/jordan-harbinger-interview-2/)、[Zale Mednick](https://booktime584.wordpress.com/2023/04/04/preconceivedinterview/)。

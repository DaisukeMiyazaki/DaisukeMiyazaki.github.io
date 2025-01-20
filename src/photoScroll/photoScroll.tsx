import React, { useRef } from "react";

interface ImageData {
  id: number;
  src: string;
  description: string;
}

const images: ImageData[] = [
  {
    id: 1,
    src: "https://storage.googleapis.com/daisukemiyazaki_website/builds/front.jpeg",
    description:
      "こんにちは、皆さん！先月頭、アート愛好者の妻のために、どこにも売っていない特別なワークベンチを作る挑戦をしてみました。妻がアートを楽しんでいる様子を見るのは素晴らしいこと。でも5畳もないお部屋で散らかり具合...収納が足りない！そして、どうしても座って書いていると姿勢が...そこで立ったままアートを楽しむことができるワークベンチがあれば、こんな悩みも解消されるんじゃないかと。そう思って作りはじめてみました。それでは、DIYの開始です！",
  },
  {
    id: 2,
    src: "https://storage.googleapis.com/daisukemiyazaki_website/builds/test0.jpeg",
    description: "座っている状態だとどうしても目線が下がってしまいます。",
  },
  {
    id: 3,
    src: "https://storage.googleapis.com/daisukemiyazaki_website/builds/test1.jpeg",
    description: "この高さだと、まだ顔が下を向いていて首が疲れてしまいそう。",
  },
  {
    id: 4,
    src: "https://storage.googleapis.com/daisukemiyazaki_website/builds/test3.jpeg",
    description:
      "この高さなら、全体的にまっすぐになっていて良さそう。立った時と比較しても、大体同じくらい中心線になっているのがわかります。こちらで高さは110センチくらいが良さそうだとわかりました。",
  },
  {
    id: 5,
    src: "https://storage.googleapis.com/daisukemiyazaki_website/builds/cad.jpeg",
    description:
      "次に3Dモデリングで設計します。全体のバランスや重心の計算、イメージのすり合わせなどを妻のフィードバックを得ながら作っていきます。こだわった点は...",
  },
  {
    id: 6,
    src: "https://storage.googleapis.com/daisukemiyazaki_website/builds/inProgress.jpeg",
    description:
      "木材が届いたら、あとは作るのみ。イメージ通りに作っていきます。こちら途中経過...",
  },
  {
    id: 7,
    src: "https://storage.googleapis.com/daisukemiyazaki_website/builds/miniTruck.jpeg",
    description:
      "扉は寸法もモデルで見ていた通りにならなかったので後付けにしました。買い出しに再度ホームセンターのコーナンへ、暑いので自転車でむかったものの巨大すぎるドアをどうも運べず。再度配送料を払うのもバカバカしい。。。",
  },
  {
    id: 8,
    src: "https://storage.googleapis.com/daisukemiyazaki_website/builds/miniTruck2.jpeg",
    description:
      "そんなときなんと、コーナンでは軽トラを無料で借りれることが判明。ハンドルつき、普通免許で運転できることも初めて知りました。おかげ様でスムーズに運ぶことができました。",
  },
  {
    id: 9,
    src: "https://storage.googleapis.com/daisukemiyazaki_website/builds/hotMan.jpeg",
    description:
      "仕上げにはニス塗りもしっかりと。あっつい部屋でもしっかりと換気をしつつ。真夏のクーラーの効かない部屋で二重マスク。",
  },
  {
    id: 10,
    src: "https://storage.googleapis.com/daisukemiyazaki_website/builds/legs.jpeg",
    description:
      "仕上げには転倒対策。大きなものなのでこちらも必須です。モデルでは足を強固にする予定だったけれど加工が手間で面倒くさい。。。色々考えてみた結果、ホームセンターで見つけたこいつ一枚で解決。",
  },
  {
    id: 11,
    src: "https://storage.googleapis.com/daisukemiyazaki_website/builds/seita.jpeg",
    description: "また、横揺れもしたので背板をつけることで解消しました。",
  },
  {
    id: 12,
    src: "https://storage.googleapis.com/daisukemiyazaki_website/builds/front.jpeg",
    description: "ついに完成！",
  },
  {
    id: 13,
    src: "https://storage.googleapis.com/daisukemiyazaki_website/builds/front2.jpeg",
    description: "完成したワークベンチ",
  },
  {
    id: 14,
    src: "https://storage.googleapis.com/daisukemiyazaki_website/builds/front3.jpeg",
    description: "完成したワークベンチ",
  },
  {
    id: 15,
    src: "https://storage.googleapis.com/daisukemiyazaki_website/builds/tableWidth.jpeg",
    description: "折りたたみ式の天板も180cm * 50cmと十分な広さがあります。",
  },
  {
    id: 16,
    src: "https://storage.googleapis.com/daisukemiyazaki_website/builds/faceToCamera.jpeg",
    description: "折りたたみ式の天板も180cm * 50cmと十分な広さがあります。",
  },
  {
    id: 17,
    src: "https://storage.googleapis.com/daisukemiyazaki_website/builds/positionCheck.jpeg",
    description:
      "立った時の姿勢も、測ったときの姿勢とほぼ一致しています。これで快適にアートに取り組めるはず！",
  },
  {
    id: 18,
    src: "https://storage.googleapis.com/daisukemiyazaki_website/builds/foldedTableTop.jpeg",
    description:
      "天板が扉の役割も兼用し、コードなども隠して見た目もすっきりするように。",
  },
  {
    id: 19,
    src: "https://storage.googleapis.com/daisukemiyazaki_website/builds/mount.jpeg",
    description:
      "天板が扉の役割も兼用し、コードなども隠して見た目もすっきりするように。",
  },
  {
    id: 20,
    src: "https://storage.googleapis.com/daisukemiyazaki_website/builds/codes.jpeg",
    description:
      "天板が扉の役割も兼用し、コードなども隠して見た目もすっきりするように。",
  },
  {
    id: 21,
    src: "https://storage.googleapis.com/daisukemiyazaki_website/builds/front.jpeg",
    description:
      "いかがでしょうか？皆さんも、身近なものやサービスを利用しながら、特別なものをDIYで作って贈ってみてはみてはいかがでしょうか？",
  },
];

const ImageGallery = () => {
  const imageRefs = useRef<(HTMLDivElement | null)[]>([]);

  // show an image one by one streached to the screen, and scroll to the next image when the user scrolls
  // description is displayed on the image

  // as the user scrolls, description changes
  // when the user scrolls to the next image, the description of the next image is displayed

  return (
    <>
      <div className="h-screen w-fit snap-y snap-mandatory overflow-y-scroll">
        {images.map((image, index) => (
          <div
            key={image.id}
            className="relative snap-center snap-always"
            ref={(el: HTMLDivElement | null) => (imageRefs.current[index] = el)}
            data-index={index}
          >
            <img
              src={image.src}
              alt={`Image ${image.id}`}
              className="h-screen w-full object-cover"
            />

            <div className="pointer-events-none absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 transform whitespace-pre-wrap rounded bg-white bg-opacity-50 p-2 text-lg text-black transition-opacity duration-300">
              {image.description}
            </div>
          </div>
        ))}
      </div>
    </>
  );
};

export default ImageGallery;

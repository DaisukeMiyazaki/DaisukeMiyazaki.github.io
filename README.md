## ローカルサーバーでの立ち上げ

```
cd DaisukeMiyazaki.github.io
bundle exec jekyll serve
```

## cssの編集
ローカルサーバーを立ち上げると、自動的にassets/css/main.scssを読み込みコンパイルを行う。
編集するのは、_sass/以下のpartialsファイル

## 詳細テキストの入れかた
```
<details markdown=block>
<summary markdown=span>want to see the detail?</summary>
this is an example text
</details>
```

## backendserverについて
pythonanywhereを用いてflaskを走らせています。linkは[こちら](https://www.pythonanywhere.com/user/mDaisukeNet/webapps/#tab_id_mdaisukenet_pythonanywhere_com)
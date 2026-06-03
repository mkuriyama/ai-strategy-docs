# ai-strategy-docs

AI戦略実践プロジェクトのドキュメントサイト（**MkDocs Material** + **GitHub Pages**）。

「ボキャブラリーリスト（用語集）」と「スタートガイド」を、検索・相互リンク・
用語ツールチップに対応したドキュメントサイトとして公開します。

## 機能

- MkDocs Material テーマ
- 日本語全文検索（CJK 分割対応）
- 用語ツールチップ（`abbreviations` 拡張）— スタートガイド本文の用語にカーソルを合わせると定義を表示
- 用語集ページ ⇄ スタートガイドページの相互リンク
- ライト／ダークモード切り替え
- GitHub Actions による GitHub Pages への自動デプロイ

## ディレクトリ構成

```
.
├─ mkdocs.yml                    # サイト設定
├─ requirements.txt              # 依存（mkdocs-material）
├─ .github/workflows/ci.yml      # 自動デプロイ
└─ docs/
   ├─ index.md                   # ホーム
   ├─ start-guide.md             # スタートガイド
   ├─ glossary.md                # ボキャブラリーリスト（用語集）
   └─ includes/
      └─ abbreviations.md        # ツールチップ用 用語定義（全ページに自動付与）
```

## ローカルでのプレビュー

```bash
pip install -r requirements.txt
mkdocs serve            # http://127.0.0.1:8000 で確認
mkdocs build            # site/ に静的ファイルを生成
```

## 本文の差し替え方法（重要）

現在の `docs/start-guide.md` / `docs/glossary.md` / `docs/includes/abbreviations.md`
の本文は **動作確認用のサンプル** です。元の PDF（または生成スクリプト）の本文に
差し替えてください。

1. **スタートガイド**: `docs/start-guide.md` の本文を置き換え。
2. **用語集**: `docs/glossary.md` の用語と定義を置き換え。
3. **ツールチップ**: `docs/includes/abbreviations.md` に
   `*[用語]: 定義` 形式で各用語を記載（用語集と同じ定義にそろえる）。
   ここに登録した用語が、全ページ本文中でツールチップ表示されます。

> ヒント: 用語集と `abbreviations.md` は定義を一致させると保守しやすくなります。

## デプロイ（GitHub Pages）

`main` ブランチへ push すると GitHub Actions が走り、`mkdocs gh-deploy` で
`gh-pages` ブランチへサイトを発行します。

初回のみ、リポジトリの **Settings → Pages** で以下を設定してください。

- **Source**: `Deploy from a branch`
- **Branch**: `gh-pages` / `(root)`

公開 URL: `https://mkuriyama.github.io/ai-strategy-docs/`

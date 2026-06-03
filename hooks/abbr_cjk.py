"""MkDocs hook: 日本語（CJK）対応の abbreviations ツールチップ。

python-markdown 標準の `abbr` 拡張は用語マッチに単語境界 `\\b` を用いるため、
「プロンプト」のように日本語の文中に空白なしで埋め込まれた用語を検出できません
（CJK 文字はすべて「単語文字」と見なされ、隣接する日本語との間に境界が生じない）。

この hook は `AbbrTreeprocessor.run` を差し替え、用語の端の文字種に応じて境界を
切り替えます。

- 端が ASCII 英数字の用語（API, RAG など）: ASCII の単語境界を維持
  （例: "RAPID" の中の "API" にはマッチしない）。
- 端が日本語などの用語（プロンプト など）: 境界を要求せず、文中どこでもマッチ。

これにより、用語集の各用語がスタートガイド本文中でツールチップ表示されます。
"""

from __future__ import annotations

import re

try:
    from markdown.extensions.abbr import AbbrTreeprocessor
except Exception:  # pragma: no cover - 拡張が無い場合は何もしない
    AbbrTreeprocessor = None


_ASCII_WORD = re.compile(r"[0-9A-Za-z_]")


def _pattern(key: str) -> str:
    """用語 1 件分の、文字種を考慮した正規表現パターンを返す。"""
    esc = re.escape(key)
    left = r"(?<![0-9A-Za-z_])" if _ASCII_WORD.match(key[0]) else ""
    right = r"(?![0-9A-Za-z_])" if _ASCII_WORD.match(key[-1]) else ""
    return left + esc + right


def _patched_run(self, root):
    """標準実装と同じだが、CJK 対応の境界で正規表現を構築する。"""
    if not self.abbrs:
        return
    # 長い用語を優先（"生成AI" を "AI" より先に判定させる）
    keys = sorted(self.abbrs.keys(), key=len, reverse=True)
    self.RE = re.compile("(?:" + "|".join(_pattern(k) for k in keys) + ")")
    self.iter_element(root)


# import 時にパッチを適用（MkDocs が hook を読み込んだ時点で有効化）
if AbbrTreeprocessor is not None:
    AbbrTreeprocessor.run = _patched_run

#!/usr/bin/env python3

import argparse
import sys
from pathlib import Path

STEPS = {
    "1": """1段階目
- 答えを見ずに5分考える。わからなかったら答えを見る。
- 答えを見て理解したと思ったら答えを隠して書く。
- 筆が進まず5分迷ったら答えを見る。答えを見たら全部消してやり直し。
- 答えを見ずに正解したら一段階目は完了。
""",
    "2": """2段階目
- コードを読みやすくするように整える。
- 動くコードになったら二段階目は完了。

ほかの人の解答を読む。
PR に memo.md を用意して疑問や感想を書くのもいい。
""",
    "3": """3段階目
- すべて消して書き直す。
- アクセプトされたらもう一度消して書く
- 10 分以内に一回もエラーを出さずに書ける状態になるまで続ける。（時間は理念に従い調整）
- 「10 分以内にエラーなしで書く」を 3 回続けてできたら三段階目は完了。
"""
}

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description="ディレクトリごとに stepX.<ext> を生成します。"
    )
    parser.add_argument(
        "step",
        choices=["1", "2", "3", "all"],
        help="出力するステップ。all で 1,2,3 全てを生成。"
    )
    parser.add_argument(
        "extension",
        help="生成ファイルの拡張子（例: ts, cpp, py）。"
    )
    parser.add_argument(
        "pattern",
        nargs="?",
        default=".",
        help="ターゲットディレクトリの glob パターン。省略時はカレントディレクトリ。"
    )
    return parser.parse_args()

def main() -> None:
    args = parse_args()

    root = Path(__file__).resolve().parent.parent
    if args.pattern == ".":
        dirs = [Path.cwd()]
    else:
        dirs = [d for d in sorted(root.glob(args.pattern)) if d.is_dir()]
    if not dirs:
        sys.exit("対象ディレクトリが見つかりません。")

    steps = ["1", "2", "3"] if args.step == "all" else [args.step]
    for directory in dirs:
        for step in steps:
            file_path = directory / f"step{step}.{args.extension}"
            file_path.write_text(STEPS[step], encoding="utf-8")
            print(f"{file_path} を生成しました。")

if __name__ == "__main__":
    main()


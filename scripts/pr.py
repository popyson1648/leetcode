#!/usr/bin/env python3

import argparse
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

IN_FILE = "input.txt"
OUT_FILE = "output.txt"
FILE_STRUCTURE = [
    "ファイル構成: ",
    "memo.md: ほかの人の解答を見た際の疑問や解答が書かれています。"
]

def process_text(text: str, date_str: str) -> str:
    title_m = re.search(r"#ProblemName:\s*(.+)", text)
    link_m  = re.search(r"#ProblemLink:\s*(.+)", text)
    raw_m   = re.search(r"#Link:\s*(.+)", text, re.DOTALL)

    lines: list[str] = []
    if title_m:
        lines.append(title_m.group(1).strip())
    if link_m:
        lines.append(link_m.group(1).strip())
        lines.append("")

    if raw_m:
        urls = re.findall(r"https?://.+?(?=https?://|$)", raw_m.group(1).strip())
        if urls:
            lines.append(f"同じ問題を解いた方のPRリンク集 ({date_str} 時点) :")
            lines.extend(urls)
            lines.append("")

    lines.extend(FILE_STRUCTURE)
    return "\n".join(lines)

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description="input.txt を整形して output.txt を生成し、GitHub PR を作成します。"
    )
    parser.add_argument(
        "pattern",
        help="ターゲットディレクトリの glob パターン。'.' でカレントディレクトリ。"
    )
    return parser.parse_args()

def main() -> None:
    args = parse_args()
    pattern = args.pattern

    root = Path(__file__).resolve().parent.parent
    dirs = [Path.cwd()] if pattern == "." else [d for d in sorted(root.glob(pattern)) if d.is_dir()]
    if not dirs:
        sys.exit(f"対象ディレクトリが見つかりません: {pattern}")

    date_str = datetime.today().strftime("%Y/%m/%d")
    for d in dirs:
        in_path = d / IN_FILE
        if not in_path.exists():
            print(f"{in_path} が見つかりません。")
            continue

        out_path = d / OUT_FILE
        formatted = process_text(in_path.read_text(encoding="utf-8"), date_str)
        try:
            out_path.write_text(formatted, encoding="utf-8")
            print(f"{out_path} を生成しました。")
        except Exception as e:
            sys.exit(f"output.txt の生成に失敗しました: {e}")

        title = formatted.splitlines()[0]
        try:
            subprocess.run(
                ["gh", "pr", "create", "--title", title, "--body-file", str(out_path)],
                check=True
            )
            print("プルリクエストを作成しました。")
        except subprocess.CalledProcessError as e:
            sys.exit(f"gh pr create に失敗しました: {e}")

if __name__ == "__main__":
    main()


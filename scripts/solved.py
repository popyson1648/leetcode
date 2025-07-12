#!/usr/bin/env python3

import argparse
from pathlib import Path
from typing import List
import os

def parse_args():
    p = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description="solved から @lc ブロックを取り除き保存する"
    )
    p.add_argument("step", choices=["1", "2", "3"],
                   help="ファイル名 stepX を決定する番号")
    p.add_argument("ext", help="保存時の拡張子")
    p.add_argument("-any", dest="any_name", nargs=1,
                   help="任意ファイル名を指定する場合に使用")
    p.add_argument("dest", help="保存先ディレクトリ ('.' でカレント)")
    return p.parse_args()

def strip_blocks(lines: List[str]) -> List[str]:
    out: List[str] = []
    state = "prefix"       # prefix / skip / code / after
    for ln in lines:
        if state == "prefix":
            if "/*" in ln:
                state = "skip"
                continue
            out.append(ln)
        elif state == "skip":
            if "// @lc code=start" in ln or "// @lc code-start" in ln:
                state = "code"
            continue
        elif state == "code":
            if "// @lc code=end" in ln or "// @lc code-end" in ln:
                state = "after"
                continue
            out.append(ln)
        else:  # after
            out.append(ln)

    compact: List[str] = []
    prev_blank = False
    for ln in out:
        blank = ln.strip() == ""
        if blank and prev_blank:
            continue
        compact.append(ln)
        prev_blank = blank
    return compact

def main():
    args = parse_args()
    src = Path("solution")
    if not src.exists():
        raise SystemExit("solution ファイルが見つかりません。")

    lines = src.read_text(encoding="utf-8").splitlines(keepends=True)
    cleaned = "".join(strip_blocks(lines))

    base = args.any_name[0] if args.any_name else f"step{args.step}"
    dest_path = Path(args.dest) / f"{base}.{args.ext}"
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    dest_path.write_text(cleaned, encoding="utf-8")
    print(f"Created {dest_path}")

if __name__ == "__main__":
    main()


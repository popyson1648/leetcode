#!/usr/bin/env python3
import argparse
import os
import sys
import tempfile
import shutil

HEADERS = {
    '1': """1段階目
- 答えを見ずに5分考える。わからなかったら答えを見る。
- 答えを見て理解したと思ったら答えを隠して書く。
- 筆が進まず5分迷ったら答えを見る。答えを見たら全部消してやり直し。
- 答えを見ずに正解したら一段階目は完了。
""",
    '2': """2段階目
- コードを読みやすくするように整える。
- 動くコードになったら二段階目は完了。

ほかの人の解答を読む。
PRに memo.md を用意して疑問や感想を書くのもいい。
""",
    '3': """3段階目
- すべて消して書き直す。
- アクセプトされたらもう一度消して書く
- 10分以内に一回もエラーを出さずに書ける状態になるまで続ける。(時間は理念に従い調整)
- 「10分以内にエラーなしで書く」を3回続けてできたら三段階目は完了。
"""
}

def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument('step', choices=['1', '2', '3'])
    ap.add_argument('path', nargs='?', default='.')
    return ap.parse_args()

def resolve_solution_path(p: str) -> str:
    if os.path.isdir(p):
        return os.path.join(p, 'solution')
    return p

def main():
    args = parse_args()
    sol_path = resolve_solution_path(args.path)

    if not os.path.isfile(sol_path):
        sys.exit(f'File not found: {sol_path}')

    with open(sol_path, encoding='utf-8') as f:
        body = f.read()

    header = HEADERS[args.step].rstrip('\n')
    new_content = header + '\n\n' + body.lstrip('\n')

    tmp_fd, tmp_path = tempfile.mkstemp()
    with os.fdopen(tmp_fd, 'w', encoding='utf-8') as tmp:
        tmp.write(new_content)

    shutil.move(tmp_path, sol_path)
    print(f'Updated {sol_path}')

if __name__ == '__main__':
    main()


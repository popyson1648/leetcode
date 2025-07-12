
#!/bin/sh

# Usage: ./create.sh <pattern|.> <1|2|3|all> <extension>

set -eu

STEPS_1="=================================== 
1段階目 
- 答えを見ずに5分考える。わからなかったら答えを見る。 
- 答えを見て理解したと思ったら答えを隠して書く。 
- 筆が進まず5分迷ったら答えを見る。答えを見たら全部消してやり直し。 
- 答えを見ずに正解したら一段階目は完了。 
==================================="

STEPS_2="=================================== 
2段階目 
- コードを読みやすくするように整える。 
- 動くコードになったら二段階目は完了。 

ほかの人の解答を読む。 
PRに memo.md を用意して疑問や感想を書くのもいい。 
==================================="

STEPS_3="=================================== 
3段階目 
- すべて消して書き直す。 
- アクセプトされたらもう一度消して書く 
- 10分以内に一回もエラーを出さずに書ける状態になるまで続ける。(時間は理念に従い調整) 
- 「10分以内にエラーなしで書く」を3回続けてできたら三段階目は完了。 
==================================="

if [ $# -ne 3 ]; then
  echo "Usage: $0 <pattern|.> <1|2|3|all> <extension>" >&2
  exit 1
fi

pattern="$1"
step_arg="$2"
ext="$3"

# 対象ディレクトリを決定
if [ "$pattern" = "." ]; then
  dirs="."
else
  dirs=$(find "$(dirname "$0")/.." -maxdepth 1 -type d -name "$pattern" | sort)
fi

# ディレクトリが見つからなければ終了
if [ -z "$dirs" ]; then
  exit 1
fi

# 作成対象ステップ
if [ "$step_arg" = "all" ]; then
  steps="1 2 3"
else
  case "$step_arg" in
    1|2|3) steps="$step_arg" ;;
    *) exit 1 ;;
  esac
fi

# ファイル作成
for dir in $dirs; do
  for step in $steps; do
    filename="step${step}.${ext}"
    filepath="${dir}/${filename}"
    case "$step" in
      1) echo "$STEPS_1" > "$filepath" ;;
      2) echo "$STEPS_2" > "$filepath" ;;
      3) echo "$STEPS_3" > "$filepath" ;;
    esac
    echo "$filepath を生成しました。"
  done
done


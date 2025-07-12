
#!/bin/sh

# Usage: ./format.sh 33*

set -eu

IN_FILE="input.txt"
OUT_FILE="output.txt"
FILE_STRUCTURE="ファイル構成:
memo.md: ほかの人の解答を見た際の疑問や解答が書かれています。"

if [ $# -ne 1 ]; then
  echo "使い方: ./format.sh <pattern>"
  exit 1
fi

pattern="$1"
root=$(cd "$(dirname "$0")/.." && pwd)
dirs=$(find "$root" -maxdepth 1 -type d -name "$pattern" | sort)

if [ -z "$dirs" ]; then
  echo "対象ディレクトリが見つかりません: $pattern"
  exit 1
fi

date_str=$(date +"%Y/%m/%d")

for dir in $dirs; do
  in_path="$dir/$IN_FILE"
  out_path="$dir/$OUT_FILE"

  if [ ! -f "$in_path" ]; then
    echo "$in_path が見つかりません。"
    continue
  fi

  text=$(cat "$in_path")

  title=$(printf "%s\n" "$text" | grep -E "^#ProblemName:" | sed -E 's/^#ProblemName:[[:space:]]*//')
  link=$(printf "%s\n" "$text" | grep -E "^#ProblemLink:" | sed -E 's/^#ProblemLink:[[:space:]]*//')
  raw=$(printf "%s\n" "$text" | grep -A1000 "^#Link:" | sed -E '1s/^#Link:[[:space:]]*//')

  urls=$(printf "%s\n" "$raw" | grep -oE "https?://[^ ]+" | sed '/^$/d')

  {
    [ -n "$title" ] && echo "$title"
    [ -n "$link" ] && {
      echo "$link"
      echo ""
    }
    [ -n "$urls" ] && {
      echo "同じ問題を解いた方のPRリンク集 ($date_str 時点) :"
      echo "$urls"
      echo ""
    }
    echo "$FILE_STRUCTURE"
  } > "$out_path"

  echo "$out_path を生成しました。"

  if [ -n "$title" ]; then
    if ! gh pr create --title "$title" --body-file "$out_path"; then
      echo "gh pr create に失敗しました。"
      exit 1
    fi
    echo "プルリクエストを作成しました。"
  fi
done


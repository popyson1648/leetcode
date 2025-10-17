## `insert.py`

`solution` ファイルにステップヘッダーを挿入します。

**Usage:** `python scripts/insert.py <step> [path]`

| 引数     | 説明                                                         |
| :------- | :----------------------------------------------------------- |
| `<step>` | 挿入するヘッダーのステップ番号 (`1`, `2`, `3`)。             |
| `[path]` | (任意) `solution` を含むファイルまたはディレクトリへのパス。 |

**Example:** `python scripts/insert.py 1 ./problem-1`


## `solved.py`

`solution` ファイルからLeetCode特有のコメントを削除します。

**Usage:** `python scripts/solved.py <step> <ext> <dest> [-any <name>]`

| 引数          | 説明                                     |
| :------------ | :--------------------------------------- |
| `<step>`      | 出力ファイル名のステップ番号 (`1`, `2`, `3`)。 |
| `<ext>`       | 出力ファイルの拡張子。                   |
| `<dest>`      | 保存先のディレクトリ。                   |
| `[-any <name>]` | (任意) 任意のファイル名を指定。          |

**Example:** `python scripts/solved.py 1 py .`


## `pr.py`

`input.txt` の内容からGitHubのプルリクエストを作成します。

**Usage:** `python scripts/pr.py <pattern>`

| 引数        | 説明                                 |
| :---------- | :----------------------------------- |
| `<pattern>` | 問題ディレクトリのglobパターン。     |

**`input.txt` のフォーマット:**
```
#ProblemName: 1. Two Sum
#ProblemLink: https://leetcode.com/problems/two-sum/
#Link:
(他の解答へのURLなど)
```

**Example:** `python scripts/pr.py 'problems/001-two-sum'`


## `create.py`

ステップファイル (`step1.ext` など) を生成します。

**Usage:** `python scripts/create.py <step> <ext> [pattern]`

| 引数        | 説明                                               |
| :---------- | :------------------------------------------------- |
| `<step>`    | ステップ番号 (`1`, `2`, `3`) または `all`。        |
| `<ext>`     | ファイルの拡張子 (例: `py`, `ts`)。                |
| `[pattern]` | (任意) 対象ディレクトリのglobパターン。            |

**Example:** `python scripts/create.py 1 py`

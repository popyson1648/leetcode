### ステップ1まで:

1. Code Nowを押下。
2. `LeetCode/Problems/問題ディレクトリ`に問題ファイルが生成される。
    - e.g. `solution.py`
3. insert.pyを実行し、ステップヘッダーを挿入。
    - `python insert.py <step> [path]`
    - e.g. `python ../scripts/insert.py 1 .`
4. 問題を解く。
5. solved.pyを実行し、解いた問題を元にStepファイルを生成。
    - `python scripts/solved.py <step> <ext> <dest> [-any <name>]`
    - e.g. `python ../scripts/solved.py 1 "py" .`

### ステップ2から:
1. 問題ファイルの解いた部分を消す。
2. 繰り返し。

### 提出:
1. input.txtを用意。
    ```
    #ProblemName: <問題名>
    #ProblemLink: <問題リンク>
    #Link: <他の解答へのURLなど>
    ```
2. pr.pyを実行。
    - `python pr.py <pattern>`
    - e.g. `python ../scripts/pr.py .`
3. PR。

#### その他

- `memo.md`: 気づきや学びやメモなどを記述するためのファイル。問題ディレクトリに含める。
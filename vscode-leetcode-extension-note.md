```
"leetcode.workspaceFolder": "/home/popyson/Document/LeetCode",
```
`leetcode.workspaceFolder`は、vscode-leetcodeが動作する上でのワーキングディレクトリの指定。


```
  "leetcode.filePath": {

    "default": {
      "folder": "Problems/${id}-${kebab-case-name}",
      "filename": "solution.${ext}"
    }
  },
  "leetcode.defaultLanguage": "python3"
}
```
folderは、`leetcode.workspaceFolder`で指定したワーキングディレクトリを基底とする問題ファイルの生成先の指定。
ここでは、`/home/popyson/Document/LeetCode/Problems/${id}-${kebab-case-name}`となる。
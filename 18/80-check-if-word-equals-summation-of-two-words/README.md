# [1880. Check if Word Equals Summation of Two Words](https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/)

You are given three strings `firstWord`, `secondWord`, and `targetWord`, each consisting of lowercase English letters `'a'` through `'j'` inclusive.

Return `true` if the summation of the numerical values of `firstWord` and `secondWord` equals the numerical value of `targetWord`, or `false` otherwise.

### Example 1:

```
Input: firstWord = "acb", secondWord = "cba", targetWord = "cdb"
Output: true
Explanation:
The numerical value of firstWord is "acb" -> "021" -> 21.
The numerical value of secondWord is "cba" -> "210" -> 210.
The numerical value of targetWord is "cdb" -> "231" -> 231.
We return true because 21 + 210 == 231.
```

### Constraints:

- `1 <= firstWord.length, secondWord.length, targetWord.length <= 8`
- `firstWord`, `secondWord`, and `targetWord` consist of lowercase English letters from `'a'` to `'j'` **inclusive**.

| Time   | Space  | Difficulty | Related Topics |
| ------ | ------ | ---------- | -------------- |
| _O(n)_ | _O(1)_ | Easy       | `String`       |

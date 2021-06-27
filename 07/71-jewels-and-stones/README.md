# [771. Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/)

You're given strings `jewels` representing the types of stones that are jewels, and `stones` representing the stones you have. Each character in `stones` is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so `"a"` is considered a different type of stone from `"A"`.

### Example 1:

```
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
```

### Constraints:

- `1 <= jewels.length, stones.length <= 50`
- `jewels` and `stones` consist of only English letters
- All the characters of `jewels` are _unique_

| Time   | Space  | Difficulty | Tag(s)                   |
| ------ | ------ | ---------- | ------------------------ |
| _O(n)_ | _O(1)_ | Easy       | `Hash Table`<br>`String` |

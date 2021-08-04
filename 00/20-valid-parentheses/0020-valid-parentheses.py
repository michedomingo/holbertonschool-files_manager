class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for i in s:
            if i in dict:                                     # 1
                stack.append(i)
            elif len(stack) == 0 or dict[stack.pop()] != i:   # 2
                return False
        return len(stack) == 0                                # 3


"""
1. if left bracket (i) key is within dict, then append it to the stack
2. else if right bracket and stack is empty w/ no left bracket match, OR, top of stack left bracket value doesn't match
3. if stack is empty return True, otherwise False if still contains unmatched left bracket
"""
# step#1       Input: s='()[]{}'
#                        ^
#                        i: '('
#               stack: ['(']
# _______________________________________
# step#2       Input: s='()[]{}'
#                         ^
#                         i: ')'
#                stack: ['(']
#
#           dict[stack.pop()] != i
#                 dict[ "(" ] == ")"
#
#                stack: []
# _______________________________________
# step#3       Input: s='()[]{}'
#
#                  i:  '('
#              stack: ['(']
#
#                  i:  ')'
#              stack: [' ']
#
#                  i:  '['
#              stack: ['[']
#
#                  i:  ']'
#              stack: [' ']
#
#                  i:  '{'
#              stack: ['{']
#
#                  i:  '}'
#              stack: [' ']
#
# return len(stack) == 0
#                            Output: True
# _______________________________________
# step#3       Input: s='([)]'
#
#                  i:  '('
#              stack: ['(']
#
#                  i:  '['
#              stack: ['([']
#
#                  i:  ')'
#              stack: ['([']
#
# elif len(stack) == 0 or dict[stack.pop()] != i:
#     return False
#
#                         dict[ "[" ] != ")"
#
#                           Output: False
# _______________________________________

assert(Solution().isValid(s="()") == True)
assert(Solution().isValid(s="()[]{}") == True)
assert(Solution().isValid(s="(]") == False)
assert(Solution().isValid(s="([)]") == False)
assert(Solution().isValid(s="{[]}") == True)


def main():
    output = Solution().isValid(s="()[]{}")
    print(f"Output: {output}")


if __name__ == '__main__':
    main()

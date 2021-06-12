class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', ]
        firstValue, secondValue, targetValue = '', '', ''

        for char in firstWord:
            firstValue += str(letters.index(char))
        for char in secondWord:
            secondValue += str(letters.index(char))
        for char in targetWord:
            targetValue += str(letters.index(char))

        sum = int(firstValue) + int(secondValue)
        if sum == int(targetValue):
            return True
        else:
            return False


def main():

    work = Solution()
    work.isSumEqual(firstWord="aaa", secondWord="a", targetWord="aaaa")


if __name__ == '__main__':
    main()

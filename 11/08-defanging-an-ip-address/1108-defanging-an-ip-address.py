class Solution:
    def defangIPaddr(self, address: str) -> str:
        replacement = "[.]"
        output = ""

        for item in address:
            if item == ".":
                output += replacement
            else:
                output += item

        return output
        # print(output)


def main():

    work = Solution()
    work.defangIPaddr("255.100.50.0")


if __name__ == '__main__':
    main()

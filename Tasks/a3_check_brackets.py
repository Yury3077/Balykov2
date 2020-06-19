from Tasks.a0_my_stack import push, pop, peek, clear


def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    clear()
    if len(brackets_row) == 0:
        return True
    else:
        for i in brackets_row:
            if i == "(":
                push(1)
            if i == ")":
                push(-1)
        summ = 0
        if peek(len(brackets_row)-1) != 1:
            return False
        else:
            for j in range(len(brackets_row)):
                summ = summ + pop()

            if summ == 0:
                return True
            else:
                return False

if __name__ == '__main__':
    print(check_brackets(""))
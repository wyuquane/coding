def ATM_machine(money: list[int], target: int, selected=[]):
    if len(money) == 0:
        if target == 0:
            print(selected)
            quit()
        else:
            return

    ATM_machine(money[1:], target - money[0], selected + [money[0]])
    ATM_machine(money[1:], target, selected)


if __name__ == '__main__':
    ATM_machine([100, 10, 20, 20, 50, 50, 50, 50, 100, 100], 400)

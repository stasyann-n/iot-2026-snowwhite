def make_new_number(number, key):
    digits = list(number)
    result = ""
    index = 0
    while digits:
        index = (index + key - 1) % len(digits)
        result += digits.pop(index)
    return result


def is_lucky(number):
    return int(number) % 3 == 0


def main():
    number = input("Введіть число N: ")
    key = int(input("Введіть ключ K (1-10): "))
    new_number = make_new_number(number, key)
    print(new_number)
    print("YES" if is_lucky(new_number) else "NO")


main()

def get_number():
    num = int(input("Enter an index in range: "))
    # int(num)
    return numbers[num]


numbers = [5, 22, 63]

# print(numbers)

# print(get_number())

n = 25
for i in range(int(n / 2) + 1):
    if (i * i) == n:
        return true

    else:
        print("no")

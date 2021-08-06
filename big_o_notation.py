# O(1)
def func1(numbers):
    print(numbers[0])


# O(log(n))
def func2(n):
    if n <= 1:
        return
    else:
        print(n)
        func2(n/2)


# O(n)
def func3(numbers):
    for num in numbers:
        print(num)


# O(n * log(n))
def func4(n):
    for i in range(int(n)):
        print(i, end=' ')
    print()


# O(n**2)
def func5(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            print(numbers[i], numbers[j])
        print()


# func1([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
# func2(10)
# func3([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# func4(10)
# func5([1, 2, 3, 4, 5])

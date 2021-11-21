def find_max(numbers):
    numbers = [10,12,50,6,70]
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    print(max)
    return  max

find_max(max)
def find_max(numbers):
    #numbers = [10,12,50,6,70]
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return  max


def find_min(numbers):
    min = numbers[0]
    for number in numbers:
        if number < min:
            min = number
    return min
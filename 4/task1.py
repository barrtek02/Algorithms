
numbers = [2, 1, 2, 3, 4, 2, 5, 1, 3, 3]

def max_element(list):
    max = list[0]
    for number in list:
        if number>max:
            max = number

    return max

def max2_element(list):
    max = list[0]
    max2 = list[1]

    for number in list:
        if number > max:
            max2 = max
            max = number
        elif number > max2:
            max2 = number

    return max, max2


def average(list):
    sum = 0
    for number in list:
        sum += number

    avg = sum/len(list)

    return avg

print(max_element(numbers)) #O(n)
print(max2_element(numbers)) #O(n)
print(average(numbers)) #O(n)
numbers = [5, 1, 2, 3, 4, 2, 1, 1, 5, 3]


def max_element_r(list):
    if len(list) == 1:
        return list[0]
    else:
        mid = len(list) // 2
        left_max = max_element_r(list[:mid])
        right_max = max_element_r(list[mid:])

        if left_max > right_max:
            return left_max
        else:
            return right_max


print(max_element_r(numbers))


def max2_element_r(list):
    if len(list) == 1:
        return list[0], None
    elif len(list) == 2:
        if list[0] > list[1]:
            return list[0], list[1]
        else:
            return list[1], list[0]
    else:
        mid = len(list) // 2
        max2, max = max2_element_r(list[:mid])
        right_second_max, right_max = max2_element_r(list[mid:])

        if max is None or max < right_max:
            max2, max = right_second_max, right_max

        for number in list[:mid]:
            if number > max:
                max2, max = max, number
            elif number > max2:
                max2 = number

        for number in list[mid:]:
            if number > max:
                max2, max = max, number
            elif number > max2:
                max2 = number

        return max, max2



print(max2_element_r(numbers))


def average_r(list):
    if len(list) == 1:
        return list[0]
    else:
        mid = len(list) // 2
        left_avg = average_r(list[:mid])
        right_avg = average_r(list[mid:])
        return ((left_avg * mid) + (right_avg * (len(list) - mid))) / len(list)


print(average_r(numbers))



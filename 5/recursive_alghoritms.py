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

def average_r(list):
    if len(list) == 1:
        return list[0]
    else:
        mid = len(list) // 2
        left_avg = average_r(list[:mid])
        right_avg = average_r(list[mid:])
        return ((left_avg * mid) + (right_avg * (len(list) - mid))) / len(list)

def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                lst[k] = left_half[i]
                i += 1
            else:
                lst[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            lst[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            lst[k] = right_half[j]
            j += 1
            k += 1
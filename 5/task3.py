def merge_sort(list):
    if len(list) > 1:
        mid = len(list) // 2
        left_half = list[:mid]
        right_half = list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                list[k] = left_half[i]
                i += 1
            else:
                list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            list[k] = right_half[j]
            j += 1
            k += 1
    return list



list1 = [1, 3, 2, 4, 5, 6]
print(list1)
print(merge_sort(list1))
print()
list2 = [6, 5, 4, 3, 2, 6]
print(list2)
print(merge_sort(list2))
# Algorytm ten działa następująco:
#
# Jeśli lista ma więcej niż jeden element, dzielimy ją na dwie połowy i rekurencyjnie sortujemy każdą z nich.
#
# Następnie łączymy dwie posortowane podlisty w jedną, przechodząc przez nie element po elemencie i wybierając zawsze mniejszy z dwóch aktualnie porównywanych elementów.
#
# Jeśli jedna z podlist zostanie już przetworzona w całości, to przepisujemy pozostałe elementy z drugiej podlisty.
#
# Na koniec, posortowana lista jest zapisywana na miejscu listy oryginalnej.
#
# Złożoność czasowa algorytmu sortowania przez scalanie wynosi O(n log n), gdzie n to liczba elementów w liście. Każdy poziom rekurencji dzieli listę na połowę, a następnie łączymy posortowane podlisty, co wymaga n porównań, co w sumie daje O(n log n).

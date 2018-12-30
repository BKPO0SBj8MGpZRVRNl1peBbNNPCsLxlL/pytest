def my_sort(numbers):
    even = [x for x in numbers if x % 2 == 0]
    odd = [x for x in numbers if x % 2 != 0]
    return sorted(odd) + sorted(even)

print(my_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) 
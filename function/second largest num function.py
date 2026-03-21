def second_largest(lst):
    largest = lst[0]
    second = lst[0]

    for num in lst:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second

print(second_largest([10,20,30,40]))

. output 30
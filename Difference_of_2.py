# The objective is to return all pairs of integers from a given collection of integers that have a difference of 2.

# The result should be sorted in ascending order.

# The input will consist of unique values. The order of the integers in the input collection should not matter.
def twos_difference(lst): 
    lst.sort()
    i = 0
    result = []
    while i < len(lst)-1:
        if lst[i]+2 == lst[i+1]:
            result.append((lst[i], lst[i+1]))
        if (i+2<len(lst)) and (lst[i]+2 == lst[i+2]):
            result.append((lst[i], lst[i+2]))
        i += 1
    return result

# почти работает))
def twos_difference2(lst): 
    lst.sort()
    return list(filter(None, map(lambda el1, el2: (el1, el2) if el1+2==el2 else None, lst, lst[1::])))


# лучшее решение
def twos_difference3(a):
    s = set(a)
    return sorted((x, x + 2) for x in a if x + 2 in s)

print(twos_difference([1, 3, 4, 6]))
print(twos_difference2([1, 3, 4, 6]))
# test.assert_equals(twos_difference([1, 2, 3, 4]), [(1, 3), (2, 4)])
# test.assert_equals(twos_difference([1, 3, 4, 6]), [(1, 3), (4, 6)])
# test.assert_equals(twos_difference([0, 3, 1, 4]), [(1, 3)])
# test.assert_equals(twos_difference([4, 1, 2, 3]), [(1, 3), (2, 4)])
# test.assert_equals(twos_difference([6, 3, 4, 1, 5]), [(1, 3), (3, 5), (4, 6)])
# test.assert_equals(twos_difference([3, 1, 6, 4]), [(1, 3), (4, 6)])
# test.assert_equals(twos_difference([1, 3, 5, 6, 8, 10, 15, 32, 12, 14, 56]), [(1, 3), (3, 5), (6, 8), (8, 10), (10, 12), (12, 14)])
# test.assert_equals(twos_difference([1, 4, 7, 10]), [])
# test.assert_equals(twos_difference([]), [])
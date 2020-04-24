"""
This code reads:
    length of sorted array
    sorted array
    number of queries
    queries1
    queries2
       .
       .
       .
And prints if queries number found
Algorithm uses binary search to perfom search (what a suprise)

Sample input:
    7
    1 2 6 7 9 9 10
    3
    4
    5
    6

Sample output:
    NIE
    NIE
    TAK

*NIE <- NO
*TAK <- YES"""

#   Returns idx of element, or None if not found
def binary_search(sorted_array_asc: [int,], value: int):
    start = 0
    end = len(sorted_array_asc) - 1

    while start <= end:
        middle = (start + end) // 2 
        if sorted_array_asc[middle] == value:
            return middle
        elif sorted_array_asc[middle] < value:
            start = middle + 1
        else:
            end = middle - 1

    return None 


n_of_numbers = int(input())
array_input = input().split() 
sorted_arr = [None] * len(array_input)

for idx, elem in enumerate(array_input):
    sorted_arr[idx] = int(elem)

n_of_queries = int(input())

while n_of_queries:
    query = int(input())
    if binary_search(sorted_arr, query) is None:
        print("NIE")
    else:
        print("TAK")
    n_of_queries -= 1


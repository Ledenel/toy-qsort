import random

def pick_pivot_index(array):
    return 0

def qsort(array):
    if len(array) >= 1:
        pivot_index = pick_pivot_index(array)
        pivot = array[pivot_index]
        remains = [x for i,x in enumerate(array) if i != pivot_index]
        less_equal_than_pivot = [x for x in remains if x <= pivot]
        greater_than_pivot = [x for x in remains if x > pivot]
        left_sorted = qsort(less_equal_than_pivot)
        right_sorted = qsort(greater_than_pivot)
        return left_sorted + [pivot] + right_sorted
    else:
        return array

if __name__ == "__main__":
    unsorted = ["1","2","3","4","5","6","7","8","9"]
    random.seed()
    random.shuffle(unsorted)
    print("unsorted: {0}".format(unsorted))
    print("sorted: {0}".format(qsort(unsorted)))
    
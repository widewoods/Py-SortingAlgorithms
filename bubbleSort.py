from random import shuffle


def bubble_sort(array):
    output = array
    length = len(array)
    for i in range(length-1):
        for j in range(0, length-1-i):
            if output[j] > output[j+1]:
                output[j], output[j+1] = output[j+1], output[j]

    return output


elem_count = 100
arr = [x for x in range(1, elem_count + 1)]
shuffle(arr)

print("Before sorting:", arr)
print("After sorting:", bubble_sort(arr))



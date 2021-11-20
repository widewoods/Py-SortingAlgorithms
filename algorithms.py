from random import sample
from math import floor


class Algorithm:
    def __init__(self, name):
        self.array = sample(range(512), 512)
        self.name = name

    def update_display(self, swap1=None, swap2=None):
        import visualizer
        visualizer.update(self, swap1, swap2)

    def run(self):
        self.algorithm()
        return self.array


class BubbleSort(Algorithm):
    def __init__(self):
        super().__init__("BubbleSort")

    def algorithm(self):
        n = len(self.array)
        while True:
            new_n = 0
            for i in range(1, n):
                if self.array[i-1] > self.array[i]:
                    self.array[i-1], self.array[i] = self.array[i], self.array[i-1]
                    new_n = i
            n = new_n
            if n <= 1:
                break
            self.update_display(self.array[i-1], self.array[i])


class QuickSort(Algorithm):
    def __init__(self):
        super().__init__("QuickSort")

    def algorithm(self, array=[], lo=0, hi=0):
        if array == []:
            array = self.array
            hi = len(array) - 1

        if (lo >= 0) & (hi >= 0) & (lo < hi):
            p = self.partition(array, lo, hi)

            self.algorithm(array, lo, p-1)
            self.algorithm(array, p+1, hi)

    def partition(self, array, lo, hi):
        pivot = self.array[hi]

        i = lo - 1
        for j in range(lo, hi+1):
            if array[j] <= pivot:
                i = i+1
                if i < j:
                    array[i], array[j] = array[j], array[i]
                    self.update_display(array[i], array[j])

        return i


class MergeSort(Algorithm):
    def __init__(self):
        super().__init__("MergeSort")

    def algorithm(self, array = []):
        if array == []:
            array = self.array

        if len(array) <= 1:
            return array

        left = []
        right = []

        for i, x in enumerate(array):
            if i < len(array)/2:
                left.append(x)
            else:
                right.append(x)

        left = self.algorithm(left)
        right = self.algorithm(right)

        return self.merge(left, right)

    def merge(self, left, right):
        result = []

        while (left != []) and (right != []):
            first_left = left[0]
            first_right = right[0]
            if first_left <= first_right:
                result.append(first_left)
                left.remove(first_left)
            else:
                result.append(first_right)
                right.remove(first_right)
            self.update_display()

        while left:
            result.append(left[0])
            left.remove(left[0])
        while right:
            result.append(right[0])
            right.remove(right[0])

        self.array = result
        self.update_display()

        return result


class HeapSort(Algorithm):
    def __init__(self):
        super().__init__("HeapSort")

    def algorithm(self):
        count = len(self.array)

        self.heapify()

        end = count - 1
        while end > 0:
            self.array[0], self.array[end] = self.array[end], self.array[0]
            self.update_display(self.array[0], self.array[end])
            end = end - 1
            self.sift_down(0, end)

    def heapify(self):
        count = len(self.array)
        start = floor((count - 1)/2)  # parent index of last element

        while start >= 0:
            self.sift_down(start, count-1)
            start = start - 1

    def sift_down(self, start, end):
        root = start

        while 2 * root + 1 <= end:
            child = 2 * root + 1
            swap = root

            if self.array[child] > self.array[swap]:
                swap = child

            if (child + 1 <= end) and (self.array[swap] < self.array[child + 1]):
                swap = child + 1

            if swap == root:
                return

            else:
                self.array[swap], self.array[root] = self.array[root], self.array[swap]
                self.update_display(self.array[swap], self.array[root])
                root = swap


class InsertionSort(Algorithm):
    def __init__(self):
        super().__init__("InsertionSort")

    def algorithm(self):
        i = 1
        while i < len(self.array):
            j = i
            while (j > 0) and (self.array[j-1] > self.array[j]):
                self.array[j - 1], self.array[j] = self.array[j], self.array[j - 1]
                self.update_display(self.array[j - 1], self.array[j])
                j = j - 1

            i = i + 1


class LSDRadixSort(Algorithm):
    def __init__(self):
        super().__init__("LSDRadixSort")

    def algorithm(self):
        max1 = max(self.array)
        exp = 1
        while max1 / exp > 0:
            self.counting_sort(exp)
            exp *= 10

    def counting_sort(self, exp):
        n = len(self.array)

        output = [0] * n
        count = [0] * 10

        for i in self.array:
            index = (i // exp) % 10
            count[index] += 1

        for i in range(1, 10):
            count[i] += count[i-1]

        i = n - 1
        while i >= 0:
            index = (self.array[i] // exp) % 10
            output[count[index] - 1] = self.array[i]
            count[index] -= 1
            i -= 1

        for j in range(n):
            self.array[j] = output[j]
            self.update_display()

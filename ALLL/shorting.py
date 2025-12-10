# Insertion Sort
def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

# Selection Sort
def selection_sort(a):
    for i in range(len(a)):
        min_i = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_i]:
                min_i = j
        a[i], a[min_i] = a[min_i], a[i]
    return a

# Bubble Sort
def bubble_sort(a):
    for i in range(len(a)):
        for j in range(0, len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

# Merge Sort
def merge_sort(a):
    if len(a) <= 1: return a
    mid = len(a)//2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left, right)

def merge(L, R):
    res = []
    i = j = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]: res.append(L[i]); i+=1
        else: res.append(R[j]); j+=1
    return res + L[i:] + R[j:]

# Quick Sort
def quick_sort(a):
    if len(a) <= 1: return a
    pivot = a[len(a)//2]
    left  = [x for x in a if x < pivot]
    mid   = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)


# ---------------- Example ----------------
arr = [64, 25, 12, 22, 11]

print("Insertion Sort :", insertion_sort(arr.copy()))
print("Selection Sort :", selection_sort(arr.copy()))
print("Bubble Sort    :", bubble_sort(arr.copy()))
print("Merge Sort     :", merge_sort(arr.copy()))
print("Quick Sort     :", quick_sort(arr.copy()))

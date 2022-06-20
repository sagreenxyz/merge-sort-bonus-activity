def selection_sort(lst): 
    for i in range(0, len(lst) - 1):
        min = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min]:
                # change the minimum number's position if a smaller number is identified
                min = j
        
        # after each pass through the items in the list, if the current minimum number is not equal 
        # to the minimum number (min), then exchange positions and swap numbers
        if min != i: 
            lst[i], lst[min] = lst[min], lst[i]

    return lst


sample_list = [5, 8, 1, 22, 18, 6, 2]
print(f"Unsorted list: {sample_list}")
selection_sort(sample_list)
print(f"Sorted list: {sample_list}")
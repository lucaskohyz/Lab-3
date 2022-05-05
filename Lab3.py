print("Lab 3 - Software Unit Testing with PyTest")


SORT_ASCENDING = 0
SORT_DESCENDING = 1


def bubble_sort(arr, sorting_order):

    # Copy input list to results list
    arr_result = arr.copy()
    if (all([isinstance(item, int) for item in arr])==True):
    # Get number of elements in the list
        n = len(arr_result)

        if n == 10:
            # Traverse through all array elements
            for i in range(n - 1):
                # range(n) also work but outer loop will
                # repeat one time more than needed.

                # Last i elements are already in place
                for j in range(0, n - i - 1):

                    if sorting_order == SORT_ASCENDING:
                        if arr_result[j] > arr_result[j + 1]:
                            arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]


                    elif sorting_order == SORT_DESCENDING:
                        if arr_result[j] < arr_result[j + 1]:
                            arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

                    else:
                        # Return an empty array
                        arr_result = []
        if n < 10:
            arr_result = 2
        if n > 10:
            arr_result = 1
        elif n==0:
            arr_result = 0
    elif (all([isinstance(item, int) for item in arr])==False):
        arr_result = 3



    return arr_result


def main():
    # Driver code to test above
    arr = [64, 34, 25, 12, 22, 11, 90, 30,10]

    choice = input("Would you like to have it in ascending or descending order(1 for ascending/2 for descending): ")
    if(choice=='1'):
        result = bubble_sort(arr, SORT_ASCENDING)
        print("\nSorted array in ascending order: ")
        print(result)
    elif(choice=='2'):
        print("Sorted array in descending order: ")
        result = bubble_sort(arr, SORT_DESCENDING)
        print(result)


if __name__ == "__main__":
    main()



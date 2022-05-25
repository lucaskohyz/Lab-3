import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 10,20,30]
    test_arr = [10,11, 12, 20,22, 25, 30,34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)


def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 10, 20, 30]
    test_arr = [90, 64, 34,30, 25, 22,20, 12, 11, 10]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90,10,20,30]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])
def checkifnumbermorethan_10():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90,10,20,30,40 ]
    result = Lab3.bubble.sort(input_arr,4)
    assert (result ==1)
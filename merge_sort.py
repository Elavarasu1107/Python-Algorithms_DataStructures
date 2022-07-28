import logging

logging.basicConfig(filename='AlgorithmLog.log', encoding='utf-8', level=logging.DEBUG)


def merge_sort(number_list):
    """
    This function merge sort the element in the list
    :param number_list: List parameter passed from main method
    :return: None
    """
    try:
        middle = len(number_list) // 2
        left = number_list[:middle]
        right = number_list[middle:]
        if len(left) > 1:
            merge_sort(left)
        if len(right) > 1:
            merge_sort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                number_list[k] = left[i]
                i += 1
            else:
                number_list[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            number_list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            number_list[k] = right[j]
            j += 1
            k += 1
    except Exception as ex:
        logging.exception("Exception : ", ex)


if __name__ == '__main__':
    number_list = [10, 5, 70, 50, 100, 80, 45, 85, 11]
    print("Before sorting: ", number_list)
    merge_sort(number_list)
    print("After sorting: ", number_list)


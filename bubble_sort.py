import logging

logging.basicConfig(filename='AlgorithmLog.log', encoding='utf-8', level=logging.DEBUG)


def bubble_sort():
    """
    This function bubble sort the element in the list
    :return: None
    """
    try:
        number_list = [50, 45, 76, 100, 10, 18, 140, 90, 60]
        print("Before sorting: ", number_list)
        i = 0
        while i < len(number_list) - 1:
            j = 0
            while j < len(number_list) - (i + 1):
                if number_list[j] > number_list[j + 1]:
                    temp = number_list[j + 1]
                    number_list[j + 1] = number_list[j]
                    number_list[j] = temp
                j += 1
            i += 1
        print("After sorting: ", number_list)
    except Exception as ex:
        logging.exception("Exception: ", ex)


if __name__ == '__main__':
    bubble_sort()

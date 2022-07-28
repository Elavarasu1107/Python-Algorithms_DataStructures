import logging

logging.basicConfig(filename='AlgorithmLog.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


def insertion_sort():
    """
    This function insertion sort the element in the list
    :return: None
    """
    try:
        number_list = [1, 5, 9, 3, 4, 2, 6, 20, 11]
        print("Before sorting: ", number_list)
        for i in range(0, len(number_list)):
            temp = number_list[i]
            j = i - 1
            while j >= 0 and number_list[j] >= temp:
                number_list[j + 1] = number_list[j]
                j -= 1
            number_list[j + 1] = temp
        print("After sorting: ", number_list)
    except Exception as ex:
        logging.exception("Exception: ", ex)


if __name__ == '__main__':
    insertion_sort()

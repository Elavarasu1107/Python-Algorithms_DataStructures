import logging

logging.basicConfig(filename='AlgorithmLog.log', encoding='utf-8', level=logging.DEBUG)


def compare(a, b):
    """
    This function compares to parameters and returns -1, 0, 1
    :param a: can be an integer or string
    :param b: can be an integer or string
    :return: integer value
    """
    try:
        result = (a > b) - (a < b)
        return result
    except Exception as ex:
        logging.exception("Exception : ", ex)


def string_search(string_list, left, right, user_input):
    """
    This function searches string in the list
    :param string_list: contains list of elements
    :param left: integer value
    :param right: integer value
    :param user_input: input value passed by user
    :return: integer value
    """
    try:
        while left <= right:
            middle = left + (right - left) // 2
            result = compare(user_input, string_list[middle])
            if result == 0:
                return middle
            if result > 0:
                left = middle + 1
            else:
                right = middle - 1
        return -1
    except Exception as ex:
        logging.exception("Exception : ", ex)


def binary_search():
    """
    This function binary search the element in the list
    :return: None
    """
    try:
        string_list = ["python", "object", "language", "interpreter", "compiler"]
        string_list.sort()
        print("Sorted list:", string_list)
        user_input = input("Enter a word to search: ")
        left = 0
        right = len(string_list) - 1
        output = string_search(string_list, left, right, user_input)
        if output == -1:
            print("Word not found in the list")
        else:
            print(user_input, " is at index ", output)
    except Exception as ex:
        logging.exception("Exception : ", ex)


if __name__ == '__main__':
    binary_search()

import logging

logging.basicConfig(filename='AlgorithmLog.log', encoding='utf-8', level=logging.DEBUG)


def anagram(string_one, string_two):
    """
    This function checks two input strings whether its anagram
    :param string_one: string parameter passed from main method
    :param string_two: string parameter passed from main method
    :return: None
    """
    try:
        to_char1 = list(string_one.lower())
        to_char2 = list(string_two.lower())
        to_char1.sort()
        to_char2.sort()
        if to_char1 == to_char2:
            print("Both strings are anagrams")
        else:
            print("Both strings are not anagrams")
    except Exception as ex:
        logging.exception(ex)


if __name__ == '__main__':
    string_one = input("Enter first word: ")
    string_two = input("Enter second word: ")
    anagram(string_one, string_two)

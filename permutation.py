import logging

logging.basicConfig(filename='AlgorithmLog.log', encoding='utf-8', level=logging.DEBUG)


def permutation(input_string, i):
    """
    This function find possible combination of elements
    :param input_string: string value
    :param i: integer value
    :return: None
    """
    try:
        if i == len(input_string):
            print("".join(input_string), end=" ")
        for j in range(i, len(input_string)):
            words = []
            for k in input_string:
                words.append(k)
            words[i], words[j] = words[j], words[i]
            permutation(words, i + 1)
    except Exception as ex:
        logging.exception("Exception : ", ex)


if __name__ == '__main__':
    input_string = input("Enter a string: ")
    permutation(input_string, 0)
    print(input_string)

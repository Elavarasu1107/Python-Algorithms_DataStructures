import logging

logging.basicConfig(filename='AlgorithmLog.log', encoding='utf-8', level=logging.DEBUG)


def brackets(open_bracket, close_bracket):
    """
    This function checks brackets and return boolean
    :param open_bracket: (, [, {
    :param close_bracket: ), ], }
    :return: boolean
    """
    try:
        if open_bracket == "[" and close_bracket == "]":
            return True
        if open_bracket == "(" and close_bracket == ")":
            return True
        if open_bracket == "{" and close_bracket == "}":
            return True
        return False
    except Exception as ex:
        logging.exception("Exception: ", ex)


def balanced_parentheses(input_string):
    """
    This function checks whether parentheses are balanced
    :param input_string: string value
    :return: None
    """
    try:
        bracket_list = []
        for i in range(0, len(input_string)):
            if input_string[i] == "[" or input_string[i] == "(" or input_string[i] == "{":
                bracket_list.append(input_string[i])
            elif input_string[i] == "]" or input_string[i] == ")" or input_string[i] == "}":
                if brackets(bracket_list[len(bracket_list) - 1], input_string[i]):
                    bracket_list.pop()
        if len(bracket_list) == 0:
            print("String has balanced parentheses")
        else:
            print("String has unbalanced parentheses")
    except Exception as ex:
        logging.exception("Exception: ", ex)


if __name__ == '__main__':
    user_input = "(5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3)"
    balanced_parentheses(user_input)

"""A snippet that validates a variable type and if empty.

Usage: python -B validate_input_snip.py
"""
TEST_TYPES = [
    str,
    int,
    float,
    complex,
    list,
    tuple,
    dict,
    set,
    frozenset,
    bool,
    bytes,
    bytearray,
    memoryview,
    None
]

TEST_EXAMPLES = [
    'John',  # 0: string
    '',  # 1: empty string
    '  ',  # 2: empty string
    '\r',  # 3: carriage return
    '\r\n',  # 4: carriage return and line feed
    5,  # 5: int
    5.5,  # 6: float
    5j,  # 7: complex
    ['John', 5, True],  # 8: list
    ('John', 5, True),  # 9: tuple
    {'name': 'John', 'years': 5, 'active': True},  # 10: dict
    {'John', 5, True},                             # 11: set
    frozenset({'John', 5, True}),                  # 12: frozenset
    False,                                         # 13: bool
    int(False),                                    # 14: Equals 0
    True,                                          # 15: bool
    int(True),                                     # 16: Equals 1
    b'John',                                       # 17: bytes
    bytearray(5),                                  # 18: bytearray
    memoryview(bytes(5)),                          # 19: memoryview
    None                                           # 20: None
]


def __get_var_name(obj: object) -> str:
    """Get the name of a variable.

    :param any obj: The variable object.
    :return str: The name of the variable.
    """
    for _name, _value in globals().items():
        if _value is obj:
            return _name
    return 'input_var'


def __is_expected_type(obj_to_check: object, expected_type: type | None) -> bool:
    """Check if an object is the correct type,
    accounting for NoneTypes before Python 3.10.

    :param object obj_to_check: The object to check.
    :param type | None expected_type: The expected type of the object.
    :return bool: If the object is of the expected type.
    """
    if expected_type is None:
        return obj_to_check is None
    return isinstance(obj_to_check, expected_type)


def __is_empty(obj_to_check: object) -> bool:
    """Check if an object is empty, whitespace, or contains only None values.

    :param object obj_to_check: The object to check.
    :return bool: If the object is empty, whitespace, or contains only None values.
    """
    if isinstance(obj_to_check, str):
        return obj_to_check.strip() == ''

    if isinstance(obj_to_check, (list, tuple, set, frozenset)):
        return not obj_to_check or all(item is None for item in obj_to_check)

    if isinstance(obj_to_check, dict):
        return not obj_to_check or all(value is None for value in obj_to_check.values())

    return False


def validate_input(obj_to_check: object,
                   expected_type: type | None,
                   allow_empty: bool = False) -> tuple:
    """Check if an input is the correct type and (optionally) not empty.

    :param any obj_to_check: The input to check.
    :param type expected_type: The expected type of the input.
    :param bool allow_empty: Allow empty inputs, defaults to False
    :raises TypeError: If the input is the wrong type.
    :raises ValueError: If the input is empty and it should not be.
    :return tuple: 0 and None if valid, else 1 and an error message.
    """
    try:
        # Get the name of the input, if possible.
        _var_name = __get_var_name(obj_to_check)

        # Check if the input is the right type
        if not __is_expected_type(obj_to_check, expected_type):
            raise TypeError(f"'{_var_name}' is not {expected_type}.")

        # Check if the input is empty, whitespace, or contains only None values
        if not allow_empty and __is_empty(obj_to_check):
            raise ValueError(
                f"'{_var_name}' cannot be empty, whitespace, or contain only None values."
            )

        return 0, None
    except (TypeError, ValueError) as e:
        return 1, f"Error: {str(e)}"


if __name__ == '__main__':
    for t in TEST_TYPES:
        # result = validate_input(TEST_EXAMPLES[12], t)
        result = validate_input([None], t)
        print(t, result)

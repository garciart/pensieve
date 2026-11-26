"""A snippet that displays different Python variable types.

Note: types module requires Python 3.10+

Usage: python -B python_types_snip.py
"""
from types import NoneType

python_types = [
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
    NoneType
]

python_type_examples = [
    'John',                                        # string
    '',                                            # empty string
    '  ',                                          # empty string
    '\r',                                          # carriage return
    '\r\n',                                        # carriage return and line feed
    5,                                             # int
    5.5,                                           # float
    5j,                                            # complex
    ['John', 5, True],                             # list
    ('John', 5, True),                             # tuple
    {'name': 'John', 'years': 5, 'active': True},  # dict
    {'John', 5, True},                             # set
    frozenset({'John', 5, True}),                  # frozenset
    False,                                         # bool
    int(False),                                    # Equals 0
    True,                                          # bool
    int(True),                                     # Equals 1
    b'John',                                       # bytes
    bytearray(5),                                  # bytearray
    memoryview(bytes(5)),                          # memoryview
    None                                           # None
]

for e in python_type_examples:
    print(f"{type(e)}: {e}")

for t in python_types:
    print(isinstance(None, t))

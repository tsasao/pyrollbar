from rollbar.lib import binary_type, string_types


from collections.abc import Mapping, Sequence, Set


CIRCULAR = -1
DEFAULT = 0
MAPPING = 1
TUPLE = 2
NAMEDTUPLE = 3
LIST = 4
SET = 5
STRING = 6


def get_type(obj):
    if isinstance(obj, (string_types, binary_type)):
        return STRING

    if isinstance(obj, Mapping):
        return MAPPING

    if isinstance(obj, tuple):
        if hasattr(obj, "_fields"):
            return NAMEDTUPLE

        return TUPLE

    if isinstance(obj, set):
        return SET

    if isinstance(obj, Sequence):
        return LIST

    return DEFAULT


__all__ = [
    "CIRCULAR",
    "DEFAULT",
    "MAPPING",
    "TUPLE",
    "NAMEDTUPLE",
    "LIST",
    "SET",
    "STRING",
    "get_type",
]

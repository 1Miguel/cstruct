"""
__description__
"""

import struct

from enum import IntEnum
from typing import Tuple, Dict, Any, Literal, TypeVar, TypedDict
from typing_extensions import Self


_FIELDS = "__cstruct_fields__"


u8 = TypeVar("u8")
i8 = TypeVar("i8")
u16 = TypeVar("u16")
i16 = TypeVar("i16")
u32 = TypeVar("u32")
i32 = TypeVar("i32")
u64 = TypeVar("u64")
i64 = TypeVar("i64")


_TYPE_MAP = {
    u8: "b"
}


def is_cstruct(obj_or_type) -> bool:
    """
    __doc__
    """
    return hasattr(obj_or_type, _FIELDS)


class _Missing:
    """Missing type."""


class _Field(TypedDict):
    """C struct field metadata."""
    name: str
    type: str
    enum: IntEnum
    default: Any
    len: int


class _CstructMeta(type):

    def __new__(
        mcs,
        name: str,
        bases: Tuple[type, ...],
        namespace: Dict[str, Any],
        endianness: Literal["little", "big"],
    ) -> "_CstructMeta":
        """"""
        annon = mcs.__annotations__
        inst = type.__new__(mcs, name, bases, namespace)
        fields = {}

        if annon:
            for i in annon:
                pass

        return inst


class _Cstruct(endianness="little", metaclass=_CstructMeta):

    def from_buffer(self) -> Self:
        """
        __dest__
        """
        return _Cstruct()

    def __bytest__(self) -> bytes:
        """
        __dest__
        """
        pass


class Cstruct:
    pass

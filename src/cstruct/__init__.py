"""
__description__
"""

import struct

from enum import IntEnum
from typing import Tuple, Dict, Any, Literal, TypeVar, TypedDict
from typing_extensions import Self

__all__ = (
    "Cstruct",
    "u8",
)

_CSTRUCT_FIELDS = "__cstruct_fields__"
_CSTRUCT_DESC = "__cstruct_desc__"


u8 = TypeVar("u8", int, float)
i8 = TypeVar("i8")
u16 = TypeVar("u16")
i16 = TypeVar("i16")
u32 = TypeVar("u32")
i32 = TypeVar("i32")
u64 = TypeVar("u64")
i64 = TypeVar("i64")


_TYPE_MAP = {
    u8: "b",
    i8: "q",
}


def is_cstruct(obj_or_type) -> bool:
    """
    __doc__
    """
    return hasattr(obj_or_type, _CSTRUCT_FIELDS)


class _Field(TypedDict):
    """C struct field metadata."""
    name: str
    type: str
    enum: IntEnum
    default: Any
    len: int
    is_array: bool
    struct: str


class Array:
    """"""

    def __init__(self, length: int = 0) -> None:
        self.length = length


class _CstructMeta(type):

    def __new__(
        mcs,
        name: str,
        bases: Tuple[type, ...],
        namespace: Dict[str, Any],
        endianness: Literal["little", "big"] = "little",
    ) -> "_CstructMeta":
        """"""
        inst = type.__new__(mcs, name, bases, namespace)
        annon = inst.__annotations__
        fields = {}
        desc = ""

        if annon:
            for i, (n, t) in enumerate(annon.items()):
                if n in fields:
                    raise ValueError(f"field '{n}' already exists")

                val = getattr(inst, n, None)
                fields = {"name": n, "type": t, "default": val}
                meta = getattr(t, "__metadata__", None)

                if meta and isinstance(meta[0], Array):
                    fields["length"] = meta[0].length
                    fields["is_array"] = True
                    fields["type"] = t.__origin__
                elif meta is not None:
                    raise TypeError(f"invalid type metadata '{meta}'")

                if isinstance(fields["type"], IntEnum):
                    fields["enum"] = fields["type"]
                    # packed the enum to its appropriate size
                    
                # this is used to compile to struct
                # if the array size if unknown, add a marker
                # this will be filled up later by the array size

        setattr(inst, _CSTRUCT_FIELDS, fields)
        setattr(inst, _CSTRUCT_DESC, desc)

        return inst

class Cstruct(metaclass=_CstructMeta, endianness="little"):

    @classmethod
    def from_buffer(cls, data: bytes) -> Self:
        """
        __dest__
        """
        return Cstruct()

    def __bytes__(self) -> bytes:
        """
        __dest__
        """
        pass

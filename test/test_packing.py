import unittest

from typing import Annotated
from cstruct import Cstruct, Array, u8

class TestPacking(unittest.TestCase):

    def test_pack_unsigned(self) -> None:
        class TestStruct(Cstruct):
            my_u8: Annotated[u8, Array(4)]
        print(TestStruct.__annotations__)

    def test_pack_signed(self) -> None:
        class TestStruct(Cstruct):
            my_i8: u8

if __name__ == "__main__":
    unittest.main()

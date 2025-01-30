import unittest

import cstruct

class TestPacking(unittest.TestCase):


    def test_pack_unsigned(self) -> None:
        class TestStruct(cstruct.Cstruct):
            pass


if __name__ == "__main__":
    unittest.main()

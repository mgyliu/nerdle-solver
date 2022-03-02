import unittest
from simulate import getHints


class TestSimulate(unittest.TestCase):
    def test_get_hints(self):
        # 20220227
        self.assertEqual(getHints(answer="3*42=126", guess="1+8*6=49"), "PBBPPPPB")
        self.assertEqual(getHints(answer="3*42=126", guess="42=6*1*7"), "PPPPPGBB")
        self.assertEqual(getHints(answer="3*42=126", guess="0*6421=0"), "BGPPPGPB")
        self.assertEqual(getHints(answer="3*42=126", guess="3*42=126"), "GGGGGGGG")

        # 20220222
        self.assertEqual(getHints(answer="1-8+16=9", guess="5+6*4=29"), "BPPBBPBG")
        self.assertEqual(getHints(answer="1-8+16=9", guess="11=6/3+9"), "GPPPBBPG")
        self.assertEqual(getHints(answer="1-8+16=9", guess="1-8+16=9"), "GGGGGGGG")


if __name__ == "__main__":
    unittest.main()

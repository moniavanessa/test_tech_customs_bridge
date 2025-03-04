from unittest import TestCase

from main import get_random_list, sort_list, dpmr


class Test(TestCase):

    def test_get_random_list(self):
        list_randoms = get_random_list(10, 1, 15)
        self.assertEqual(len(list_randoms), 10)
        print(list_randoms)

    def test_sort_list(self):
        list_randoms = [8, 11, 7, 4, 7, 10, 11, 2, 11, 9]

        sorted_list = sort_list(list_randoms)
        self.assertEqual(sorted_list, [2, 4, 7, 7, 8, 9, 10, 11, 11, 11])


    def test_dpmr(self):
        sorted_list = [2, 4, 5, 7, 8, 9, 10, 11, 11, 11]
        new_elem = 6

        index = dpmr(sorted_list, new_elem)

        print("final index ", index)

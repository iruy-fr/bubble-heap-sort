import unittest

from codigo import bubble_sort, heap_sort


class TestAlgoritmosOrdenacao(unittest.TestCase):
    def conferir_ordenacao(self, algoritmo):
        casos = [
            [],
            [1],
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1],
            [3, 1, 4, 1, 5, 9, 2],
            [10, -1, 0, 10, 3, -1],
        ]

        for caso in casos:
            with self.subTest(algoritmo=algoritmo.__name__, caso=caso):
                entrada = caso.copy()
                algoritmo(entrada)
                self.assertEqual(entrada, sorted(caso))

    def test_bubble_sort(self):
        self.conferir_ordenacao(bubble_sort)

    def test_heap_sort(self):
        self.conferir_ordenacao(heap_sort)


if __name__ == "__main__":
    unittest.main()

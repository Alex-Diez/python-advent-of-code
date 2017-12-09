import unittest


def number_of_redistribution(banks):
    history = set()
    size = len(banks)
    _copy = list(banks)
    while tuple(_copy) not in history:
        history.add(tuple(_copy))
        index, value = most_blocks_bank(_copy)
        _copy[index] = 0
        for i in range(value):
            j = (i + index + 1) % size
            _copy[j] += 1

    return len(history)


def most_blocks_bank(banks):
    max_index = 0
    max_value = banks[max_index]
    for index in range(len(banks)):
        if max_value < banks[index]:
            max_value = banks[index]
            max_index = index
    return max_index, max_value


PUZZLE_INPUT = [4, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3, 14, 5, 12, 34, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3, 14, 5, 12, 3]


class MemoryBankRedistributionTest(unittest.TestCase):
    def testAllZeros(self):
        self.assertEqual(1, number_of_redistribution([0, 0, 0, 0]))

    def testSingleOne(self):
        self.assertEqual(4, number_of_redistribution([0, 0, 1, 0]))

    def testTaskInput(self):
        self.assertEqual(5, number_of_redistribution([0, 2, 7, 0]))

    def testPrintSolution(self):
        print(number_of_redistribution(PUZZLE_INPUT))

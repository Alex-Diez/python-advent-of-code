import unittest


def steps_from(index):
    if index == 1:
        return 0
    max_on_level = 1
    level = 0
    while index > max_on_level:
        level += 1
        max_on_level += level * 8

    axis = [Cell(2), Cell(4), Cell(6), Cell(8)]
    for _ in range(level - 1):
        axis[0].increment()
        axis[1].increment()
        axis[2].increment()
        axis[3].increment()
    distance = min(map(lambda e: abs(e.current() - index), axis))
    return level + distance


class Cell(object):
    def __init__(self, current):
        self._current = current
        self._delta = current - 1

    def increment(self):
        _next = self._current + self._delta + 8
        self._delta += 8
        self._current = _next

    def current(self):
        return self._current





class MemoryAccessTest(unittest.TestCase):
    def testReadFromCellOne(self):
        self.assertEqual(0, steps_from(1))

    def testReadFromCellNine(self):
        self.assertEqual(2, steps_from(9))

    def testTaskInput(self):
        self.assertEqual(0, steps_from(1))
        self.assertEqual(3, steps_from(12))
        self.assertEqual(2, steps_from(23))
        self.assertEqual(31, steps_from(1024))

    def testPrintSolution(self):
        print(steps_from(361527))



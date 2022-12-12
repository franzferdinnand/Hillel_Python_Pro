from decimal import *


class frange:
    def __init__(self, *args):

        if len(args) == 3:
            self._start, self._stop, self._step = args
        elif len(args) == 2:
            self._start, self._stop = args
            self._step = 1
        elif len(args) == 1:
            self._stop, = args
            self._start = 0
            self._step = 1

    def __iter__(self):
        return self

    def __next__(self):
        if (self._start > self._stop and self._step < 0) \
                or (self._start < self._stop and self._step > 0):

            result = Decimal(self._start)
            self._start += self._step
            return result.quantize(Decimal('1.0'))

        raise StopIteration()


assert (list(frange(5)) == [0, 1, 2, 3, 4])
assert (list(frange(2, 5)) == [2, 3, 4])
assert (list(frange(2, 10, 2)) == [2, 4, 6, 8])
assert (list(frange(10, 2, -2)) == [10, 8, 6, 4])
assert (list(frange(2, 5.5, 1.5)) == [2, 3.5, 5])
assert (list(frange(1, 5)) == [1, 2, 3, 4])
assert (list(frange(0, 5)) == [0, 1, 2, 3, 4])
assert (list(frange(0, 0)) == [])
assert (list(frange(100, 0)) == [])

print('success')

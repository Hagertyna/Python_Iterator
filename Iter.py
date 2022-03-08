#Creating a infinite custom iterator
class Infinite_Iter:
    """Infinite iterator to return all odd numbers"""

    def __iter__(self):
        self.num = 1
        return self
    def __next__(self):
        num = self.num
        self.num += 2
        return num
i = Infinite_Iter()
a = iter(i)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
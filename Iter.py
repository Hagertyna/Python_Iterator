#Creating a infinite custom iterator
class Infinite_Iter:
    """Infinite iterator to return all odd numbers"""

    #__iter__
    def __iter__(self):
        self.num = 1
        return self
    def __next__(self):
        num = self.num
        self.num += 2
        return num
i = Infinite_Iter()
a = iter(i)
#prints first element
print(next(a))
#prints second element
print(next(a))
#print's third element
print(next(a))
#prints fourth element
print(next(a))


#new list creation
values = [10, 20, 30]
iterator = iter(values)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

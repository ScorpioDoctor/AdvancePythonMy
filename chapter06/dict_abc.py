from collections import abc

mydict = {"a": 1, "b": 2}
mydict2 = dict()
print(type(mydict))
print(type(mydict2))
print(type(dict))
print(isinstance(mydict, abc.Mapping))
print(isinstance(mydict2, abc.MutableMapping))

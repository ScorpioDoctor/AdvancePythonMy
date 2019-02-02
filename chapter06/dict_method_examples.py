mydict = {"a": {"school": "studyai.com"},
          "b": {"school": "xjtu.com"},
          "c": [1, 2, 3],
          "d": 989}
# print(mydict)
# mydict.clear()
# print(mydict)

# mydict2 = mydict.copy()
# mydict2["a"]["school"] = "studyai.cn"
# print(mydict2)
# print(mydict)
#
# import copy
# mydict3 = copy.deepcopy(mydict)
# mydict3["a"]["school"] = "studyai.net"
# print(mydict3)
# print(mydict)

keys=(1,2,3)
mydict4 = dict.fromkeys(keys,"studyai.com")
# print(mydict4)

print(mydict4.get(4,"study"))

# print(type(mydict.items()))
# print(mydict.items())

# for key,value in mydict.items():
#     print(key,":",value)


# print(mydict.pop("d"))
# print(mydict.popitem())
# print(mydict.items())

# print(mydict.setdefault('c',"ai"))
# print(mydict.items())

print(mydict.items())
# mydict.update({"00":"xx"})
# mydict.update([("00","xx"),("oo","yyy")])
mydict.update((("00","xx"),("oo","yyy")))
print(mydict.items())
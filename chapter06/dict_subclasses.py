class MyDict(dict):
    def __setitem__(self, key, value):
        print("我被钓鱼啦！")
        super().__setitem__(key, value + "5")


mydict = MyDict(a="aaa")
# mydict["b"] = "aaa"
print(mydict)
# 不建议直接去继承 dict,list

from collections import UserDict, UserList, UserString


class MyUserDict(UserDict):
    def __setitem__(self, key, value):
        print("我被调用啦！")
        super().__setitem__(key, value + "--user")

    def __missing__(self, key):
        return "我是默认值！笑嘻嘻笑嘻嘻"


myuserdict = MyUserDict(a="bbb")
myuserdict['b'] = "cccc"
print(myuserdict["ppp"])


def set_default():
    return "我是默认值！studyai.cn"


from collections import defaultdict

# my_default = defaultdict(dict)
# my_default = defaultdict(list)
# my_default = defaultdict(School)
my_default = defaultdict(set_default)
# my_default = defaultdict(None)
value = my_default["studyai.com"]
print(value)

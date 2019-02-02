from collections.abc import Sized
class School(Sized):
    def __init__(self, teacher_list):
        self.teacher_list = teacher_list

    def __len__(self):
        return len(self.teacher_list)

class Xiaoxue(School):
    pass

sch = School(['王八蛋', '张三疯', '岳不群'])
if hasattr(sch, '__len__'):
    print(len(sch))
else:
    print("School class  has no __len__")

from collections import Sized

if isinstance(sch,Sized):
    print(len(sch))
else:
    print("School class  has no __len__")
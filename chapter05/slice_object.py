from collections import Sequence
from numbers import Integral


class School(object):
    def __init__(self, name, teacher_list):
        self.name = name
        self.teacher_list = teacher_list

    def __str__(self):
        return ':'.join(self.teacher_list)

    # def __reversed__(self):
    #     for i in reversed(range(len(self))):
    #         yield self[i]

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item,slice):
            return cls(self.name, self.teacher_list[item])
        elif isinstance(item,Integral):
            return cls(self.name,[self.teacher_list[item],])

    def __len__(self):
        return len(self.teacher_list)


sch = School('西安交大', ['王八蛋', '张三疯', '岳不群', 'studyai', 'antares'])
sub_sch = sch
for item in sub_sch:
    print(item)
sub_sch = sch[3:0:-1]
# sub_sch = sch[2]
print(type(sub_sch))
print(sub_sch)

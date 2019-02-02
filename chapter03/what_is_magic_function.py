class School(object):
    def __init__(self, teacher_list):
        self.teacher_list = teacher_list

    def __str__(self):
        return ':'.join(self.teacher_list)
    def __len__(self):
        return len(self.teacher_list)
    # def __iter__(self):
    #     pass
    def __getitem__(self, item):
        return self.teacher_list[item]

sch = School(['王八蛋', '张三疯', '岳不群'])
# print(sch.teacher_list[0:2])
# print(sch[1:2])
# sch
# list,set ,tuple,dict
print(len(sch))
for tech in sch:
    print(tech)
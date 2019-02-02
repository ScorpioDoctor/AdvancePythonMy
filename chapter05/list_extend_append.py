class School(object):
    def __init__(self, teacher_list):
        self.teacher_list = teacher_list
    def __str__(self):
        return ':'.join(self.teacher_list)
    def __len__(self):
        return len(self.teacher_list)
    def __getitem__(self, item):
        return self.teacher_list[item]

sch = School(['王八蛋', '张三疯', '岳不群'])

q = [1, 2, 3]
# print(id(q))
p = ('a', 'x', (1, 2, 5))
# qp = q + p  #产生新对象
# print(id(qp))
# print(qp)
# q += sch #原位操作，不产新的对象
# q.extend(p)
# q.extend(sch)
q.append(p)
q.append(sch)
# print(id(q))
print(q)

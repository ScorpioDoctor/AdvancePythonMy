class Duck(object):
    teacher_list =['王八蛋','猪八戒']
    def eat(self):
        print("duck eat 鱼~~ ")
    # def __iter__(self):
    #     pass
    def __getitem__(self, item):
        return self.teacher_list[item]

class Chicken(object):
    def eat(self):
        print("chicken eat 虫子~~ ")
    def __getitem__(self, item):
        foods = ["虫子1","虫子2","虫子3"]
        return foods[item]

class Dog(object):
    def eat(self):
        print("dog eat 骨头~~ ")
    def __getitem__(self, item):
        foods = ["骨头1","骨头2","骨头3"]
        return foods[item]

class Car(object):
    def eat(self):
        print("car eat 石油~~ ")

# animals = [Dog(), Chicken(), Duck(),Car()]
# for animal in animals:
#     animal.eat()

xyz = ["qq","study","ai"]
ppp = [".com", ".cn"]
tuple1 = (".com", ".cn")
setq = set()
setq.add("study")
setq.add("python")
xyz.extend(ppp)
xyz.extend(tuple1)
xyz.extend(setq)
duck = Duck()
chk = Chicken()
xyz.extend(duck)
xyz.extend(chk)
xyz.extend(Dog())
print(xyz)


# class Animal(object):
#     def eat(self):
#         print("animal eat something~~ ")
# class Machine(object):
#     def eat(self):
#         print("机器 eat something~~ ")
# class Cat(Animal):
#     def eat(self):
#         print("cat eat 鸟~~ ")
# class Pig(Animal):
#     def eat(self):
#         print("pig eat 草料~~ ")
#
#
# Animal ani = new Pig()
# ani.eat()
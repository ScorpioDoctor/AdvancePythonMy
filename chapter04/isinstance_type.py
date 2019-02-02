class Base(object):
    pass
class Child(Base):
    pass

child = Child()
print(isinstance(child,Child))
print(isinstance(child,Base))
print(type(child) is Child)
print(id(type(child))==id(Child))
print(type(child) is Base)
print(id(type(child)), id(Base))
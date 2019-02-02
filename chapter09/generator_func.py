# 生成器函数：只要这个函数里面写了yield这个关键字，他就是生成器函数
# 生成器函数的返回值是一个generator对象，他实现了迭代器协议
# 生成器对象是在Python编译字节码的时候就产生了
# 生成器对象可以迭代返回很多个值，迭代求值过程是懒惰的或者叫延迟的
def gen_func():
    yield "abc"
    yield "123"
    yield "www"
    yield "studyai.com"
    return 0
# 普通函数
def normal_func():
    return ["abc","123","www","studyai.com"]

if __name__=="__main__":
    gen = gen_func()#生成器函数的返回值是一个generator对象，他实现了迭代器协议
    for val in gen:
        print(val)
    # norm = normal_func()
    pass
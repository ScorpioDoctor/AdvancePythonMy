# 斐波拉契数列: 0，1，1，2，3，5，8，13，21

# 递归调用：退出条件
def digui_fab(n):
    if n <= 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return digui_fab(n - 2) + digui_fab(n - 1)


# 希望得到求值中间过程：打印整个数列
def fab_func1(n):
    a0, a1 = 0, 1
    res_list = [a0]
    index = 1
    while index <= n:
        res_list.append(a1)
        a0, a1 = a1, a0 + a1
        index += 1
    return res_list

# 用生成器函数来实现，得到求值中间过程：打印整个数列
def fab_gen_func(n):
    a0, a1 = 0, 1
    index = 0
    while index <= n:
        yield a0
        a0, a1 = a1, a0 + a1
        index += 1

if __name__ == "__main__":
    print(digui_fab(10))
    print(fab_func1(10))
    gen = fab_gen_func(10)
    # 在迭代求值输出的时候，每次迭代计算一个值，不会导致内存爆炸
    # 在输出求值过程的时候不用去保存每次的结果
    for val in gen:
        print(val)

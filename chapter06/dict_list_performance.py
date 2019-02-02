from random import randint, Random


def random_str(random_length=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        str += chars[random.randint(0, length)]
    return str


def write_data_to_file(file_name="oooxxx.txt", maxlines=100):
    with open(file_name, encoding="utf8", mode="a") as f_open:
        for line in range(maxlines):
            f_open.writelines([random_str(randint(20, 80)), '\n'])


def load_list_data(total_nums, target_nums, file_name="oooxxx.txt"):
    """
    从文件中读取数据，以list的方式返回
    :param total_nums: 读取的数量
    :param target_nums: 需要查询的数据的数量
    """
    all_data = []
    target_data = []

    with open(file_name, encoding="utf8", mode="r") as f_open:
        for count, line in enumerate(f_open):
            if count < total_nums:
                all_data.append(line)
            else:
                break

    for x in range(target_nums):
        random_index = randint(0, total_nums)
        if all_data[random_index] not in target_data:
            target_data.append(all_data[random_index])
            if len(target_data) == target_nums:
                break

    return all_data, target_data


def load_dict_data(total_nums, target_nums, file_name="oooxxx.txt"):
    """
    从文件中读取数据，以dict的方式返回
    :param total_nums: 读取的数量
    :param target_nums: 需要查询的数据的数量
    """
    all_data = {}
    target_data = []

    with open(file_name, encoding="utf8", mode="r") as f_open:
        for count, line in enumerate(f_open):
            if count < total_nums:
                all_data[line] = 0
            else:
                break
    all_data_list = list(all_data)
    for x in range(target_nums):
        random_index = randint(0, total_nums - 1)
        if all_data_list[random_index] not in target_data:
            target_data.append(all_data_list[random_index])
            if len(target_data) == target_nums:
                break

    return all_data, target_data


def find_test(all_data, target_data):
    # 测试运行时间
    test_times = 100
    total_times = 0
    import time
    for i in range(test_times):
        find = 0
        start_time = time.time()
        for data in target_data:
            # 判断一个随机字符串在一个列表里面花的时间长还是在字典里面花的时间长
            if data in all_data:
                find += 1
        last_time = time.time() - start_time
        total_times += last_time
    return total_times / test_times


if __name__ == "__main__":
    # write_data_to_file(file_name="oooxxx.txt", maxlines=1000000)
    # all_data, target_data = load_list_data(10000, 1000, file_name="oooxxx.txt")#花费时间：0.055323164463043216
    # all_data, target_data = load_list_data(100000, 1000, file_name="oooxxx.txt")#花费时间：0.7014501214027404
    # all_data, target_data = load_list_data(1000000, 1000,file_name="oooxxx.txt")#花费时间：很长很长。。。

    # all_data, target_data = load_dict_data(10000, 1000)#花费时间：8.000373840332031e-05
    # all_data, target_data = load_dict_data(100000, 1000)#花费时间：0.00010000467300415039
    all_data, target_data = load_dict_data(1000000, 1000)#花费时间：0.000130007266998291
    last_time = find_test(all_data, target_data)
    print(last_time)

    #dict查找性能远大于list
    #list中的数据查找时间与list的长度正比例
    #dict里面查找元素的时间几乎与dict的容量无关

    #1、dict的key或者set的值，都必须是可以hash的
    #2、不可变对象都是可hash的：str,frozenset，tuple,自己实现的类：__hash__
    #3、dict的内存开销较大但是查询速度快，查找算法的速度 o(1)
    #4、dict的元素存储顺序和添加顺序有关
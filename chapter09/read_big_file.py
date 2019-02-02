from random import randint, Random


# 产生指定长度的随机字符串
def random_str(random_length=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        str += chars[random.randint(0, length)]
    return str


# 写随机字符串数据到指定的文件
def write_data_to_file(file_name="oooxxx.txt", maxlines=100):
    with open(file_name, encoding="utf8", mode="a") as f_open:
        for line in range(maxlines):
            f_open.writelines([random_str(randint(20, 80)), '<||>'])

# 根据分隔符按行读取被写成一行的大文件
def read_big_file(f, spliter):
    buf = ""
    while True:
        # 检测buf里面有没有分隔符spliter，
        # 如果有，说明当前buf里面还有完整的行，不断的输出这些行
        while spliter in buf:
            pos = buf.index(spliter)
            yield buf[0:pos]
            #把已经输出的行给冲掉
            buf = buf[pos + len(spliter):]
        #如果上面的buf没有完整的行，就接着读取文件内容
        chunk = f.read(4096)# 有可能包含多行内容，也有可能包含不完整的行
        if not chunk:
            yield buf
            break
        else:
            buf += chunk


if __name__ == "__main__":
    # write_data_to_file("bigfile.txt", maxlines=100)
    with open("bigfile.txt",mode='r') as f:
        gen = read_big_file(f,'<||>')
        for line in gen:
            print(line)
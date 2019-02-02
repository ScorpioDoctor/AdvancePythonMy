# 实现上下文管理器协议的类
class FileReader(object):
    def __init__(self):
        print("FileReader正在初始化。。。")
    def __enter__(self):
        print("正在进入FileReader上下文")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("文件正在关闭~~")
    def read_file(self):
        print("正在读取文件")


with FileReader() as reader:
    print(type(reader))
    reader.read_file()

print("上下文已退出")
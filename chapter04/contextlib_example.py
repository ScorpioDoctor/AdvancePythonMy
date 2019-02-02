import contextlib

@contextlib.contextmanager
def file_read(filename):
    print("正在进入FileReader上下文")
    yield {}
    print("文件正在关闭~~")

def process_file(file_opened):
    print("file 正在处理中")


with file_read("studyai.com.txt") as file_opened:
    process_file(file_opened)

print("文件处理完毕，with上下文已退出")
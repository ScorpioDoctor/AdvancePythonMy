# try except else finally
try:
    print("Study begining")
    a=[1,2,3]
    a[2] = 9
    s = 1 / 2
    f_read = open("studyai.com")
    # raise KeyError
except KeyError as e:
    print("key error")
except ZeroDivisionError as e:
    print("zero divide error")
except FileNotFoundError as e:
    print("file not found error")
except Exception as e:
    print("exception error")
else:
    print("i am else")
finally:
    f_read.close()
    print("i am finally")


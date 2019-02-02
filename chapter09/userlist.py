from collections import UserList

class MyList(UserList):
    def __iter__(self):
        i = 0
        try:
            while True:
                v = self[i]
                yield {i:v}
                i += 1
                # yield i
        except IndexError:
            return

if __name__=="__main__":
    mylist = MyList(["a","c","studyai"])

    for item in mylist:
        print(item)
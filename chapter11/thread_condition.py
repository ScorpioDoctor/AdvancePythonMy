# 条件变量用于复杂的线程间同步
import threading
import time

class God(threading.Thread):
    def __init__(self,lock):
        self.lock = lock
        super().__init__(name="上帝")
    def run(self):
        self.lock.acquire()
        print(self.name+"问: 你是谁？")
        self.lock.release()
        time.sleep(1)

        self.lock.acquire()
        print(self.name+"问: 你来自何方？")
        self.lock.release()
        time.sleep(1)


class Human(threading.Thread):
    def __init__(self,lock):
        self.lock = lock
        super().__init__(name="人类")
    def run(self):
        self.lock.acquire()
        print(self.name+"答: 我是猪八戒！")
        self.lock.release()
        time.sleep(1)
        self.lock.acquire()
        print(self.name+"答: 我来自凌霄宝殿！")
        self.lock.release()
        time.sleep(1)


class God2(threading.Thread):
    def __init__(self,cond):
        self.cond = cond
        super().__init__(name="上帝")
    def run(self):
        with self.cond:
            print(self.name+"问: 你是谁？")
            self.cond.notify()
            self.cond.wait()

            print(self.name+"问: 你来自何方？")
            self.cond.notify()
            self.cond.wait()

            print(self.name + "问: 你要去何方？")
            self.cond.notify()
            self.cond.wait()

            print(self.name + "问: 你去干什么？")
            self.cond.notify()
            self.cond.wait()

class Human2(threading.Thread):
    def __init__(self,cond):
        self.cond = cond
        super().__init__(name="人类")
    def run(self):
        with cond:
            self.cond.wait()
            print(self.name+"答: 我是猪八戒！")
            self.cond.notify()
            self.cond.wait()
            print(self.name+"答: 我来自凌霄宝殿！")
            self.cond.notify()
            self.cond.wait()
            print(self.name + "答: 我要去高老庄！")
            self.cond.notify()
            self.cond.wait()
            print(self.name + "答: 我要去学Python！")
            self.cond.notify()

if __name__=="__main__":
    # lock = threading.Lock()
    # god = God(lock)
    # human = Human(lock)
    # god.start()
    # human.start()

    cond = threading.Condition()
    god2 = God2(cond)
    human2 = Human2(cond)
    # 先启动上帝线程，再启动人类线程
    # god2.start()
    # human2.start()
    # 先启动人类线程，再启动上帝线程
    human2.start()
    god2.start()
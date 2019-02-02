class MyDate(object):
    #构造函数：对象(实例)方法
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    #魔法函数：对象(实例)方法
    def __str__(self):
        return "{0}年{1}月{2}日".format(self.year,self.month, self.day)
    #对象(实例)方法
    def yesteday(self):
        return MyDate(self.year,self.month,self.day-1)
    #静态方法
    @staticmethod
    def parse_date_str(date_str):
        year, month, day = tuple(date_str.split('-'))
        return MyDate(year,month,day)
    @staticmethod
    def valid_date_str(date_str):
        year, month, day = tuple(date_str.split('-'))
        if int(month)>0 and int(month)<13:
            return True
        else:
            return False
    # 类方法
    @classmethod
    def parse_from_string(cls,date_str):
        year, month, day = tuple(date_str.split('-'))
        return cls(year, month, day)

if __name__ == "__main__":
    my_date = MyDate(2019, 1, 12)
    print(my_date)
    yestday = my_date.yesteday()
    print(yestday)
    #用字符串来产生日期
    date_str= "2019-12-165"
    year,month,day = tuple(date_str.split('-'))
    new_date = MyDate(year,month,day)
    print("new_date: ",new_date)
    #用静态方法来解析字符串日期
    new_date2 = MyDate.parse_date_str(date_str)
    print("new_date2: ",new_date)
    # 用类方法来解析字符串日期
    new_date3 = MyDate.parse_from_string(date_str)
    print("new_date3: ", new_date)
    # 用静态方法来验证日起字符串换
    res = MyDate.valid_date_str(date_str)
    print(res)
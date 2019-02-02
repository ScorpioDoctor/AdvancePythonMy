# 设计一个分类器基类
class ClassifierBase():
    def train(self, train_data, train_label):
        raise NotImplementedError
    def predict(self, test_data):
        raise NotImplementedError
base_classifier = ClassifierBase()
import abc
class ClassifierBase2(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def train(self, train_data, train_label):
        pass
    @abc.abstractmethod
    def predict(self, test_data):
        pass
# base_classifier2 = ClassifierBase2()
# 设计一个支持向量分类器
class SVMClassifier(ClassifierBase2):
    def train(self, train_data, train_label):
        print("分类器正在训练：SVM")
    def predict(self, test_data):
        print("分类器正在预测：SVM")


svm = SVMClassifier()
svm.train("xxx", "00000")
svm.predict("yyy")

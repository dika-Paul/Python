import numpy as np


# 神经元激活函数
def active_func(input_num):
    return input_num


# 神经元
class Neuron:

    def __init__(self, weights, bias):
        self._weights = weights
        self._bias = bias

    # 强化学习，可以理解为接受外来数据后进行运算
    def FeedForward(self, input_weights):
        cal_res = np.dot(self._weights, input_weights) + self._bias
        return active_func(cal_res)


def main():
    weights = np.array([0, 1])
    bias = 2
    n = Neuron(weights, bias)
    x = np.array([2, 3])
    print(n.FeedForward(x))


if __name__ == "__main__":
    main()

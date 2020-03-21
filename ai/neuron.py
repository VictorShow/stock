import tensorflow as tf
import math
import numpy as np
class Neuron:
    @staticmethod
    def new_random_uniform_number(dim):
        #균일 분포 : MAX, MIN사이값 동일분포에서 수 추출
        # [1] 결과값 shop 행, 열 차원의 수 2*3
        rand = tf.random.uniform([dim], 0, 1)
        print(rand)
        return rand

    @staticmethod
    def new_random_normal_number(dim):
        #균일 분포 : MAX, MIN사이값 동일분포에서 수 추출
        # [1] 결과값 shop 행, 열 차원의 수 2*3
        rand = tf.random.random([dim], 0, 1)
        print(rand)
        return rand

    @staticmethod
    def sigmoid(x):
        return 1/(1 + math.exp(-x))


    def new_neuron(self):
        x = 0
        y = 1
        w = tf.random.normal([1], 0, 1)
        b = tf.random.normal([1], 0, 1)
        for i in range(1000):
            neuron = self.sigmoid(x * w + 1 * b)
            error = y - neuron  # 1과의 거리 ...차이를 말함..
            w = w + x * 0.1 * error
            b = b + x * 0.1 * error

            if i  % 100 == 99:
                print(i, error, neuron)
        return neuron

    # sigmoid함수는 예전 버전..
    def sigmoid_tanh_relu(self):
        x = np.arange(-5, 5, 0.01)
        sigmoid_x = [self.sigmoid(z) for z in x]
        tanh_x = [math.tanh(z) for z in x]
        relu = [0 if z < 0 else z for z in x]
        return {'x' : x, 'sigmoid_x' : sigmoid_x, 'tanh_x' : tanh_x, 'relu' : relu}
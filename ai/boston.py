from ai.util import Storage
from tensorflow.keras.datasets import boston_housing
from tensorflow import keras
import tensorflow as tf
class Boston:
    boston : object

    def __init__(self):
        self.storage = Storage

    @property
    def boston(self) -> object: return self._boston

    @boston.setter
    def boston(self, boston): self._boston = boston

    def initialize(self):
        this = self.storage
        (train_data, train_targets), (test_data, test_targets) = boston_housing.load_data()
        #print(f'확률변수 x의 길이 :  {len(this.train_X)}')
        #print(f'확률변수 y의 길이 :  {len(this.train_Y)}')
        #print(f'확률변수 x[0] :  {this.train_X[0]}')
        #print(f'확률변수 y[0] :  {this.train_y[0]}')
        """
        crim : crime rate, zn : residential area rate, indus : biz district rate, chas: close river 1 or 0
        nox : nitrous oxide concentration, rm : a number of room per house, age : housing before 1940s rate,
        dis : vocational employment center distance , rad: access to highway, tax, ptratio: teacher per students rate,
        b : black man rate , lstat : lower layer ratio, medv : center value for housing price
        """

    def standardization(self):
        this = self.storage
        x_mean = this.train_X.mean(axis=0)
        x_std = this.train_X.std(axis=0)
        this.train_X -= x_mean
        this.train_X /= x_std
        this.test_X -= x_mean
        this.test_X /= x_std

        y_mean = this.train_Y.mean(axis=0)
        y_std = this.train_Y.std(axis=0)
        this.train_Y -= y_mean
        this.train_Y /= y_std
        this.test_Y -= y_mean
        this.test_Y /= y_std

    def new_model(self):
        model = keras.Sequential([
                keras.layers.Flatten(),
                keras.layers.Dense(units=52, activation='relu', input_shape=(13, 1)), # 엽력 13 출력 1
                keras.layers.Dense(units=39, activation='relu'),
                keras.layers.Dense(units=26, activation='relu'),
                keras.layers.Dense(units=1) # 출력 1(마지막층)
        ])

        model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.07), loss='mse')
        return model

    def learn_model(self, model):
        this = self.storage
        history = model.fit(this.train_X, this.train_Y, epochs=25,
                            batch_size=32, validation_split=0.25,
                            callbacks=[tf.keras.callbacks.EarlyStopping(patience=3,
                                                                        monitor='val_loss')])       #관대 적합을 피하기 위해서....이런 조건을 줌..
        return history

    def eval_model(self, model):
        this = self.storage
        print(model.evalute(this.test_X, this.test_Y))  # 평가.
        return this

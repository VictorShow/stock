from ai.util import Storage
from tensorflow.keras.datasets import boston_housing
from tensorflow import keras
import tensorflow as tf
import pandas as pd
class Wine:
    wine : object

    def __init__(self):
        self.storage = Storage()

    @property
    def wine(self) -> object: return self._wine

    @wine.setter
    def wine(self, wine): self._wine = wine

    def initialize(self):

        red = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv', sep=';')
        white = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv', sep=';')

    def normalization(self):
        pass

    def new_model(self):
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(units=48, activation='relu', input_shape=(12,)),
            tf.keras.layers.Dense(units=24, activation='relu'),
            tf.keras.layers.Dense(units=12, activation='relu'),
            tf.keras.layers.Dense(units=48, activation='softmax')       # 결과값이 1이상 나올때..
        ])
        model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.07),
                      loss='categorical_crossentropy',      # 크로스엔트로피
                      metrics=['accuracy'])
        print(f'model summary : {model.summary()}')
        return model

    def learn_model(self, model):
        this = self.storage
        history = model.fit(this.train_X, this.train_Y, epochs=25, batch_size=32, validation_splite=0.25)
        return history

    def eval_model(self, model):
        this = self.storage
        model.evalute(this.test_X, this.test_Y)

if __name__ == '__main__':
    wine = Wine()
    wine.initialize()
    wine.normalization()
    model = wine.new_model()
    history = wine.learn_model(model)
    wine.eval_model(model)
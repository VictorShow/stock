import tensorflow as tf
import tensorflow_hub as hub
from ai.view import View
from ai.neuron import Neuron
from ai.iris import Iris
from ai.boston import Boston
from ai.wine import Wine

if __name__ == '__main__':
    def print_menu():
        print('0, Show Version')
        print('1, Random Number')
        print('2, Neuron')
        print('3, Iris')
        print('4, Boston')
        print('5, Wine')
        return input('Select Menu\n')
    view = View()
    while 1:
        menu = print_menu()
        if menu == '0':
            print(f'버전 : {tf.__version__}')
            print(f'즉시실행모드 : {tf.executing_eagerly}')
            print(f'허브버전 : {hub.__version__}')
            print('GPU', '사용가능' if tf.config.experimental.list_logical_devices('GPU') else '사용 불가능')

        if menu == '1':
            neu = Neuron()
            rand = neu.new_random_uniform_number(100)
            view.show_hist(rand)
            view.show_line(rand)
            rand = neu.new_random_normal_number(100)
            view.show_hist(rand)
            view.show_blot(rand)

        if menu == '2':
            neu = Neuron()
            neuron = neu.new_neuron()
            dic = neu.sigmoid_tanh_relu()
            view.show_sigmoid_tanh_relu((dic))

        if menu == '3':
            iris = Iris()
            iris.initialize()
            iris.show_scatter()
            iris.show_errors()
            # iris.show_decision_tree()       # 알고리즘..
            iris.show_adaline()

        if menu == '4':
            boston = Boston()
            boston.initialize()
            boston.standardization()
            model = boston.new_model()
            history = boston.learn_model(model)
            storage = boston.eval_model(model)
            boston.eval_model(model)
            view.show.history(history)
            view.show_boston({'model' : model, 'storage' : storage})

        if menu == '5':
            wine = Wine()
            wine.initialize()
            wine.normalization()
            model = wine.new_model()
            history = wine.learn_model(model)
            wine.eval_model(model)
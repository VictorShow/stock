from algorithm.dtree import Dtree
if __name__ == '__main__':
    def print_menu():
        print('0. Exit')
        print('1. 결정트리')
        return input('메뉴선택 \n')
    while 1:
        menu = print_menu()
        if menu == '0':
            break
        if menu == '1':
            app = Dtree()
            # Dtree().breast_cancer()
            Dtree.iris()
            # print('유방암 분류기 정화고: %f' % Dtree().breast_cancer())

        if menu == '2':
            pass
from crime_map.controller import Controller
from crime_map.foliumtest import Foliumtest


if __name__ == '__main__':
    def print_menu():
        print('0, Exit')
        print('1, MODELING')
        print('2, CRIME MAP')
        print('3, 미국 실업율 지도')
        return input('Select Menu\n')

    app = Controller()

    while 1:
        menu = print_menu()
        if menu == '1':
            app.pilice_pos()
            app.cctv_pop()
            app.police_norm()

        if menu == '2':
            # 숫자화한다.
            # 인식하기 위해..
            app.crime_map()

        if menu == '3':
            # app.learning('train.csv', 'test.csv')
            t = Foliumtest()
            t.show_map()

        if menu == '4':
            # app.summit('train.csv', 'test.csv')
            pass

        if menu == '5':
            t = Foliumtest()
            t.show_map()

        elif menu == '0':
            break

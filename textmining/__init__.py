from textmining.controller import Controller

if __name__ == '__main__':
    def print_menu():
        print('0, Exit')
        print('1, 사전 다운로드')
        print('2, 삼성 전략보고서 분석')
        print('3, 스톱워드 추출')
        return input('Select Menu\n')

    app = Controller()

    while 1:
        menu = print_menu()
        if menu == '1':
            app.download_dictionary()

        if menu == '2':
            #app.data_analysys('kr-Report_2018.txt')
            app.data_analysys()
        if menu == '3':
            app.data_stopword('stopwords.txt')

        elif menu == '0':
            break

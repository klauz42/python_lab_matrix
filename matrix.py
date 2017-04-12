from random import randint

class matrix:

    def __init__(self, size):
        self.size = int(size)
        self.M = [[0] * self.size for i in range(self.size)]

    def __getitem__(self, item):
        return self.M[item[0]][item[1]]

    def __setitem__(self, key, value):
        self.M[key[0]][key[1]] = int(value)

    def print(self):
        for i in range(self.size):
            print(self.M[i])
        print('')

    def __str__(self):
        tmp = ""
        for i in range(self.size):
            tmp += str(self.M[i]) + "\n"
        return tmp

    def makeident(self):
        for i in range(self.size):
            for j in range(self.size):
                if i == j:
                    self.M[i][j] = 1
                else:
                    self.M[i][j] = 0

    def makezero(self):
        self.M = [[0] * self.size for i in range(self.size)]

    def makerandom(self):
        for i in range(self.size):
            for j in range(self.size):
                self.M[i][j] = randint(0, 100)

    def __mul__(self, other):
        tmp = matrix(self.size)
        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    #tmp.M[i][j] +=  int(self.M[i][j]) * int(other.M[j][i])
                    tmp[i, j] += self[i, k] * other[k, j]
        return tmp

    def saveadd(self, i, j, value):
        try:
           self[i, j] = int(value)
           return True
        except ValueError:
            print("Недопустимый ввод! Попробуйте еще раз.")
            return False

    def savetofile(self, path):
        f = open(str(path), "w")
        tmp = ''
        for i in range(self.size):
            for j in range(self.size):
                tmp += str(self[i, j]) + " "
        f.write(tmp)
        f.close()

    def loadfromfile(self, path):
        f = open(str(path))
        tmp = f.read()
        f.close()
        el = tmp.split(" ")
        el.pop()
        s = int(len(el) ** (1/2))
        k = 0
        t = matrix(s)

        for i in range(s):
            for j in range(s):
                t[i, j] = int(el[k])
                k += 1
        return t

    def changeel(self):
        check = False
        while not check:
            i = int(input("Введите номер строки: "))
            j = int(input("Введите номер столбца: "))
            v = int(input("Введите значение: "))
            if i < self.size and i >= 0 and j < self.size and i >= 0:
                check = self.saveadd(i,j, v)
            else:
                print("Элемента не существует! Попробуйте еще раз: ")
                check = False

    def fillmatrix(self):
        cancel = False
        tmp = matrix(self.size)
        for i in range(self.size):
            for j in range(self.size):
                if cancel == True:
                    break
                else:
                    check = False
                    while not check:
                        t = input("Введите (целочисленное значение) элемент [{0}, {1}]: ".format(i, j))
                        if t == "cancel":
                            cancel = True
                            break
                        else:
                            check = tmp.saveadd(i, j, t)

def help():
    print("01 - создать первую матрицу\n"
          "02 - создать вторую матрицу\n"
          "1. Заполнить первую матрица с клавиатуры\n"
          "2. Заполнить вторую матрицу с клавиатуры\n"
          "3. Заполнить первую матрицу нулями\n"
          "4. Заполнить вторую матрицу нулями\n"
          "5. Заполнить первую матрицу случайными значениями\n"
          "6. Заполнить вторую матрицу случайными значениями\n"
          "7. Сделать первую матрицу единичной\n"
          "8. Сделать вторую матрицу единичной\n"
          "9. Перемножить матрицы\n"
          "10. Показать первую матрицу\n"
          "11. Показать вторую матрицу\n"
          "12. Поменять элемент в первой матрице\n"
          "13. Поменять элемент во второй матрице\n"
          "14. Сохранить первую матрицу в файл\n"
          "15. Сохранить вторую матрицу в файл\n"
          "16. Загрузить первую матрицу из файла\n"
          "17. Загрузить вторую матрицу из файла\n"
          "\n"
          "exit - закрыть приложение\n"
          "help - вывести список команд\n")

def task(m1, m2, isFirstExist, isSecExist):
    try:
        while True:
            select = input("Введите команду: ")
            if (select == "01"):
                s1 = int(input("Введите размерность матрицы: "))
                m1 = matrix(s1)
                isFirstExist = True
            elif (select == "02"):
                s2 = int(input("Введите размерность матрицы: "))
                m2 = matrix(s2)
                isSecExist = True
            elif (select == "1"):
                if isFirstExist == True:
                    m1.fillmatrix()
                else:
                    print("Матрица не создана")
            elif (select == "2"):
                if isSecExist == True:
                    m2.fillmatrix()
                else:
                    print("Матрица не создана")
            elif (select == "3"):
                if isFirstExist == True:
                    m1.makezero()
                else:
                    print("Матрица не создана")
            elif (select == "4"):
                if isSecExist == True:
                    m2.makezero()
                else:
                    print("Матрица не создана")
            elif (select == "5"):
                if isFirstExist == True:
                    m1.makerandom()
                else:
                    print("Матрица не создана")
            elif (select == "6"):
                if isSecExist == True:
                    m2.makerandom()
                else:
                    print("Матрица не создана")
            elif (select == "7"):
                if isFirstExist == True:
                    m1.makeident()
                else:
                    print("Матрица не создана")
            elif (select == "8"):
                if isSecExist == True:
                    m2.makerandom()
                else:
                    print("Матрица не создана")
            elif (select == "9"):
                if isFirstExist != True or isSecExist != True:
                    print("Не созданы обе матрицы")
                elif m1.size != m2.size:
                    print("Размерности не совпадают, перемножение невозможно.")
                elif isFirstExist == True and isSecExist == True:
                    m1 = m1 * m2
            elif (select == "10"):
                if isFirstExist == True:
                    print(m1)
                else:
                    print("Матрица не создана")
            elif (select == "11"):
                if isSecExist == True:
                    print(m2)
                else:
                    print("Матрица не создана")
            elif (select == "12"):
                if isFirstExist == True:
                    m1.changeel()
                else:
                    print("Матрица не создана")
            elif (select == "13"):
                if isSecExist == True:
                    m2.changeel()
                else:
                    print("Матрица не создана")
            elif (select == "14"):
                if isFirstExist == True:
                    path = input("Введите путь для сохранения: ")
                    m1.savetofile(str(path))
                else:
                    print("Матрица не создана")
            elif (select == "15"):
                if isSecExist == True:
                    path = input("Введите путь для сохранения: ")
                    m2.savetofile(str(path))
                else:
                    print("Матрица не создана")
            elif (select == "16"):
                if isFirstExist == True:
                    path = input("Введите путь для загрузки: ")
                    m1 = m1.loadfromfile(str(path))
                else:
                    print("Матрица не создана")
            elif (select == "17"):
                if isSecExist == True:
                    path = input("Введите путь для загрузки: ")
                    m2 = m2.loadfromfile(str(path))
                else:
                    print("Матрица не создана")
            elif (select == "exit"):
                raise SystemExit(0)
            elif (select == "help"):
                help()
            else:
                print("Недопустимая команда!")
    except ValueError:
        print("Неверное значение! Возвращаюсь в меню.")
        task(m1, m2, isFirstExist, isSecExist)
    except FileNotFoundError:
        print("Файл не найден! Возвращаюсь в меню.")
        task(m1, m2, isFirstExist, isSecExist)

m1 = matrix(0)
m2 = matrix(0)
isFirstExist = False
isSecExist = False

print("Работа с матрицами")
help()
task(m1, m2, isFirstExist, isSecExist)

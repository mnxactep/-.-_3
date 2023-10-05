# Функция для определения цвета поля
def is_same_color(k, l, m, n):
    return (k + l) % 2 == (m + n) % 2

# Функция для определения угрозы фигуры полю
def is_threatened(k, l, m, n, figure):
    if figure == "ферзь":
        return k == m or l == n or abs(k - m) == abs(l - n)
    elif figure == "ладья":
        return k == m or l == n
    elif figure == "слон":
        return abs(k - m) == abs(l - n)
    elif figure == "конь":
        return (abs(k - m) == 2 and abs(l - n) == 1) or (abs(k - m) == 1 and abs(l - n) == 2)
    else:
        return False

# Функция для определения возможности попадания на поле
def can_reach(k, l, m, n, figure):
    if figure == "ладья" or figure == "ферзь":
        return k == m or l == n
    elif figure == "слон":
        return abs(k - m) == abs(l - n)
    else:
        return False

# Функция для определения возможности попадания на поле за два хода
def can_reach_in_two_moves(k, l, m, n, figure):
    if figure == "слон":
        for i in range(1, 9):
            for j in range(1, 9):
                if abs(k - i) == abs(l - j) and abs(i - m) == abs(j - n):
                    return True
        return False
    else:
        return False

# Ввод данных от пользователя
k = int(input("Введите номер вертикали для первого поля: "))
l = int(input("Введите номер горизонтали для первого поля: "))
m = int(input("Введите номер вертикали для второго поля: "))
n = int(input("Введите номер горизонтали для второго поля: "))

# Условие для верно введённых данных полей
while k >= 9 or l >= 9 or m >= 9 or n >= 9:
        print("Введенные данные должны быть числами меньше или равными 8.")
        k = int(input("Введите номер вертикали для первого поля: "))
        l = int(input("Введите номер горизонтали для первого поля: "))
        m = int(input("Введите номер вертикали для второго поля: "))
        n = int(input("Введите номер горизонтали для второго поля: "))

figure = input("Введите название фигуры (ферзь, ладья, слон или конь): ")

# Проверка цвета полей
if is_same_color(k, l, m, n):
    print("Поля (", k, ",", l, ") и (", m, ",", n, ") являются полями одного цвета.")
else:
    print("Поля (", k, ",", l, ") и (", m, ",", n, ") не являются полями одного цвета.")

# Проверка угрозы фигуры полю
if is_threatened(k, l, m, n, figure):
    print("Фигура", figure, "угрожает полю (", m, ",", n, ").")
else:
    print("Фигура", figure, "не угрожает полю (", m, ",", n, ").")

# Проверка возможности попадания на поле
if can_reach(k, l, m, n, figure):
    print("Фигура", figure, "может попасть на поле (", m, ",", n, ") одним ходом.")
elif can_reach_in_two_moves(k, l, m, n, figure):
    print("Фигура", figure, "может попасть на поле (", m, ",", n, ") за два хода.")
else:
    print("Фигура", figure, "не может попасть на поле (", m, ",", n, ") за два хода.")

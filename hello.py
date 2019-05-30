names = ["кирилл"]
a = input ("введите свое имя: ")
while True:
    if a in names:
        print("Добро пожаловать " + a)
        break
    else: 
        print("Мы с вами не знакомы")
        b = input("Хотите что бы вас добавили в список пользователей?")
        if b == "да":
            names.append(a)
        elif b == "нет":
            print("ну и не надо")
        else:
            print("ты ввел что то не то")
while True:
    action = input(a + " что нужно сделать?(калькулятор, фильмы или выйти)")
    if action == "калькулятор":
        while True:
            action_culc = input("что нужно сделать? (+, -, *, / или выйти)")
            if action_culc == "выйти":
                break
            num_1 = input("введите первое число: ")
            num_2 = input("введите второе число: ")
            if action_culc == "+":
                print (int(num_1) + int(num_2))
            elif action_culc == "-":
                print(int(num_1) - int(num_2))
            elif action_culc == "*":
                print(int(num_1) * int(num_2))
            elif action_culc == "/":
                print(int(num_1) / int(num_2))
            else:
                print("ты ввел что то не то")
    elif action == "фильмы":
        while True:
            action_films = input("введите жанр фильма который хотели бы посмотреть или выйти (фантастика, мультфильмы, история, документальные, боевики, сериалы)")
            if action_films == "выйти":
                break
            elif action_films == "фантастика":
                print("1. Мстители 2. Матрица 3. Властелин колец 4. Терминатор 5. Гарии Поттер 6. Лига Справедливости")
                break
            elif action_films == "мультфильмы":
                print("1.Тачки  2. Маша и Медведь 3. Мулан 4. Зверополис 5. Щенячий патруль")
                break
            elif action_films == "история":
                print("1.Троя 2. Брестская крепость 3.Ганди  4.Игры разума 5. Кон-Тики")
                break
            elif action_films == "документальные":
                print("1.Сноуден  2. Сена 3.Канатаходец  4.Стивен Хоккинг. Судьба вселенной 5. Джобс. Империя Соблазна")
                break
            elif action_films == "боевики":
                print("1.Форсаж  2. Такси 3. Исходный код 4. Кто я 5. Хакер")
                break
            elif action_films == "сериалы":
                print("1.Кремниевая долина  2. Герои 3. Дневники вампира 4. Флэш 5. Сверхестественное")
                break
            else:
                print("вы ввели что то не то")
    elif action == "выйти":
        print("До свидания!")
        break
    else:
        print("вы что писать не умеете??????")
            
print("hello world")
input()



name = 'Восточка'
address = 'ул. Юсупа Абдрахманова д. 212'
phone_number = '+996555555555'
total_table = 2
menu_1 = (('Бощь', 70), ('Щи', 70), ('Солянка', 100))
menu_2 = (('Плов', 150), ('Лагман', 170), ('Пельмени', 150))
menu_3 = (('Пироженное ', 70), ('Мороженное', 70), ('Кулебяка', 500))
menu_4 = (('Кофе', 100), ('Чай', 50), ('Лимонад', 150))
order = []
orders = []
action_2 = ''
status = True
print(f'Мы рады привествовать Вас в нашем кафе "{name}"! Спасибо, что выбарли нас.')
while status == True:


    for b in range(total_table):
        order = []
        while status == True:

            action = input('''
        Нажмите 1 , чтобы выбрать первые блюда.
        Нажмите 2 , чтобы выбрать вторые блюда.
        Нажмите 3 , чтобы выбрать десерт.
        Нажмите 4 , чтобы выбрать напитки.
        Нажмите 5 , чтобы получить чек.
        Нажмите 6 , чтобы выйти.
            ''').strip()
            if action == '1':
                while action_2 != 4:
                    action_2 = input(f'''
                    Введите номер блюда.
                    1 {menu_1[0][0]} - {menu_1[0][1]} сом.
                    2 {menu_1[1][0]} - {menu_1[1][1]} сом.
                    3 {menu_1[2][0]} - {menu_1[2][1]} сом.
                    4 Вернуться в предыдущее меню.
                    ''')
                    if action_2 == '1':
                        print(f'{menu_1[0][0]} - добавлено в ваш заказ.')
                        order.append((menu_1[0][0], menu_1[0][1]))
                        orders.append((menu_1[0][0], menu_1[0][1]))
                    elif action_2 == '2':
                        print(f'{menu_1[1][0]} - добавлено в ваш заказ.')
                        order.append((menu_1[1][0], menu_1[1][1]))
                        orders.append((menu_1[1][0], menu_1[1][1]))
                    elif action_2 == '3':
                        print(f'{menu_1[2][0]} - добавлено в ваш заказ.')
                        order.append((menu_1[2][0], menu_1[2][1]))
                        orders.append((menu_1[2][0], menu_1[2][1]))
                    elif action_2 == '4':
                        break
                    else:
                        print('Такого в меню нет.')
            elif action == '2':
                while action_2 != 4:
                    action_2 = input(f'''
                                Введите номер блюда.
                                1 {menu_2[0][0]} - {menu_2[0][1]} сом.
                                2 {menu_2[1][0]} - {menu_2[1][1]} сом.
                                3 {menu_2[2][0]} - {menu_2[2][1]} сом.
                                4 Вернуться в предыдущее меню.
                                ''')
                    if action_2 == '1':
                        print(f'{menu_2[0][0]} - добавлено в ваш заказ.')
                        order.append((menu_2[0][0], menu_2[0][1]))
                        orders.append((menu_2[0][0], menu_2[0][1]))
                    elif action_2 == '2':
                        print(f'{menu_2[1][0]} - добавлено в ваш заказ.')
                        order.append((menu_2[1][0], menu_2[1][1]))
                        orders.append((menu_2[1][0], menu_2[1][1]))
                    elif action_2 == '3':
                        print(f'{menu_2[2][0]} - добавлено в ваш заказ.')
                        order.append((menu_2[2][0], menu_2[2][1]))
                        orders.append((menu_2[2][0], menu_2[2][1]))
                    elif action_2 == '4':
                        break
                    else:
                        print('Такого в меню нет.')
            elif action == '3':
                while action_2 != 4:
                    action_2 = input(f'''
                                Введите номер блюда.
                                1 {menu_3[0][0]} - {menu_3[0][1]} сом.
                                2 {menu_3[1][0]} - {menu_3[1][1]} сом.
                                3 {menu_3[2][0]} - {menu_3[2][1]} сом.
                                4 Вернуться в предыдущее меню.
                                ''')
                    if action_2 == '1':
                        print(f'{menu_3[0][0]} - добавлено в ваш заказ.')
                        order.append((menu_3[0][0], menu_3[0][1]))
                        orders.append((menu_3[0][0], menu_3[0][1]))
                    elif action_2 == '2':
                        print(f'{menu_3[1][0]} - добавлено в ваш заказ.')
                        order.append((menu_3[1][0], menu_3[1][1]))
                        orders.append((menu_3[1][0], menu_3[1][1]))
                    elif action_2 == '3':
                        print(f'{menu_3[2][0]} - добавлено в ваш заказ.')
                        order.append((menu_3[2][0], menu_3[2][1]))
                        orders.append((menu_3[2][0], menu_3[2][1]))
                    elif action_2 == '4':
                        break
                    else:
                        print('Такого в меню нет.')
            elif action == '4':
                while action_2 != 4:
                    action_2 = input(f'''
                                Введите номер блюда.
                                1 {menu_4[0][0]} - {menu_4[0][1]} сом.
                                2 {menu_4[1][0]} - {menu_4[1][1]} сом.
                                3 {menu_4[2][0]} - {menu_4[2][1]} сом.
                                4 Вернуться в предыдущее меню.
                                ''')
                    if action_2 == '1':
                        print(f'{menu_4[0][0]} - добавлено в ваш заказ.')
                        order.append((menu_4[0][0], menu_4[0][1]))
                        orders.append((menu_4[0][0], menu_4[0][1]))
                    elif action_2 == '2':
                        print(f'{menu_4[1][0]} - добавлено в ваш заказ.')
                        order.append((menu_4[1][0], menu_4[1][1]))
                        orders.append((menu_4[1][0], menu_4[1][1]))
                    elif action_2 == '3':
                        print(f'{menu_4[2][0]} - добавлено в ваш заказ.')
                        order.append((menu_4[2][0], menu_4[2][1]))
                        orders.append((menu_4[2][0], menu_4[2][1]))
                    elif action_2 == '4':
                        break
                    else:
                        print('Такого в меню нет.')
            elif action == '5':
                print(f'''
                          Кафе "{name}"
                          Мы находимся по адресу {address}
                          Наш номер телефона: {phone_number}''')

                print(f'Ваш заказ: {order}')
                total_summ = 0
                for i in order:
                    total_summ += i[1]
                print(f'''Итоговая сумма заказа {total_summ}
Ваш столик {b+1}
Приятного аппетита :)
Осталось {total_table -(b+1)} свобдных толиков''')
                break
            elif action == '6':
                break
            else:
                print('Вы выбрали не верный пункт. Попробуте снова.')
    status = False
print('К сожалению все столики заняты. Мы не можем принять следующий заказ.')




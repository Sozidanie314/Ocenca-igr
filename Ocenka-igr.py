graphics = 0
gameplay = 0
control = 0
sound = 0



mainStart = '''
Поставь оценку четырем характеристике игры!
'''
print(mainStart)



# Графика
graphicsRating = int(input('Оценка графики от 1 до 5: '))
if graphicsRating == 5:
    graphicsRating = 2.5
    graphics = graphicsRating
    print('Вопрос 2 ...')
elif graphicsRating == 4:
    graphicsRating = 2
    graphics = graphicsRating
    print('Вопрос 2 ...')
elif graphicsRating == 3:
    graphicsRating = 1.5
    graphics = graphicsRating
    print('Вопрос 2 ...')
elif graphicsRating == 2:
    graphicsRating = 1
    graphics = graphicsRating
    print('Вопрос 2 ...')
elif graphicsRating == 1:
    graphicsRating = 0.5
    graphics = graphicsRating
    print('Вопрос 2 ...')
else:
    print('Ошибка 100')



# Геймплей
gameplayRating = int(input('Оценка геймплея от 1 до 5: '))
if gameplayRating == 5:
    gameplayRating = 2.5
    gameplay = gameplayRating
    print('Вопрос 3 ...')
elif gameplayRating == 4:
    gameplayRating = 2
    gameplay = gameplayRating
    print('Вопрос 3 ...')
elif gameplayRating == 3:
    gameplayRating = 1.5
    gameplay = gameplayRating
    print('Вопрос 3 ...')
elif gameplayRating == 2:
    gameplayRating = 1
    gameplay = gameplayRating
    print('Вопрос 3 ...')
elif gameplayRating == 1:
    gameplayRating = 0.5
    gameplay = gameplayRating
    print('Вопрос 3 ...')
else:
    print('Ошибка 101')



# Управление
controlRating = int(input('Оценка управления от 1 до 5: '))
if controlRating == 5:
    controlRating = 2.5
    control = controlRating
    print('Вопрос 4 ...')
elif controlRating == 4:
    controlRating = 2
    control = controlRating
    print('Вопрос 4 ...')
elif controlRating == 3:
    controlRating = 1.5
    control = controlRating
    print('Вопрос 4 ...')
elif controlRating == 2:
    controlRating = 1
    control = controlRating
    print('Вопрос 4 ...')
elif controlRating == 1:
    controlRating = 0.5
    control = controlRating
    print('Вопрос 4 ...')
else:
    print('Ошибка 102')



# Звук
soundRating = int(input('Оценка звука от 1 до 5: '))
if soundRating == 5:
    soundRating = 2.5
    sound = soundRating
elif soundRating == 4:
    soundRating = 2
    sound = soundRating
elif soundRating == 3:
    soundRating = 1.5
    sound = soundRating
elif soundRating == 2:
    soundRating = 1
    sound = soundRating
elif soundRating == 1:
    soundRating = 0.5
    sound = soundRating
else:
    print('Ошибка 103')



rez = graphics + gameplay + control + sound
if rez == 10.0: rez = 10
elif rez == 9.0: rez = 9
elif rez == 8.0: rez = 8
elif rez == 7.0: rez = 7
elif rez == 6.0: rez = 6
elif rez == 5.0: rez = 5
elif rez == 4.0: rez = 4
elif rez == 3.0: rez = 3
elif rez == 2.0: rez = 2
    


print(f'Результат оценки игры: {rez}')

# 100 - проблема в цикле: графика
# 101 - проблема в цикле: геймплей
# 102 - проблема в цикле: управление
# 103 - проблема в цикле: звук

while True:
    ex = input('Чтобы выйти пропишите "выход": ')
    if ex == 'выход'.lower(): exit()
    else: print('ошибка ввода.')
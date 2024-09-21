team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Волшебники Данных'
else:
    challenge_result = 'Ничья!'

print('В команде Мастера кода участников: %(team1_num)s!' % {'team1_num': 5})
print('Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s!' % {'team1_num': 5, 'team2_num': 6})
print('Команда Волшебники данных решила задач: {score_2}!'.format(score_2=42))
print('Волшебники данных решили задачи за {team2_time} с !'.format(team2_time=2153.31451))

print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Сегодня было решено {tasks_total} задачи, в среднем по {time_avg} секунды на задачу!.')
print(f'Результат битвы: {challenge_result}!')

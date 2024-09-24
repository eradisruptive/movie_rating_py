﻿# Рейтинг фильмов

Программа для работы с рейтингами фильмов. Она может обрабатывать следующие команды:
add - добавить фильм с указанным названием. Если фильм с таким названием существует, выводит сообщение об ошибке.
delete - удалить фильм с указанным названием. Если фильма с таким названием не существует,  выводит сообщение об ошибке.
list - вывести список фильмов в виде таблицы (название, средний рейтинг). Если у фильма нет рейтингов, выводит вместо рейтинга сообщение, что фильм "не оценивался".

rate - добавить оценку к фильму по названию.
Оценка попадает в интервал от 0 до 10, предполагает, что пользователь вводит только числа.
Если пользователь ввёл оценку 0, удаляет оценку этого пользователя.
Если пользователь с указанным именем уже оценивал этот фильм, замените оценку на новую.

find - найти фильм по названию и показать его название и все оценки в виде таблицы (имя пользователя, оценка) + среднюю оценку. Если у фильма нет рейтингов, выводит сообщение, что фильм "не оценивался".


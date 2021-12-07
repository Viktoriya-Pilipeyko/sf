# 2 ЮНИТ
# Импортируем объект Counter из модуля collections
from collections import Counter
# Создаём пустой объект Counter
c = Counter()
c['red'] += 1
print(c)

# создадим список повторяющихся элементов
cars = ['red', 'blue', 'black', 'black', 'black', 'red', 'blue', 'red', 'white']
# Посчитать значения, конечно, можно и в цикле, используя синтаксис из предыдущего примера:
for car in cars:
    c[car] += 1    
print(c)
# Однако гораздо проще при создании Counter сразу передать в круглых скобках итерируемый объект, 
# в котором необходимо посчитать значения:
c = Counter(cars)
print(c)

# Узнать, сколько раз встретился конкретный элемент, можно, обратившись к счётчику по ключу как к обычному словарю:
print(c['black'])
# Если обратиться к счётчику по несуществующему ключу, то, в отличие от словаря, ошибка KeyError не возникнет:
print(c['purple'])
# Узнать сумму всех значений в объекте Counter можно, воспользовавшись следующей конструкцией:
print(sum(c.values()))

# Допустим, вы с другом из другого города решили посчитать количество цветов встреченных на дороге машин. 
# У вас получились такие списки цветов:
cars_moscow = ['black', 'black', 'white', 'black', 'black', 'white', 'yellow', 'yellow', 'yellow']
cars_spb = ['red', 'black', 'black', 'white', 'white', 'yellow', 'yellow', 'red', 'white']
# Получим для них счётчики:
counter_moscow = Counter(cars_moscow)
counter_spb = Counter(cars_spb)
 
print(counter_moscow)
print(counter_spb)

# Чтобы узнать, сколько машин разных цветов встретилось в двух городах, 
# можно сложить два исходных счётчика и получить новый счётчик:
print(counter_moscow + counter_spb)

# Чтобы узнать разницу между объектами Counter, необходимо воспользоваться функцией subtract, 
# которая меняет тот объект, к которому применяется. В примере выше из значений, посчитанных для Москвы, 
# вычитаются значения, посчитанные для Санкт-Петербурга:
counter_moscow.subtract(counter_spb)
print(counter_moscow)

# Заметьте, что белых машин в counter_spb оказалось больше, чем в counter_moscow, поэтому разность отрицательная. 
# Красных машин в moscow вообще не было, а в spb их оказалось сразу две, поэтому разница равна -2. 
# Значения для black и yellow остались положительными, потому что их было больше.
# К сожалению, функцию subtract не всегда бывает удобно использовать для вычитания, так как модифицируется 
# исходный счётчик. Однако аналога у этой функции нет, поскольку вычитание с помощью оператора "-" приводит 
# к другому результату:
# Пересоздаём счётчики, потому что объект counter_moscow поменял свои значения
# после функции subtract.
counter_moscow = Counter(cars_moscow)
counter_spb = Counter(cars_spb)
 
print(counter_moscow - counter_spb)

# Чтобы получить список всех элементов, которые содержатся в Counter, используется функция elements(). 
# Она возвращает итератор, поэтому, чтобы напечатать все элементы, распакуем их с помощью *:
print(*counter_moscow.elements())

# Чтобы получить список уникальных элементов, достаточно воспользоваться функцией list():
print(list(counter_moscow))

# Функция most_common() позволяет получить список из кортежей элементов в порядке убывания их встречаемости:
print(counter_moscow.most_common())

# В неё также можно передать значение, которое задаёт желаемое число первых наиболее частых элементов, например, 2:
print(counter_moscow.most_common(2))

# Наконец, функция clear() позволяет полностью обнулить счётчик:
counter_moscow.clear()
print(counter_moscow)

# ---------------------------------------------------------------------

# Возможно, вы уже сталкивались с задачей, когда необходимо было создать словарь, 
# в котором по ключам расположены списки. 
# Например, у нас есть список из кортежей с фамилиями студентов и их учебными группами:
students = [('Ivanov',1),('Smirnov',4),('Petrov',3),('Kuznetsova',1),
            ('Nikitina',2),('Markov',3),('Pavlov',2)]
# Сохраним эти данные в словаре, в котором ключами будут номера групп, а элементами — списки студентов. 
# Сделать это можно следующим образом:
groups = dict()
 
for student, group in students:
    # Проверяем, есть ли уже эта группа в словаре
    if group not in groups:
        # Если группы ещё нет в словаре, создаём для неё пустой список
        groups[group] = list()
    groups[group].append(student)
 
print(groups)

# Обратите внимание, что для решения этой задачи нам потребовался шаг с проверкой наличия номера группы в словаре. 
# Если номера группы не было, для этой группы мы создавали новый список в словаре. Без шага проверки мы бы 
# натолкнулись на KeyError

from collections import defaultdict
groups = defaultdict(list)

for student, group in students:
    groups[group].append(student)
 
print(groups)

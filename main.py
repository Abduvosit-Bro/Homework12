#1
print('Камень, ножница и бумага. Правила очень простые. Пишите в поле только первую букву!')

a = input("Введите первую букву: ")
b = input("Введите первую букву: ")

if a == 'к' and b == 'н' or a == 'н' and b == 'к':
    print('Камень выиграл');
elif a == 'к' and b == 'б' or a == 'б' and b == 'к':
    print('Бумага выиграла');
elif a == 'н' and b == 'б' or a == 'б' and b == 'н':
    print('Ножница выиграла');
else:
    print('Ничья')

#2
# names = ['Jonh', 'Rayn', 'Tom', 'James']
names = []
numbers = []
services = []
while True:
    admin = input('Что нужно сделать? Добавить имя; Добавить номер; Добавить услугу; Изменить имя; Удалить имя; ')
    if admin == 'Добавить номер':
        number = input('Введите номер для добавления! ')
        numbers.append(number)
        print('Номер успешно добавлен!')
    elif admin == 'Добавить имя':
        name = input('Введите имя для добавления! ')
        if name in names:
            print('Это имя уже есть')
        else:
            names.append(name)
            print('Имя успешно добавлен!')
    elif admin == 'Добавить услугу':
        service = input('Введите услугу для добавления! ')
        services.append(service)
        print('Услуга успешно добавлена!')
    elif admin == 'Изменить имя':
        if names:
            print(names)
            name_to_edit = input('Выберите имя для изменения ')
            if name_to_edit in names:
                new_name = input('Введите новое значание ')
                names[names.index(name_to_edit)] = new_name
                print('Имя изменено')
            else:
                print('Такого имени нет')
    elif admin == 'Удалить имя':
        if names:
            print(names)
            name_to_delete = input('Выберите имя для удаления ')
            if name_to_delete in names:
                names.remove(name_to_delete)
                print('Имя удалено')
            else:
                print('Такого имени нет')
    else:
        print('Неизвестное действие')

#3
num = [1,2,3,4]
nums = [spam*2 for spam in num]
print(nums)


name = 'Pasha'
n = [x for x in name]
print(n)

print([x for x in 'Pasha'])

numbers = [i for i in range(1, 100)]
print(numbers)


print([i for i in range(100)])

nums = [i for i in range(1, 11)]
chotnie = [num for num in nums if num % 2 == 0]
nechotnie = [num for num in nums if num % 2 != 0]

print(f'{chotnie}\n{nechotnie}')


names = ['Pavel', 'Jordan', 'Sasha']
names2 = [name for name in names if 'o' in name]
print(names2)



names = ['Pavel', 'Sasha', 'Jordan', 'Pasha']
answer = [i[0] for i in names]
print(answer)


nums1 = [i for i in range(1, 21)]
nums2 = [i for i in range(1, 21) if i % 2 == 0]

print(nums1)
print(nums2)

usernames = []

while True:
    user = input('Введите имя ')
    if user in usernames:
        print(f'Такое {user} уже имеется')
    else:
        usernames.append(user)
        print(f'{user} успешно добавлен')

#4
all_products = {'Весь склад': {}}
korzina = []

while True:
    admin = input('Что хотите сделать: ')
    if admin.lower() == 'добавить':
        product_name = input('Введите название продукта ')
        product_count = input('Введите количество ')
        all_products['Весь склад'][product_name] = product_count
        print(f'Добавлено{all_products}')
    elif admin.lower() == 'продукты':
        print(all_products)
    elif admin.lower() == 'купить':
        chto_kupit = input('Введите название продукта ')
        korzina.append(chto_kupit)
        print('Добавлено в корзину')
    elif admin.lower() == 'Удалить':
        chto_udalit = input('Введите название продукта ')
        korzina.remove(chto_udalit)
        print('Удалено')
    elif admin.lower() == 'корзина':
        print(korzina)
    else:
        print('Неизвестная команда')

#5
import datetime as dt
import requests

base_url = 'http://api.openweathermap.org/data/2.5/weather?'
api_key = open('api_key.txt', 'r').read()
city = 'New York'

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

url = base_url + 'appid=' + api_key + '&q=' + city

response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

print(f'Temperature in {city}: {temp_celsius:.2f}C or {temp_fahrenheit:.2f}F')
print(f'Temperature in {city} feels like: {feels_like_celsius:.2f}C or {feels_like_fahrenheit:.2f}F')
print(f'Humidity in {city}: {humidity}%')
print(f'Wind Speed in {city}: {wind_speed}m/s')
print(f'General weather in {city}: {description}')
print(f'Sunrises in {city}: {sunrise_time} local time.')
print(f'Sunsets in {city}: {sunset_time} local time.')

#6
students = {}
opened_class = [i for i in range(1, 11)]
closed_class = []

def add_student(name, class1):
    students[name] = class1
    opened_class.remove(class1)
    closed_class.append(class1)

def delete_student(name):
    opened_class.append(students[name])
    closed_class.remove(students[name])
    students.pop(name)

def show_class():
    return closed_class


while True:
    student_name = input('Введите имя и фамилию ученика для регистарции: ')
    student_choice = int(input('1 - Посметреть классы, 2 - Покинуть класс, 3 - Классы  '))
    if student_choice == 1:
        print(opened_class)
        student_class = int(input('Выберите класс: '))
        add_student(student_name, student_class)
        print('Успешно добавлен')
    elif student_choice == 2:
        if student_name in students:
            delete_student(student_name)
        else:
            print('Вас нет в базе')
    elif student_choice == 3:
        print(show_class())
    else:
        print('Не понял')

#7
class Comment:
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes


user = Comment('Alecco', 'Hello')
print(user.likes)


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

person1 = Person('John', 25, 'Male')
person2 = Person('Sarah', 35, 'Female')
person3 = Person('Bob', 42, 'Male')

print(f'Name: {person1.name}, age: {person1.age}, gender: {person1.gender}')
print(f'Name: {person2.name}, age: {person2.age}, gender: {person2.gender}')
print(f'Name: {person3.name}, age: {person3.age}, gender: {person3.gender}')

#8
class Animal:
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print('Bow bow')


class Cat(Animal):
    def make_sound(self):
        print('Meow')


class Cow(Animal):
    def make_sound(self):
        print('Moo')


dog = Dog()
cat = Cat()
cow = Cow()

dog.make_sound()
cat.make_sound()
cow.make_sound()


class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(self.brand)
        print(self.year)


class Car(Vehicle):
    def __init__(self, brand, year, hp):
        super().__init__(brand, year)
        self.hp = hp

    def display_info(self):
        super().display_info()
        print(self.hp)


class Motorcycle(Vehicle):
    def __init__(self, brand, year, speed):
        super().__init__(brand, year)
        self.speed = speed

    def display_info(self):
        super().display_info()
        print(self.speed)


car = Car('Toyota', 1995, 200)
car.display_info()

motorcycle = Motorcycle('Honda', 2011, 190)
motorcycle.display_info()


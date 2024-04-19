##8
# def adjust_strings(strings):            #Oпределяет максимальную длину строки в списке
#     max_length=max(len(string) for string in strings)  #Возвращает длину самой длинной строки в списке
#     adjusted_strings=[]     
#     for string in strings:
#         adjusted_string=string.ljust(max_length, '_')  
#         adjusted_strings.append(adjusted_string)  
#     return adjusted_strings

# strings_list_1=['крот', 'белка', 'выхухоль']
# strings_list_2=['a', 'aa', 'aaa', 'aaaa', 'aaaaa']
# strings_list_3=['qweasdqweas', 'q', 'rteww', 'ewqqqqq']

# adjusted_strings_1=adjust_strings(strings_list_1)
# adjusted_strings_2=adjust_strings(strings_list_2)
# adjusted_strings_3=adjust_strings(strings_list_3)

# print("Скорректированные строки для первого списка:", adjusted_strings_1)   #Выводит исходные строки и их скорректированные версии для сравнения
# print("Скорректированные строки для второго списка:", adjusted_strings_2)
# print("Скорректированные строки для третьего списка:", adjusted_strings_3)

# ##9
# def is_alpha(name):  #Возвращает True, если все символы в строке являются буквами, и False в противном случае
#     return all(char.isalpha() for char in name)

# def count_vowels_consonants(name):  #Подсчитывает количество гласных и согласных букв в строке 
#     vowels=0
#     consonants=0
#     for char in name:
#         if char.lower() in 'aeiouаеёиоуыэюя':
#             vowels +=1
#         elif char.isalpha():
#             consonants +=1
#     return vowels, consonants

# def print_sorted_letters(name):     #Выводит буквы имени name в алфавитном порядке
#     letters=sorted(set(char.lower() for char in name if char.isalpha()))
#     print("Буквы имени в алфавитном порядке:", ", ".join(letters))

# name=input("Введите ваше имя: ")

# if not is_alpha(name):      #Проверяет, состоит ли строка   name   только из букв
#     print("Имя должно содержать только буквы")
# else:
#     print("Привет,", name.capitalize())

#     count_letters = len(name)
#     print("Количество букв в имени:", count_letters)

#     count_vowels, count_consonants = count_vowels_consonants(name)
#     print("Количество гласных букв:", count_vowels)
#     print("Количество согласных букв:", count_consonants)

#     print_sorted_letters(name)

# ##11

n=int(input("Введите количество букв английского алфавита: "))      #Функция  input  запрашивает у пользователя ввод количества букв английского алфавита 
#Функция  int  преобразует введенное пользователем значение в целое число

alphabet_sequence=[chr(ord('a') + i) for i in range(n)]     #Функция  chr  принимает целое число и возвращает символ с соответствующим ASCII кодом.
#Функция  ord  принимает символ и возвращает его ASCII код    Функция  range  создает последовательность чисел от 0 до n-1, где n - число, переданное в качестве аргумента
print("Последовательность из букв английского алфавита в нижнем регистре:", alphabet_sequence)

repeated_alphabet_sequence=[chr(ord('a') + i)*(i + 1) for i in range(n)]
print("Последовательность из букв английского алфавита, где каждая буква повторяется i раз:", repeated_alphabet_sequence)

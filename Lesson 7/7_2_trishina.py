# Задание 2
# Пользователь вводит с клавиатуры некоторый текст,
# после чего пользователь вводит список зарезервированных
# слов. Необходимо найти в тексте все зарезервированные
# слова и изменить их регистр на верхний. Вывести на
# экран измененный текст.

print("Enter the text:")
text = input()
print("Enter the list of reserved words:")
words = input()
symbol = " "

pozition = 0
for i in range(words.count(symbol)+1):
    num = words[pozition:].find(symbol)

    if num != -1:
        word = words[pozition:pozition+num]
        pozition = num+1
    else:
        word = words[pozition:]

    text = text.replace(word, word.upper())

print(text)


"""
Из предложенного текстового файла (text18-28.txt) вывести на экран его содержимое,
количество символов в тексте. Сформировать новый файл, в который поместить текст в
стихотворной форме предварительно вставив после строки N (N – задается пользователем)
произвольную фразу
"""

with open("text18-28.txt", "r", encoding="utf-16") as f:
    content = f.read()
    print(content)
    print(f'\nКоличество символов в тексте: {len(content)} \n')

N = int(input("Введите номер строки, перед которой нужно вставить фразу '----Произвольная фраза----': "))
with open("text18-28.txt", "r", encoding="utf-16") as f:
    string = f.readlines()
    string.insert(N, '----Произвольная фраза---- \n')

with open("new_file.txt", "w", encoding="utf-16") as f:
    f.writelines(string)

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.


from googletrans import Translator

translator = Translator()

f = open("text_4.txt", "r", encoding="utf-8")
contents = f.read()
result = translator.translate(contents, dest='ru')
print(result.text)
with open("translated.txt", 'w', encoding="utf-8") as f:
    f.write(result.text)
f.close()

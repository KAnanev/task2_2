# это код, который был в презентации к занятию
# вы можете его модифицировать и разобраться, как работают регулярные выражения
import re

text = "Что такое регулярные выражения и как их использовать?" \
       "Говоря простым языком, регулярное выражение — это последовательность символов, " \
       "используемая для поиска и замены текста в строке или файле. Как уже было упомянуто, " \
       "их поддерживает множество языков общего назначения: Python, Perl, R. Так что изучение " \
       "регулярных выражений рано или поздно пригодится."

pattern = "[\w]+"
result = re.findall(pattern, text, re.U)
print(result)

pattern = re.compile("регулярн[а-я]+ выражен[а-я]+")
print("=== re.sub ===")
result = pattern.sub("RegEx", text)
print(result)

print("=== re.split ===")
result = re.split("[.?]", text)
print(result)
print("Всего предложений: {}".format(len(result)))

print("=== re.findall ===")
result = pattern.findall(text)
print(result)

print("=== re.match ===")
print(re.match(pattern, text))
result = re.match("Что", text)
print(result)
print(result.group(0))
print("First: {}, last: {}".format(result.start(), result.end()))
print("=== re.search ===")
print(re.search(pattern, text))

result = pattern.findall(text)
print(result)

# ==========
# пример замены через регулярные выражения. Он пригодится при выполнении ДЗ
# чтобы указать группу, пишите ее номер через бэкслеш, например: r"\3" выберет для вас "(812)"
# протестировать свои регулярки можно на файле, часть которого мы использовали в лекции - смотрите organizations.csv
# ВАЖНО!
# 1) обратите внимания - в регулярках группы (то, что в круглых скобках) нумеруются с 1, а не с 0!
# 2) для того, чтобы работала замена, необходимо перед строкой с выражением замены написать r.
# Например: r"\3". Это знак для python, что \3 - это номер группы, а не какой-то спецсимвол (как \d, например)
test_text = "Заместитель начальника пансионата по административно-хозяйственной деятельности: 8 (812)  432-97-31;"
phone_pattern = "(\+7|8)*(\s*)(\(\d+\))(\s*)(\d+)(-*)(\d+)(-*)(\d+)"
find = re.findall(phone_pattern, test_text)
print(find)
result = re.sub(phone_pattern, r"+7\3\5-\7-\9", test_text)
print(result)

# Если хотите, можете попрактиковать свои навыки, упростив регулярное выражение
# (его можно сократить минимум вдвое минимум двумя способами ;)
# например, вспомните часть лекции про регистр символов
orgname_pattern = "(федеральн[а-яё]*\s|Федеральн[а-яё]*\s)?(государственн[а-яё]*" \
                  "\s|Государственн[а-яё]*\s)?(.*)?(учрежден[а-яё]*\s|Учрежден[а-яё]" \
                  "*\s)(инклюзивн[а-яё]*\s|Инклюзивн[а-яё]*\s)?(дополнит[а-яё]*\s|Дополнит" \
                  "[а-яё]*\s|высше[а-яё]*\s|Высше[а-яё]*\s)(профессиональн[а-яё]*\s|" \
                  "Профессиональн[а-яё]*\s)?(образован[а-яё]*|Образован[а-яё]*)"
# названия вузов для практики:
# 1) федеральное государственное бюджетное образовательное учреждение высшего профессионального
# образования «Московский государственный университет дизайна и технологии»
# 2) Государственное образовательное учреждение высшего образования Московской области
# «Государственный социально-гуманитарный университет»
# описание задачи, примеры регулярок и ссылки на код - в статье https://habr.com/ru/post/301436/

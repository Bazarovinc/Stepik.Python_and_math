import requests as r

n = 100
# How to check your website for Dos attack
list_site = [
    "https://bmstu.ru/",
    "http://fn.bmstu.ru/tm-fs-4",
    "https://bmstu.ru/departments/rl6"
]
code = r.get(list_site[0])
while code == 200:
    print(str(code) + "\t" + "OK")
    code = r.get(list_site[0])

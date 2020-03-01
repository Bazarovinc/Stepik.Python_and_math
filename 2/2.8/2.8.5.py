import os.path as o

fn = input()
if o.isfile(fn) == False:
    if o.isdir(fn) == True:
        print("ERROR:\nЭто каталог, а не файл")
    elif o.isfile(fn) == False and o.isdir(fn) == False:
        print("ERROR:\nФайл не существует")
else:
    with open(fn, 'r') as f_o:
        lines = f_o.readlines()
    print("CONTENT:")
    for line in lines:
        print(line, end='')

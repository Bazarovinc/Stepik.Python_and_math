import os.path as o

if o.isfile(file_name) == True:
    with open(file_name, 'r', encoding="utf-8") as f_o:
        lines = f_o.readlines()
    size = 0
    for line in lines:
        if line != '\n':
            size += 1
    with open(file_name, 'w', encoding="utf-8") as f_o:
        new_event = "event " + str(size + 1) + ' - ' + "'" + event + "'" + '\n'
        f_o.write(new_event)
        for line in lines:
            f_o.write(line)
else:
    with open(file_name, 'w', encoding="utf-8") as f_o:
        new_event = "event " + str(1) + ' - ' + "'" + event + "'" + '\n'
        f_o.write(new_event)
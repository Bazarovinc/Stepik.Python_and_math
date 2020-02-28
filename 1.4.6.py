f_n = "file.txt"
with open(f_n, 'r') as  f_o:
    lines = f_o.readlines()
f_n_w = lines[0]
f_n_r = lines[1].rstrip('\n')
line_number = int(lines[2])
with open(f_n_r, 'r') as f_o_1:
    lines_1 = f_o_1.readlines()
line = lines_1[line_number].lower()
with open(f_n_w, 'a') as f_o_2:
    f_o_2.write(line)

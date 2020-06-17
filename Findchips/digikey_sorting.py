with open('723digikey.csv') as f:
    part_no_list = f.readlines()
part_no_list =[x.strip() for x in part_no_list]

LST= []
for i in part_no_list[1:]:
    a = i.split('|')
    p = a[3:]
    if p[-1] =='':
        p.pop()
    else: pass
    p.reverse()
    for i in range(0,100,2):
        if i < len(p):
            p[i+1],p[i] = p[i],p[i+1]
        else:pass
    ap = a[0:3] + p
    LST.append(ap)

y = open('correct_version_digikey.csv', 'a', encoding='utf-8')
csv_column_name = ['Part Number', 'Manufacturer Part Number', 'Stock', 'Price']
y.write("|".join(csv_column_name))
y.write('\n')
for row in LST:
    y.write("|".join(row))
    y.write('\n')
y.close()
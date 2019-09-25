# log file reading and extract  some desired  data
f1 = open('out3.txt', 'w')
f2 = open('out4.csv', 'w')

f1.write('IP \t date  \t pics  \t url \n')
f2.writelines(['IP,', 'Date,', 'Pics,', 'Url\n'])

f3 = open(r'D:\Python Dev\training\log\server.txt')

for line in f3:
    if line[:3].isdigit():
        # print(line)
        sp = line.split()
        print(sp)
        ip = sp[0]
        # print(ip)
        dt = sp[3]
        dt = dt.split(':')
        # print(dt)
        dt = dt[0]
        d1 = dt.lstrip('[')
        d2 = dt.replace('[', '')
        d3 = dt[1:]
        # if sp[6].startswith('/pics')
        # if sp[6][:5] == '/pics'
        if 'pics' in sp[6].split('/'):
            im = sp[6].split('/')
            im = im[-1]
        else:
            im = 'no image'
        print(im)
        url = sp[10]
        print(ip, d1, im, url, sep='\t', file=f1)
        print(ip, d1, im, url, sep=',', file=f2)
f1.close()
f2.close()
f3.close()

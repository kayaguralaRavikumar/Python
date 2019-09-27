import sqlite3
import re
import urllib.request as u

con = sqlite3.connect('mydb.sqlite3')
# import  pymysql
# con = pymysql.connect(host = '', port ='' , user ='' ,passwod='',db='')
cur = con.cursor()
query = '''CREATE TABLE IF NOT EXISTS LOGDATA(
            IP VARCHAR(100),
            DATE VARCHAR(100),
            PICS VARCHAR(100),
            URL VARCHAR(100)
            )'''
cur.execute(query)

myurl = 'https://www.jafsoft.com/searchengines/log_sample.html'

f = u.urlopen(myurl)

# regex  values
'''
\d --> digit
\D --> non digit
. --> any character \. to use strict  or [.]
{} -->  quantifier
[0-9] --> \d
modifiers - will work with combination of pattern
* --> 0  or more
+ --> 1 or more
? --> 0 or one
* --> only  *
\d* ---> now *  have value
\s --> space
\S --> non-space
\w --> word collect [0-9a-zA-Z_]
\W --> non word [^0-9a-zA-Z_]
^  --> matter when put first  , end  it will be same ^
r[ea]{2}d
r[ea]+d
r[ea]*d
r[ea]?d
greed operator
'''

for line in f:
    # print(line)
    # print(type(line))
    line = line.decode()
    # print(type(line))
    # m= re.match('[0-9]{3}\.[0-9]{3}\.[0-9]{3}\.[0-9]{3}',line)
    # m = re.m
    # atch('[0-9][0-9][0-9]\.[0-9]{3}[.][0-9]{1,3}\.[0-9]{3}*', line)
    m = re.match(
        '(\d\d\d\.\d{3}[.]\d{3}[.][0-9]{3}).*?(\d{1,2}/[A-Za-z]{3}/\d{4}).*GET\s+/(pics/(\w+\.\w+))?.*(http[s]?://\S+)</A>.*',line)
    # print(m)
    if m != None:
        ip = m.group(1)
        dt = m.group(2)
        im = m.group(4)
        url = m.group(5)
        if im == None:
            im = 'no image'
        print(ip, dt, im, url)
        query  = f"insert into LOGDATA values ('{ip}' , '{dt}','{im}','{url}') "
        cur.execute(query)
con.commit()
cur.execute('select * from logdata')
result  = cur.fetchall()
print('result=',result)

import  csv
f = open('dbdump.csv','w',newline='')
wt = csv.writer(f)
wt.writerow(['IP','Date','pics','Url'])
for line in result :
    wt.writerow(line)
f.close()

import pandas as pd

l1 = [[10, 20, 30], [40, 50, 60]]
l2 = list([[10, 20, 30], [40, 50, 60]])
df1 = pd.DataFrame([[10, 20, 30], [40, 50, 60]], index=['r1', 'r2'], columns=['c1', 'c2', 'c3'])
print(l1, l2, df1, sep='\n')

df2 = pd.DataFrame(result)
df2.to_csv('out5.csv',index=None,header=['Ip', 'Date', 'pics', 'URL'])
df2.to_excel('outp6.xlsx')
df2.to_json('out7.json')
cur.execute('select * from logdata')
df3 = pd.DataFrame(cur)
df3.to_csv('out8.csv')
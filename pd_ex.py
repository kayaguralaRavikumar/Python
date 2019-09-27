import pandas as  pd

df = pd.read_csv('out5.csv')
# print(df)

# df1 = df.head(5)
# print(df1)
# df2 = df.tail(5)
# print(df2)
# df3 = df.describe()
# print(df3)
# df4 = df['ID'].describe()
# print(df4)
# df5 = df['pics'].describe()
# print(df5)
# print(df['pics'].count())
# df6 = df['pics'].value_counts()
# print(df6)
#
# import matplotlib.pyplot as plt
# df6.plot()
# plt.show()
# df6.plot.bar()
# plt.savefig('graph.png')
#
# writer = pd.ExcelWriter('myreport.xlsx',engine='xlsxwriter')
# df6.to_excel(writer,sheet_name='DATA')
# wb= writer.book
# ws= wb.add_worksheet('graph')
# ws.insert_image('B2','graph.png')
# writer.close()

# df7 = df[df['ID']>10]
# print(df7)
#
# df8 = df[df['ID']==df['ID'].max()]
# print(df8)
# df9 = df[df['pics'].str.endswith('jpg')]
# print(df9)
df10 = df.groupby(['pics']).count()
print(df10)

df11 = df.iloc[1, 1]  # index location
df12 = df.iloc[1]  # 1 rows only
df13 = df.iloc[:, 1]  # all rows
df14 = df.iloc[1:10]  # 1 to 10 rows  only
df15 = df.iloc[1:10, ::2]  # 1 to 10 rows , cloumns  step by 2
df16 = df.iloc[[1, 3, 5]]  # 1,3,5 rows
df17 = df.iloc[[1, 3, 5], [1, 3]] # 1,3,5 rows 1,3 Columns


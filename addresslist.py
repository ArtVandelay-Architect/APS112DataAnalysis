import pandas as pd

def search(df,st):
    for i in range(len(df)):
        if (df['col 1'][i] == st):
            return i
    return -1


df = pd.read_excel("./Final.xlsx")
df.head(3)

df2 = pd.DataFrame(columns=['col 1', 'col 2'],index=range(15000))



cols = ['Delivery Number','Street Name',]

raw = df[cols]

dold = 0

c = 0

for i in range(len(raw)):
    if (i % 100 == 0):
        print(i)
    
    dnum = raw['Delivery Number'][i]
    if (dnum != dold):
        dold = dnum
        dest = raw['Street Name'][i]
        loc = search(df2,dest)
        if (loc == -1):
            c += 1
            df2['col 1'][c] = dest
            df2['col 2'][c] = 1
        else:
            df2['col 2'][loc] += 1

df2.to_excel("output.xlsx")


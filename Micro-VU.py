# -*- coding: utf-8 -*-

# Micro-VU 数据导出

# 这个程序需要删除 txt 中的 ':BEGIN', ':END'

def Save_to_Desktop(datalist, dataframe):
    import pandas as pd
    import os
    Path = os.path.join(os.path.expanduser("~"),'Desktop')+'\\results.csv'
    AddFrame = pd.DataFrame(datalist, columns = dataframe)
    AddFrame.to_csv(Path,index = False)

def Sorting(filename):
    import os
    Path = os.path.join(os.path.expanduser("~"),'Desktop')+'\\'+str(filename)+'.txt'
    from pandas import read_csv
    data = read_csv(Path, sep='\t', header=None)
    x = data.iloc[:,0]
    y = data.iloc[:,1]
    LeftTop = []
    LeftBottom = []
    RightTop = []
    RightBottom = []
    BBWidth =[]
    Space =[]
    Width = []
    dlist=[]
    
    for i in range(0,len(x)):
        if x[i]=='LeftTop':
            LeftTop.append(y[i])
        elif x[i]=='RightTop':
            RightTop.append(y[i])
        elif x[i]=='RightBottom':
            RightBottom.append(y[i])
        elif x[i]=='LeftBottom':
            LeftBottom.append(y[i])
        elif x[i]=='BBWidth':
            BBWidth.append(y[i])
        elif x[i]=='Space':
            Space.append(y[i])
        elif x[i]=='Width':
            Width.append(y[i])
    
    for i in range(0,len(LeftTop)):
        if Space==[]:
            Space = ['NA']*len(LeftTop)
        if Width==[]:
            Width = ['NA']*len(LeftTop)
        temp=[LeftTop[i], RightTop[i], RightBottom[i], LeftBottom[i], BBWidth[i],\
              Space[i], Width[i]]
        dlist.append(temp)
      
    frame =['LeftTop','RightTop','RightBottom','LeftBottom','BBWidth',\
            'Space','Width']
    
    Save_to_Desktop(dlist, frame)

# ============= 主程序部分=====================================================

# 计时开始
import time
t1 = time.perf_counter()

Sorting('rear')
#Sorting('front')

# 计时结束
t2 = time.perf_counter()
print("Time Cost = ",(t2-t1),"s")
# ============================================================================




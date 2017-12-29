# Shantanu singh
import pandas as pd
import re
xl = pd.ExcelFile("Book1.xlsx")
df=xl.parse('Sheet1')

length=df['values'].size
point={17:['chair'],14:['vice chair'],10:['director'],12:['best delegate','best del'],8:['high commendation','high comm'],6:['special mention','spec men','specmen'],4:['hon men','honorable mention','honmen'],2:['verbal mention'],0.1:['america','usa','united states of america','russia','ussr','russian fedration']}
value=point.keys()
prize=point.values()
finallist=[]
for i in range(0,length):
    exp=df['values'][i].lower()#reading experiance of delegate one at a time
    score=0
    length=len(exp)*.05
    score=score+length;
    for j in point:
        temp=point[j]
        for k in temp:#exact charcter to be matched
            value=re.findall(k,exp)
            if(value!=None):
                count=len(value)
                score=score+count*j
    finallist.append(score)
print(finallist)

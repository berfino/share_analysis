import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def maxProfit(price, start, end):
 
     if (end <= start):
         return 0;
 
     profit = 0;
 
     for i in range(start, end, 1):
                
         for j in range(i+1, end+1):
            
             if (price[j] > price[i]):
                #  print(price[i],price[j])
              
                 curr_profit = price[j] - price[i] +maxProfit(price,start, i - 1)+maxProfit(price,j + 1, end);
 
                
                 profit = max(profit, curr_profit);
 
     return profit;
 
     
excelPath=r'C:\Users\kagan\Desktop\Desktop\School Documents\algorithms\shareAnalysis\share_analysis\AnadoluEFEStumhisse.xlsx'
excelFile = pd.read_excel(excelPath,sheet_name="isyatirim")

tarih=excelFile['Tarih']
price=excelFile['Kapanis(TL)']

minIndex=np.argmin(price)#Minumum değere sahip anının indexi
maxIndex=np.argmax(price)#Maximum değere sahip anının indexi
# print("Original array: ",price)
print("Minimum Values: ",minIndex,"\nMaximum Values: ",maxIndex)

max_element = np.max(price) #price arrayinin içindeki en büyük sayıyı buluyor
min_element = np.min(price) #price arrayinin içindeki en küçük sayıyı buluyor
print('minimum element in the array is: ', min_element,'\nmaximum element in the array is: ', max_element)
print("Kapanış değerine göre ,\nŞu tarihte Al:",tarih[minIndex],"\nŞu Tarihte Sat:",tarih[maxIndex])

indexes=price[minIndex : maxIndex+1]#kar maksimizasyonu uygulanmış arrayı tanımlıyoruz.
print('SubArray=>\n',indexes)

dates = tarih[minIndex : maxIndex+1]

plt.plot(tarih,price,label = "Share Graph")
plt.plot(dates,indexes, label = "Profit Maximization", color = 'red')
plt.xlabel("tarih")
plt.ylabel("price")
plt.legend()
# plt.figure(tarih,price)
plt.show()
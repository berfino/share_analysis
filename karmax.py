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
                 print(price[i],price[j])
              
                 curr_profit = price[j] - price[i] +maxProfit(price,start, i - 1)+maxProfit(price,j + 1, end);
 
                
                 profit = max(profit, curr_profit);
 
     return profit;
 
     
excelPath=r'C:\Users\Ufuk\Desktop\Berfin Works\PythonWorks\KaganVeri\AnadoluEFEStumhisse.xlsx'
excelFile = pd.read_excel(excelPath,sheet_name="isyatirim")

tarih=excelFile['Tarih']
price=excelFile['Kapanis(TL)']


print("Original array: ",price)
print("Maximum Values: ",np.argmax(price))
print("Minimum Values: ",np.argmin(price))

max_element = np.max(price)
min_element = np.min(price)

print('maximum element in the array is: ',
      max_element)
print('minimum element in the array is: ',
      min_element)
indexes = price[np.argmin(price) : np.argmax(price)+1]
print(indexes)
dates = tarih[np.argmin(price) : np.argmax(price)+1]

plt.plot(tarih,price,label = "Share Graph")
plt.plot(dates,indexes, label = "Profit Maximization", color = 'red')
plt.xlabel("tarih")
plt.ylabel("price")
plt.legend()
# plt.figure(tarih,price)
plt.show()
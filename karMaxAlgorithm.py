import pandas as pd
import matplotlib.pyplot as plt

def maxProfit(arr,len):
    i=0
    minIndex=0
    maxIndex=0
    profit=0
    tempProfit=0
    while i<len:

        j=i+1
        while j<len:
            tempProfit=arr[j]-arr[i]
            if(tempProfit>profit):
                profit=tempProfit
                minIndex=i
                maxIndex=j

            j+=1    
        i+=1
        

    return minIndex,maxIndex,profit

excelPath=r'C:\Users\kagan\Desktop\Desktop\School Documents\algorithms\shareAnalysis\share_analysis\AnadoluEFEStumhisse.xlsx'
excelFile = pd.read_excel(excelPath,sheet_name="isyatirim")

tarih=excelFile['Tarih']
price=excelFile['Kapanis(TL)']


# print(price)
len=len(price)
minIndex,maxIndex,profit=maxProfit(price,len)

dates=tarih[minIndex:maxIndex+1]
indexes=price[minIndex:maxIndex+1]
print("Buy on Day:",tarih[minIndex],"\nSell on Day:",tarih[maxIndex],"\nYour Profit:",profit)
# print(indexes)

plt.plot(tarih,price,label = "Share Graph")
plt.plot(dates,indexes, label = "Profit Maximization", color = 'red')
plt.xlabel("tarih")
plt.ylabel("price")
plt.legend()
# plt.figure(tarih,price)
plt.show()
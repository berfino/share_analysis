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

efesPath=r'./AnadoluEFES2022.xlsx' #Enter the file name of the data set to be processed in excel format.
efesFile = pd.read_excel(efesPath,sheet_name="isyatirim")


date=efesFile['Tarih']
price=efesFile['Kapanış(TL)']



len=len(price)
minIndex,maxIndex,profit=maxProfit(price,len)

dates=date[minIndex:maxIndex+1]
indexes=price[minIndex:maxIndex+1]
print("Buy on Day:",date[minIndex],"\nSell on Day:",date[maxIndex],"\nYour Profit:",profit)
print("Start Index:",minIndex,"-- End Index:",maxIndex)
print("Start Index Value:",price[minIndex],"-- End Index Value:",price[maxIndex])

plt.plot(date,price,label = "Share Graph")
plt.plot(dates,indexes, label = "Profit Maximization", color = 'red',linestyle = 'dashed')
plt.xlabel("tarih")
plt.ylabel("price")
plt.legend()
# plt.figure(tarih,price)
plt.show()
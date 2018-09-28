import pandas as pd
import matplotlib.pyplot as plt
# for export 14-15
data_frame1 = pd.read_csv('/home/nimesh/My-Files/Study/Semester 3rd/DW/DW Project/Gurkiran/Export_2014_15.csv')
data_frame2=data_frame1.groupby('pc_description').agg({'value':sum})
data_frame3=data_frame2.sort_values(by=['value'],ascending=False)
data_frame3=data_frame3.reset_index()
arr=[]
arr2=[]
arr=data_frame3['pc_description']
arr2=data_frame3['value']
arr=arr[:20]
arr2=arr2[:20]


plt.bar(arr,arr2, align='center', alpha=0.5)
plt.xlabel('Product')
plt.ylabel('Price in Million dollars')
plt.xticks(arr,rotation='vertical')

# for export-15-16
data_frame4 = pd.read_csv('/home/nimesh/My-Files/Study/Semester 3rd/DW/DW Project/Gurkiran/Export_2015_16.csv')
data_frame5=data_frame4.groupby('pc_description').agg({'value':sum})
data_frame6=data_frame5.sort_values(by=['value'],ascending=False)
data_frame6=data_frame6.reset_index()
arr=[]
arr2=[]
arr=data_frame6['pc_description']
arr2=data_frame6['value']
arr=arr[:20]
arr2=arr2[:20]


plt.bar(arr,arr2, align='center', alpha=0.5)
plt.xlabel('Product')
plt.ylabel('Price in Million dollars')
plt.xticks(arr,rotation='vertical')

#for export 16-17

data_frame7 = pd.read_csv('/home/nimesh/My-Files/Study/Semester 3rd/DW/DW Project/Gurkiran/Export_2016_17.csv')
data_frame8=data_frame7.groupby('pc_description').agg({'value':sum})
data_frame9=data_frame8.sort_values(by=['value'],ascending=False)
data_frame9=data_frame9.reset_index()
arr=[]
arr2=[]
arr=data_frame9['pc_description']
arr2=data_frame9['value']
arr=arr[:20]
arr2=arr2[:20]


plt.bar(arr,arr2, align='center', alpha=0.5)
plt.xlabel('Product')
plt.ylabel('Price in Million dollars')
plt.xticks(arr,rotation='vertical')

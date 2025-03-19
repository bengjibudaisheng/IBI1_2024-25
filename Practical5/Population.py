# import matplotlib.pyplot to create graghs
import matplotlib.pyplot as plt

# store country/province and population into dictionary
UK={'England':57.11,'Wales':3.13,'Northern Ireland':1.91,'Scotland':5.45}
CN={'Zhejiang':65.77,'Fujian':41.88,'Jiangxi':45.28,'Anhui':61.27,'Jiangsu':85.15}

# create two lists storing given values
uk_countries=list(UK.values())
cn_provinces=list(CN.values())

# sort values and print two lists of sorted values
uk_countries.sort()
cn_provinces.sort()
print(uk_countries,cn_provinces)

# create pie graghs and set the distributions, labels and colors
colors1=['pink','brown','gray','cyan']
plt.pie(list(UK.values()),labels=list(UK.keys()),colors=colors1,autopct='%1.1f%%')
plt.show()
colors2=['red','orange','yellow','green','blue']
plt.pie(list(CN.values()),labels=list(CN.keys()),colors=colors2,autopct='%1.1f%%')
plt.show()
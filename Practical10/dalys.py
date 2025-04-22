# Import some python libraries.
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Import the .csv file.
dalys_data=pd.read_csv("dalys-rate-from-all-causes.csv")

# This code is used to show the third column for the first ten rows.
print(dalys_data.iloc[0:10,2])

# This code is used to show the DALYs for all countries in 1990.
print(dalys_data.loc[dalys_data.Year==1990,'DALYs'])

# Make two objects to store the data from the United Kingdom and France.
uk=dalys_data.loc[dalys_data.Entity=='United Kingdom',['DALYs','Year']]
fr=dalys_data.loc[dalys_data.Entity=='France',['DALYs','Year']]

# Use the describe function to computed the mean DALYs in the UK and France.
uk_dalys=uk.describe()
uk_mean=uk_dalys.loc['mean','DALYs']
fr_dalys=fr.describe()
fr_mean=fr_dalys.loc['mean','DALYs']

# This part of code is used to state whether the mean DALYs in the UK was greater or smaller than France.
if uk_mean>=fr_mean:
    print('The mean DALYs in the UK was greater than France.')
elif uk_mean<=fr_mean:
    print('The mean DALYs in the UK was smaller than France.')
else:
    print('The mean DALYs in the UK was as same as France.')

#  Create a plot showing the DALYS over time in the UK.
plt.plot(uk.Year,uk.DALYs,'b+')
plt.title('the DALYS over time in the UK')
plt.ylabel('DALYs')
plt.xticks(uk.Year,rotation=90)
plt.show()

country=dalys_data.loc[dalys_data.DALYs>=650000,'Entity']
print(country)
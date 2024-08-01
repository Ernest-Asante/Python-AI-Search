import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "SSN": [123, 445, 511, 872],
    "Name": ["Anna", "Bob", "Jobs", "Mike"],
    "Age" : [29, 43, 82, 23],
    "Height": [176, 165, 187, 182],
    "Gender": ["f", "m", "m", "m"]
}

df = pd.DataFrame(data)
df.set_index("SSN", inplace=True)

df.sort_index(inplace=True)
print(df)

df.sort_values(by=['Name', 'Age'], inplace=True)
print(df)
#print(df.count())
#print(df['Height'].mean())
#print(df['Height'].std())
#print(df['Height'].describe())
#print(df['Height'].apply(np.sin))

#for x in df:
#    print(x)

#sorting


#df.hist()
#plt.show()  
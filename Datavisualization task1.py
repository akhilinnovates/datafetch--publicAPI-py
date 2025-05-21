#required packages
import matplotlib.pyplot as plt
import pandas as pd
import numpy as ny

#required data
x=[1,2,3,4]
y=[100,209,400,300]

#basic line chart 
plt.plot(x,y)
plt.title("Basic line chart of the provided data")
plt.xlabel("month")
plt.ylabel("purchase")
plt.show()


print(plt.style.available)    #to check available styles

#to add data in jupyter notebook

import pandas as pd
data={
    'WEATHER':["sunny","partial rainy","cloudy","heavly rainimg"],
    'RAIN level':[1,2,3,4],
    'HUMIDITY':[45,7,6,76]
}
res=pd.DataFrame(data)

print("student Records\n\n",res)


x=["sunny","partial rainy","cloudy","heavely raining", font="arial"]
y=[45,7,6,67]
#visualization of data
plt.plot(x,y)
plt.title("WEATHER DATA",)
plt.xlabel("weather condition")
plt.ylabel("humidity")
plt.show()

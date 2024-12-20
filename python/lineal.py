# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 
# dataset = pandas.DataFrame(linearfunc_intercept, linearfunc_maskederror)
# dataset = dataset.drop_duplicates()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df= dataset
df.sort_values(by=["time"], inplace=True)
df.reset_index(inplace=True)

def linearfunc(time, slope, intercept):
    return slope * time + intercept

def plot(domain, range, parameters=None, size=(8,4), scatter = 5, add_margins=True, step_length=0.1, color = "red"):
    plt.style.use('dark_background')
    plt.figure(figsize=size)

    if add_margins:
        start_point = domain[0] -1
        end_point = domain[-1] + 1
    else:
        start_point = domain[0]
        end_point = domain[-1]
    x = np.arange(start_point, end_point, step_length)

    y = linearfunc(x, *parameters)
    
    plt.scatter(domain, range, s = scatter)
    plt.ylabel("Luminosidad (flux)", size = 12)
    plt.xlabel("Tiempo (medido en días terrestres)", size = 12)
    plt.plot(x, y, color = color, linewidth = 3)
    
    plt.show()
    

time = list(df["time"])
flux = list(df["flux"])
slope = df["linearfunc_slope"][0]
intercept = df["linearfunc_intercept"][0]
prediction = list((slope, intercept))
plot(time, flux, prediction)
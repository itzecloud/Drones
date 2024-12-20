# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 
# dataset = pandas.DataFrame(linearfunc_intercept, linearfunc_maskederror)
# dataset = dataset.drop_duplicates()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df= dataset
df.sort_values(by=["time"], inplace=True)
df.reset_index(inplace=True)

def trig(x, a, b, c):
    return a * np.sin(b * x + c)

def ntrigs(time, mean, *params):
    result = mean
    for i in range(0, len(params), 3):
        result += trig(time, params[i], params[i+1], params[i+2])
    return result

def plot(domain, range, mean, parameters=None, size=(8,4), scatter = 5, add_margins=True, step_length=0.1, color = "white"):
    plt.style.use('dark_background')
    plt.figure(figsize=size)

    if add_margins:
        start_point = domain[0] -1
        end_point = domain[-1] + 1
    else:
        start_point = domain[0]
        end_point = domain[-1]
    x = np.arange(start_point, end_point, step_length)

    y = ntrigs(x, mean, *parameters)
    
    plt.scatter(domain, range, s = scatter)
    plt.ylabel("Luminosidad (flux)", size = 12)
    plt.xlabel("Tiempo (medido en días terrestres)", size = 12)
    plt.plot(x, y, color = color, linewidth = 3)
    
    plt.show()
    

time = list(df["time"])
flux = list(df["flux"])
mean = df["threetrigs_mean"][0]
amplitude1 = df["threetrigs_amplitude1"][0]
amplitude2 = df["threetrigs_amplitude2"][0]
amplitude3 = df["threetrigs_amplitude3"][0]
frequency1 = df["threetrigs_frequency1"][0]
frequency2 = df["threetrigs_frequency2"][0]
frequency3 = df["threetrigs_frequency3"][0]
hshift1 = df["threetrigs_hshift1"][0]
hshift2 = df["threetrigs_hshift2"][0]
hshift3 = df["threetrigs_hshift3"][0]
prediction = list((amplitude1, frequency1, hshift1, amplitude2, frequency2, hshift2, amplitude3, frequency3, hshift3))
plot(time, flux, mean, prediction)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = dataset
df.sort_values(by=['object', 'time'], inplace=True)

sample_data = df.head(20) # Create a table plot 
fig, ax = plt.subplots(figsize=(10, 6)) 
ax.axis('tight') 
ax.axis('off') 
table = ax.table(cellText=sample_data.values, colLabels=sample_data.columns, cellLoc='center', loc='center')
intercept = df["linearfunc_slope"][0]
plt.title(intercept)
plt.show()
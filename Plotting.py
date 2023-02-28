# Pandas uses the plot() method to create diagrams.

import pandas as pd
# We can use Pyplot, a submodule of the Matplotlib library to visualize the diagram on the screen.
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot()

plt.show()
# if you want a scatter plot:
df.plot(kind='scatter', x='Duration', y='Calories')

plt.show()

# A histogram shows us the frequency of each interval, e.g. how many workouts lasted between 50 and 60 minutes?
df["Duration"].plot(kind='hist')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader
import datetime
import pandas_datareader.data as web
from pandas.plotting import autocorrelation_plot
# %matplotlib inline

amazon = web.DataReader("AMZN", 'av-daily-adjusted', start=datetime.datetime(1999, 1, 1), end=datetime.datetime(2019, 11, 4), api_key = "RWBEQKLG65YPF62U")

amazon['open'].plot(label="Open")
amazon['close'].plot(label="Close")
amazon['high'].plot(label="High", figsize=(30, 10))
amazon['low'].plot(label="Low")
plt.legend()

plt.show()

# Website for the API: https://alpha-vantage.readthedocs.io/en/latest/

from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
import matplotlib.pyplot as plt


# To print the data
ts = TimeSeries(key='RWBEQKLG65YPF62U')
data, meta_data = ts.get_daily(symbol='MSFT')
pprint(data);

# To plot the data
ti = TechIndicators(key='RWBEQKLG65YPF62U', output_format='pandas') # API Key: RWBEQKLG65YPF62U
data, meta_data = ti.get_bbands(symbol='MSFT', interval='60min', time_period=60)

data.plot()
plt.title('BBbands indicator for  MSFT stock (60 min)')
plt.show()
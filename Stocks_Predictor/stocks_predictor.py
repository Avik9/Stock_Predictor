# Website for the API: https://alpha-vantage.readthedocs.io/en/latest/
# API Key: RWBEQKLG65YPF62U

from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
import matplotlib.pyplot as plt

listOfCompanies = [
    'APPL',  # Apple
    'MSFT',  # Microsoft
    'GOOG',  # Google
    'INTL',  # Intel
    'AMZN',  # Amazon
    'FB',    # Facebook
    'BRK-B', # Berkshire Hathaway
    'BABA',  # Alibaba
    'JNJ',   # Johnson & Johnson
    'JPM',   # JPMorgan Chase
    'XOM',   # Exxon Mobile
    'BAC',   # Bank of America
    'WMT',   # Wal-Mart
    'WFC',   # Wells Fargo
    'RDS-B', # Royal Dutch Shell
    'V',     # Visa
    'PG',    # Procter & Gamble
    'BUD',   # Anheuser-Busch Inbev
    'T',     # AT&T 
    'CVX'    # Chevron Corporation
    'UNH '   # UnitedHealth Group
    'PFE',   # Pfizer Inc.
    'RHHBY', # Roche Holding
    'CHL',   # China Mobile
    'HD',    # Home Depot
    'TSM',   # Taiwan Semiconductor
    'VZ',    # Verizon
    'ORCL',  # Oracle
    'C',     # Citigroup
    'NVS',    # Novartis
]

ts = TimeSeries(key='RWBEQKLG65YPF62U')
counter = 0

for company in listOfCompanies:
    try:
        # To print the data
        print('This is the data for ' + company)
        data, meta_data = ts.get_daily(symbol = company)
        pprint(data)

        # To plot the data
        # ti = TechIndicators(key='RWBEQKLG65YPF62U', output_format='pandas') # API Key: RWBEQKLG65YPF62U
        # data, meta_data = ti.get_bbands(symbol = company, interval='60min', time_period=60)

        # data.plot()
        # plt.title('BBbands indicator for ' + company + ' stock (60 min)')
        # plt.show()


    except:
        print('The data for ' + company + ' did not load')
        counter += 1

print(counter, "companies out of", len(listOfCompanies), "companies' data was not retrieved")

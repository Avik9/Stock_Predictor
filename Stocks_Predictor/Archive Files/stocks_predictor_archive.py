# Website for the API: https://alpha-vantage.readthedocs.io/en/latest/
# API Key: RWBEQKLG65YPF62U

# importing the dependencies 
import tensorflow as tf 
import numpy as np 
import matplotlib.pyplot as plt 
import pandas

from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.timeseries import TimeSeries
from pprint import pprint

listOfCompanies = [
    # 'APPL',  # Apple
    # 'COF',   # Capital One Bank
    # 'MSFT',  # Microsoft
    # 'NFLX',  # Netflix
    # 'GOOG',  # Google
    # 'INTC',  # Intel
    'AMZN',  # Amazon
    # 'FB',    # Facebook
    # 'GS',    # Goldman Sachs
    # 'TSLA',  # Tesla

    # 'BRK-B', # Berkshire Hathaway
    # 'BABA',  # Alibaba
    # 'JNJ',   # Johnson & Johnson
    # 'JPM',   # JPMorgan Chase
    # 'XOM',   # Exxon Mobile
    # 'BAC',   # Bank of America
    # 'WMT',   # Wal-Mart
    # 'WFC',   # Wells Fargo
    # 'RDS-B', # Royal Dutch Shell
    # 'V',     # Visa
    # 'PG',    # Procter & Gamble
    # 'BUD',   # Anheuser-Busch Inbev
    # 'T',     # AT&T 
    # 'CVX'    # Chevron Corporation
    # 'UNH '   # UnitedHealth Group
    # 'PFE',   # Pfizer Inc.
    # 'RHHBY', # Roche Holding
    # 'CHL',   # China Mobile
    # 'HD',    # Home Depot
    # 'TSM',   # Taiwan Semiconductor
    # 'VZ',    # Verizon
    # 'ORCL',  # Oracle
    # 'C',     # Citigroup
    # 'NVS',   # Novartis
]

for company in listOfCompanies:
    dates_data = []
    open_data = []
    high_data = []
    low_data = []
    close_data = []

    try:
        # Opening the file
        with open('Stock_Data/' + 'AMZN' + ".csv") as company_data:
            companyData = pandas.read_csv(company_data, delimiter=',')
            ax = plt.gca()
            companyData.plot(kind='line',x='Date',y='Open',ax=ax)
            companyData.plot(kind='line',x='Date',y='High',ax=ax)
            companyData.plot(kind='line',x='Date',y='Low',ax=ax)
            companyData.plot(kind='line',x='Date',y='Close',ax=ax)

            plt.show()
            
    except:
        print(company + " could not be loaded.")
        continue

    # y = dates_data[1::]

    # x1 = open_data[1::]
    # plt.plot(x1, y, label = "Open Prices")

    # # x4 = close_data[1::]
    # # plt.plot(x4, y, label = "Close Prices")

    # # naming the x axis 
    # plt.xlabel('Prices')

    # # naming the y axis 
    # plt.ylabel('Time')

    # # giving a title to my graph 
    # plt.title('Four lines on same graph!')

    # # show a legend on the plot 
    # # plt.legend() 
    
    # # function to show the plot 
    # plt.show() 









# WORKING WITH THE API (Later Stage of the project)

# ts = TimeSeries(key='RWBEQKLG65YPF62U', output_format='pandas')
# counter = 0

# listOfCompanies = ['AMZN']

# for company in listOfCompanies:
#     try:
#         # To print the data
#         print('This is the data for ' + company)
#         data, meta_data = ts.get_daily(symbol = company, outputsize='full')
#         pprint(data)

#         # To plot the data
#         # ti = TechIndicators(key='RWBEQKLG65YPF62U', output_format='pandas') # API Key: RWBEQKLG65YPF62U
#         # data, meta_data = ti.get_daily(symbol = company, outputsize='full')

#         data['1. open'].plot()
#         data['2. high'].plot()
#         data['3. low'].plot()
#         data['4. close'].plot()
#         plt.title('Daily indicator for ' + company)
#         plt.show()


#     except:
#         print('The data for ' + company + ' did not load')
#         counter += 1

# print(counter, "companies out of", len(listOfCompanies), "companies' data was not retrieved")
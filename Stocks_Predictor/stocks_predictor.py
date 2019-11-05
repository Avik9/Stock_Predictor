# Website for the API: https://alpha-vantage.readthedocs.io/en/latest/
# API Key: RWBEQKLG65YPF62U

# importing the dependencies 
import tensorflow as tf 
import numpy as np 
import matplotlib.pyplot as plt 
import csv

# from alpha_vantage.techindicators import TechIndicators
# from alpha_vantage.timeseries import TimeSeries
# from pprint import pprint
# import matplotlib.pyplot as plt

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
            companyDataReader = csv.reader(company_data, delimiter=',')
            for row in companyDataReader:
                dates_data.append(row[0])
                open_data.append(row[1])
                high_data.append(row[2])
                low_data.append(row[3])
                close_data.append(row[4])
                # To print the data
                # print(row)
            
    except:
        print(company + " could not be loaded.")
        continue

        y = dates_data[1::]

        x1 = open_data[1::]
        plt.plot(x1, y, label = "Open Prices")

        # x4 = close_data[1::]
        # plt.plot(x4, y, label = "Close Prices")

        # naming the x axis 
        plt.xlabel('Prices')

        # naming the y axis 
        plt.ylabel('Time')

        # giving a title to my graph 
        plt.title('Four lines on same graph!')

        # show a legend on the plot 
        # plt.legend() 
        
        # function to show the plot 
        plt.show() 









# WORKING WITH THE API (Later Stage of the project)

# ts = TimeSeries(key='RWBEQKLG65YPF62U')
# counter = 0

# for company in listOfCompanies:
#     try:
#         # To print the data
#         print('This is the data for ' + company)
#         data, meta_data = ts.get_daily(symbol = company)
#         pprint(data)

#         # To plot the data
#         ti = TechIndicators(key='RWBEQKLG65YPF62U', output_format='pandas') # API Key: RWBEQKLG65YPF62U
#         data, meta_data = ti.get_bbands(symbol = company, interval='60min', time_period=60)

#         data.plot()
#         plt.title('BBbands indicator for ' + company + ' stock (60 min)')
#         plt.show()


#     except:
#         print('The data for ' + company + ' did not load')
#         counter += 1

# print(counter, "companies out of", len(listOfCompanies), "companies' data was not retrieved")\
# importing the dependencies 
import tensorflow as tf 
import numpy as np 
import matplotlib.pyplot as plt 
import pandas

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
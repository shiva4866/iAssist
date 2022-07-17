import requests
import json
import pandas as pd
import warnings


# This will be the URL where load data happens
URL = 'https://fc3fd324-c2b4-45bd-95fc-c249d599d031.mock.pstmn.io/'

warnings.filterwarnings("ignore")

""" it will take JSON response from the request URL and put it in the dataframe """

class Computation:
    def loadData(self, URL):
        response = requests.get(URL)
        data = json.loads(response.text)
        table = pd.DataFrame(data)
        table = self.compute(table)
        return table

    """ perform computation and adding in the table 

        some formulaes
            Net Profit Margin = net income / total revenue
            Current Ratio = current assets / current liabilities
    """

    def compute(self, table):
        netProfitMarginRow = []
        operatingCashflowByNetProfitRow = []
        currentRatioRow = []
        for (columnKeys, columnValues) in table.iteritems():
            netProfitMarginRow.append(
                columnValues['Net Income']/columnValues['totalRevenue']*100)

            operatingCashflowByNetProfitRow.append(
                columnValues['Operating cashflow']/columnValues['Net Income'])

            currentRatioRow.append(
                columnValues['Current Assets']/columnValues['Current Liabilities'])
        table.loc['Net Profit Margin'] = netProfitMarginRow
        table.loc['Operating Cashflow / Net Profit'] = operatingCashflowByNetProfitRow
        table.loc['Current Ratio'] = currentRatioRow
        return table

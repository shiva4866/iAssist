import requests
import pandas as pd
import urls
from bs4 import BeautifulSoup

class Scrapper:
    
    def getCompetitors(self):
        # get the html
        urlContainer = urls.Url()
        url          = urlContainer.getCompetitorsUrl()
        r            = requests.get(url)
        htmlContent  = r.content
        soup         = BeautifulSoup(htmlContent, 'html.parser')

        # get tables attributes
        headers = []
        for i in soup.find_all('th'):
            title = i.text
            headers.append(title)

        mydata      = pd.DataFrame(columns = headers)
        competetors = []

        # Create a for loop to fill mydata
        for j in soup.find_all('tr')[1:]:
            row_data           = j.find_all('td')
            row                = [i.text for i in row_data]
            length             = len(mydata)
            mydata.loc[length] = row
            competetors.append(row[0])

        return competetors
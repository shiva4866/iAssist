import requests
import json
import pandas as pd

URL = 'https://fc3fd324-c2b4-45bd-95fc-c249d599d031.mock.pstmn.io/'

def loadData():
    response = requests.get(URL)
    data = json.loads(response.text)
    table = pd.DataFrame()
    for key,value in data.items():
        for k,v in value.items():
            print(v)

loadData()
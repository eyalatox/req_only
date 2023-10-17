import pandas as pd
import requests
from requests import post

connStr = "DemoDB_Dev; User ID = eyal; Password = LGN1cmF0aW9uLWFwaSxuZXh4;"


print(pd.read_csv('1.csv'))

HEADERS = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
    'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnROYW1lIjoid2ViYXBwLXYzMSIsInNjb3BlIjoic3RhdGljLWNvbnRlbnQtYXBpLGN1cmF0aW9uLWFwaSxuZXh4LWNvbnRlbnQtYXBpLXYzMSx3ZWJhcHAtYXBpIn0.mbuG9wS9Yf5q6PqgR4fiaRFIagiHk9JhwoKES7ksVX4',
}

res1 = requests.get('http://pbom.dev/', headers=HEADERS)

res2 = requests.get('http://ox.security/', allow_redirects=True)

res3 = requests.get('https://megalinter.io/', verify=False)

devDBPassword = 'sa%441DB2P3a#s@s'

ascii_art = r"""
________         .__        __                               
\_____  \   _____|__| _____/  |_  ________________    _____  
 /   |   \ /  ___/  |/    \   __\/ ___\_  __ \__  \  /     \ 
/    |    \\___ \|  |   |  \  | / /_/  >  | \// __ \|  Y Y  \
\_______  /____  >__|___|  /__| \___  /|__|  (____  /__|_|  /
        \/     \/        \/    /_____/            \/      \/ 
"""

myDevSecretKey = 'ab11a5b7f7b0a5b1defef8c6446b1769'
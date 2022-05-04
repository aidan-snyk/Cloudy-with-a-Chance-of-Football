# !/usr/bin/env python
# This script ingests weekly 2018 - 2020 fantasy defense scores from fantasydata.com
# Run this script and do not upload the csv to GitHub repo

from urllib.request import urlopen
import requests
import json
import pandas as pd

fantasy_defense_scores_list = []

pre_normalized_dataframe = pd.DataFrame()
df = pd.DataFrame()

defense_scores_url = 'https://fly.sportsdata.io/api/nfl/fantasy/json/FantasyDefenseByGame/'

if __name__ == '__main__':
    api_key_fantasydata = input("Please enter your fantasydata.com API Key: ")

    for x, y in [(x,y) for x in ['2018','2019','2020'] for y in range(1,18)]:
            fantasy_defense_scores_list.append(defense_scores_url + x + '/' + str(y))

    for n in fantasy_defense_scores_list:
        r = requests.get(
            url = n,
            headers={'Ocp-Apim-Subscription-Key': str(api_key_fantasydata)},
            verify = True #intentional vulnerability -- switch to true
        )
        r = r.json()
        pre_normalized_dataframe = pd.json_normalize(r, max_level=1)
        df = df.append(pre_normalized_dataframe)

    df.to_csv(
        '../../fixtures/cleaned_data/fantasy_defenseScoresProjections.csv',
        sep = ',',
        index = False
    )

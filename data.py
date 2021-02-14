# All data related imports and data processing are done here..

import pandas as pd

# Google drive data retrieving section

# gdurl = 'https://drive.google.com/file/d/1bADOBJC2yDUh23YmZSQKXr_XmFNaUT9m/view?usp=sharing'
# urlPath = 'https://drive.google.com/uc?export=download&id='+ gdurl.split('/')[-2]

# sale = pd.read_csv(urlPath, parse_dates=['Trans Date'], dayfirst=True)
sale = pd.read_csv('data/Sales.csv', parse_dates=['Trans Date'], dayfirst=True)



# Function for card to show values as human readable..

def humanizer(num):
    if num > 9999999:
        num = f"{(num/10000000).round(2)} Cr"
        return num
    # if num > 999999:
    #     num = f"{(num/1000000).round(2)} M"
    #     return num
    if num > 99999:
        num = f"{(num/100000).round(2)} L"
        return num
    if num > 999:
        num = f"{(num/1000).round(2)} K"
        return num
    if num < 1000:
        return num

# Function for card's growth & de-growth text..

def growthStr(currentDate,lastDate,type):
    try:
        if type == 'month':
            if currentDate > lastDate:
                cardStr = f"{round(currentDate/lastDate * 100) - 100}% growth from last month"
                return cardStr
            elif currentDate < lastDate:
                cardStr = f"{round(currentDate/lastDate * 100 - 100) * -1}% degrowth from last month"
                return cardStr
            else:
                cardStr = "0% growth from last month"
                return cardStr
        if type == 'week':
            if currentDate > lastDate:
                cardStr = f"{round(currentDate/lastDate * 100) - 100}% growth from last week same day"
                return cardStr
            elif currentDate < lastDate:
                cardStr = f"{round(currentDate/lastDate * 100 - 100) * -1}% degrowth from last week same day"
                return cardStr
            else:
                cardStr = "0% growth from last week same day"
                return cardStr        
    except:
        pass
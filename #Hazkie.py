#Hazkie
class colors:
    BIGreen = "[\033[1;92m\]"
    cyan = "\033[1;36m"

print(colors.BIGreen + """
╔═══╦══╗─╔═══╦═══╦═══╦═══╦═══╦════╗╔════╦═══╦═══╦╗
║╔══╣╔╗║─║╔═╗║╔══╣╔═╗║╔═╗║╔═╗║╔╗╔╗║║╔╗╔╗║╔═╗║╔═╗║║
║╚══╣╚╝╚╗║╚═╝║╚══╣╚═╝║║─║║╚═╝╠╝║║╚╝╚╝║║╚╣║─║║║─║║║
║╔══╣╔═╗║║╔╗╔╣╔══╣╔══╣║─║║╔╗╔╝─║║────║║─║║─║║║─║║║─╔╗
║║──║╚═╝║║║║╚╣╚══╣║──║╚═╝║║║╚╗─║║────║║─║╚═╝║╚═╝║╚═╝║
╚╝──╚═══╝╚╝╚═╩═══╩╝──╚═══╩╝╚═╝─╚╝────╚╝─╚═══╩═══╩═══╝""")
print(colors.cyan + u'\033[40m' + """
            ▄▄▄▄
          ▄██████     ▄▄▄█▄
        ▄██▀░░▀██▄    ████████▄
       ███░░░░░░██     █▀▀▀▀▀██▄▄
     ▄██▌░░░░░░░██    ▐▌       ▀█▄
     ███░░▐█░█▌░██    █▌         ▀▌
    ████░▐█▌░▐█▌██   ██
   ▐████░▐░░░░░▌██   █▌
    ████░░░▄█░░░██  ▐█
    ████░░░██░░██▌  █▌
    ████▌░▐█░░███   █
    ▐████░░▌░███   ██
     ████░░░███    █▌
   ██████▌░████   ██
 ▐████████████   ███
 █████████████▄████
██████████████████
██████████████████
█████████████████▀
█████████████████
████████████████
████████████████


 """)
print("[+]A FB AUTO-REPORT v1 Created By HAZKIE DEV[+]")

import requests  
import json  
import datetime  
  
# Facebook API credentials  
access_token = "YOUR_ACCESS_TOKEN"  
ad_account_id = "YOUR_AD_ACCOUNT_ID"  
  
# Set the date range for the report  
start_date = datetime.date.today() - datetime.timedelta(days=7)  
end_date = datetime.date.today()  
  
# Define the report fields  
fields = [  
   "ad_id",  
   "ad_name",  
   "ad_status",  
   "impressions",  
   "clicks",  
   "ctr",  
   "cpc",  
   "cpm",  
   "spend"  
]  
  
# Define the report filters  
filters = [  
   {  
      "field": "ad_status",  
      "operator": "IN",  
      "values": ["ACTIVE"]  
   }  
]  
  
# Define the report sorting  
sort = [  
   {  
      "field": "impressions",  
      "direction": "DESCENDING"  
   }  
]  
  
# Define the report limit  
limit = 100  
  
# Construct the API request  
url = f"https://graph.facebook.com/v13.0/{ad_account_id}/insights"  
params = {  
   "access_token": access_token,  
   "fields": ",".join(fields),  
   "filters": json.dumps(filters),  
   "sort": json.dumps(sort),  
   "limit": limit,  
   "time_range": f"{{\"since\":\"{start_date}\",\"until\":\"{end_date}\"}}"  
}  
  
# Send the API request  
response = requests.get(url, params=params)  
  
# Parse the response  
data = response.json()  
  
# Print the report  
print("Facebook Ad Report")  
print("-------------------")  
for ad in data["data"]:  
   print(f"Ad ID: {ad['ad_id']}")  
   print(f"Ad Name: {ad['ad_name']}")  
   print(f"Ad Status: {ad['ad_status']}")  
   print(f"Impressions: {ad['impressions']}")  
   print(f"Clicks: {ad['clicks']}")  
   print(f"CTR: {ad['ctr']}")  
   print(f"CPC: {ad['cpc']}")  
   print(f"CPM: {ad['cpm']}")  
   print(f"Spend: {ad['spend']}")  
   print("-------------------")

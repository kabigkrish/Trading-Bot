from py5paisa import FivePaisaClient
from dotenv import load_dotenv
import os
load_dotenv()
##
email=os.getenv('email')
passwd=os.getenv('passwd')
dob=os.getenv('dob')

#initializing client 
client = FivePaisaClient(email=email, passwd=passwd, dob=dob)
client.login() 

# NOTE : Symbol has to be in the same format as specified in the example below.

req_list_=[{
    "Exch":"N","ExchType":"C","Symbol":"BHEL","Expiry":"","StrikePrice":"0","OptionType":""},
    {"Exch":"B","ExchType":"C","Symbol":"RBLBANK","Expiry":"","StrikePrice":"0","OptionType":"" }]
print(client.fetch_market_feed(req_list_))
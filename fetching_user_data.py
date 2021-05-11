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
# Fetches holdings
holdings=client.holdings()

# Fetches margin
margin=client.margin()

# Fetches positions
positions=client.positions()

# Fetches the order book of the client
order_book=client.order_book()

print(holdings)
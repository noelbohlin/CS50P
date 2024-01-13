""" från uppgiften Bitcoin Price Index från CS50 """

import sys
import requests

# make sure the input "n" is correct
try:
    n = float(sys.argv[1])
except ValueError:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    else:
        sys.exit("Command-line argument is not a number")

# imports the rate_float as rate and makes sure it works
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    rate = response["bpi"]["USD"]["rate_float"]
except requests.RequestException:
    sys.exit("Request-failure")

print(f"${(rate * n):,.4f}")

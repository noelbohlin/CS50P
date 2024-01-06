# från uppgiften Bitcoin Price Index från CS50

import requests
import sys

# make sure the input "n" is correct
try:
    n = float(sys.argv[1])
except Exception:
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

# prints rate * input with the right formating
print(f"${(rate * n):,.4f}")

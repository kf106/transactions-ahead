import math
import requests
import json
import sys

if len(sys.argv) < 2:
    print("Command line argument missing")
    quit()

satperb = math.floor(float(sys.argv[1]))

url = "https://bitcoinfees.earn.com/api/v1/fees/list"

json_str = requests.get(url).text
json_dict = json.loads(json_str)

fees = json_dict.get("fees", "")

count = 0
offset = 0

for element in fees:
    clb = element.get("maxFee", "")
    if clb == satperb or clb - 1 == satperb:
        offset = element.get("memCount", "")
    if clb > satperb:
        count = count + element.get("memCount", "")

print("Transactions in your fee band: " + str(offset))
print("Transactions ahead of your fee band: " + str(count))



from API import *

### in API.py
# QUEUE       = "RANKED_SOLO_5x5"
# TIER        = "GOLD"
# DIVISION    = "III"
# PAGE        = "1"

### get league data
url = GET("kr", "lol/league/v4/entries/{queue}/{tier}/{division}?page={page}".format(tier=TIER, division=DIVISION, queue=QUEUE, page="1"), True)
res = requests.get(url)

if res.status_code == 200:
    json_data = json.loads(res.text)
    print("read successfully : {length}".format(length=len(json_data)))
    with open(FILE_NAME, 'w') as outfile:
        json.dump(json_data, outfile, indent=4)
else:
    print("error")
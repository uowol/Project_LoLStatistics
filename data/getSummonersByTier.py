from API import *

QUEUE       = "RANKED_SOLO_5x5"
TIER        = "SILVER"
DIVISION    = "III"
PAGE        = "1"

# get league data - silver 3 solo rank
url = GET("kr", "lol/league/v4/entries/{queue}/{tier}/{division}?page={page}".format(queue=QUEUE, tier=TIER, division=DIVISION, page=PAGE), True)
res = requests.get(url)

if res.status_code == 200:
    json_data = json.loads(res.text)
    print("read successfully : {length}".format(length=len(json_data)))
    with open("data_summoner_{tier}_{division}_{queue}.json".format(tier=TIER, division=DIVISION, queue=QUEUE), 'w') as outfile:
        json.dump(json_data, outfile, indent=4)
else:
    print("error")
from API import *

TYPE    = "normal"     # ranked / normal 
START   = "0"
COUNT   = "100"         

### get puuid by JSON file
with open(FILE_NAME_BY_SUMMONER, "r") as json_file:
    json_data = json.load(json_file)
    puuid=json_data["puuid"]
if len(puuid) > 0:
    print("read successfully")
else:
    print('error')

### get matchId
url = GET("asia", "lol/match/v5/matches/by-puuid/{puuid}/ids?type={type}&start={start}&count={count}".
    format(puuid=puuid, type=TYPE, start=START, count=COUNT), True)
res = requests.get(url)
if res.status_code == 200:
    matches = json.loads(res.text)
else:
    print("error : {code}".format(code=res.status_code))    # errorCode 429: too many requests

if len(matches) > 0:
    print("read successfully : {length}".format(length=len(matches)))
    with open(MATCH_FILE_NAME_BY_SUMMONER, 'w') as outfile:
        json.dump(matches, outfile, indent=4)
else:
    print('error')

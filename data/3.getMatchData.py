from API import *

MATCH_FILE_NAME         = "data_summoner_match_SILVER_III_RANKED_SOLO_5x5.json"
MATCH_DATA_FILE_NAME    = "data_summoner_match_data_SILVER_III_RANKED_SOLO_5x5.json"

### get matchesId, match data가 있다면 실행해줍니다.
matches_id = []
with open(MATCH_FILE_NAME, "r") as json_file:
    json_data = json.load(json_file)
    for matches in json_data:
        matches_id += matches
if len(matches_id) > 0:
    print("read successfully : {length}".format(length=len(matches_id)))
else:
    print('error')

### get match data
length_of_requests = 0
data = []
for matchId in matches_id:
    url = GET("asia", "lol/match/v5/matches/{matchId}".format(matchId=matchId), False)
    res = requests.get(url)
    # requests는 1초에 20개, 2분에 100개로 제한되기에 딜레이를 넣어줍니다.
    if ++length_of_requests % 20 == 0:  
        sleep(1)
        if length_of_requests == 100:
            sleep(120)
            length_of_requests = 0
    if res.status_code == 200:
        json_data = json.loads(res.text)
        data.append(json_data)
    else:
        print("error : {code} where {matchId}".format(code=res.status_code, matchId=matchId))    # errorCode 429: too many requests
        # 404 error?
        # 503 error?
if len(data) > 0:
    print("read successfully : {length}".format(length=len(data)))
    with open(MATCH_DATA_FILE_NAME, 'w') as outfile:
        json.dump(data, outfile, indent=4)
else:
    print('error')


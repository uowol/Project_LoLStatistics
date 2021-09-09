from API import *

### get matchesId
matches_id = []
with open(MATCH_FILE_NAME_BY_SUMMONER, "r") as json_file:
    matches_id = json.load(json_file)
if len(matches_id) > 0:
    print("read successfully : {length}".format(length=len(matches_id)))
else:
    print('error')

### get match timeline data
data = []
missing_data = []
for matchId in matches_id:
    url = GET("asia", "lol/match/v5/matches/{matchId}/timeline".format(matchId=matchId), False)
    res = requests.get(url)
    # requests는 1초에 20개, 2분에 100개로 제한되기에 딜레이를 넣어줍니다.
    if ++LENGTH_OF_REQUESTS % 20 == 0:  
        sleep(1)
        if LENGTH_OF_REQUESTS == 100:
            sleep(120)
            LENGTH_OF_REQUESTS = 0
    if res.status_code == 200:
        json_data = json.loads(res.text)
        data.append(json_data)
    else:
        print("error : {code} where {matchId}".format(code=res.status_code, matchId=matchId))    # errorCode 429: too many requests
        if res.status_code == 503 : missing_data.append(matchId)
        # 404 error - not found
        # 503 error - service unavailable
if len(data) > 0:
    print("num of missing data : {length}".format(length=(len(matches_id) - len(data))))
else:
    print('error')

### get missing data
for matchId in missing_data:
    url = GET("asia", "lol/match/v5/matches/{matchId}".format(matchId=matchId), False)
    res = requests.get(url)
    # requests는 1초에 20개, 2분에 100개로 제한되기에 딜레이를 넣어줍니다.
    if ++LENGTH_OF_REQUESTS % 20 == 0:  
        sleep(1)
        if LENGTH_OF_REQUESTS == 100:
            sleep(120)
            LENGTH_OF_REQUESTS = 0
    if res.status_code == 200:
        json_data = json.loads(res.text)
        data.append(json_data)
    else:
        print("error : {code} where {matchId}".format(code=res.status_code, matchId=matchId))    # errorCode 429: too many requests
if len(data) > 0:
    print("read successfully : {length}".format(length=len(data)))
    with open(MATCH_TIMELINE_DATA_FILE_NAME_BY_SUMMONER, 'w') as outfile:
        json.dump(data, outfile, indent=4)
else:
    print('error')
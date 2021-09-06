from API import *

### in API.py
# FILE_NAME       = "data_summoner_GOLD_III_RANKED_SOLO_5x5.json"
# PUUID_FILE_NAME = "data_summoner_puuid_SILVER_III_RANKED_SOLO_5x5.json"
# MATCH_FILE_NAME = "data_summoner_match_SILVER_III_RANKED_SOLO_5x5.json"

### get summonerId
summoner_id = []
with open(FILE_NAME, "r") as json_file:
    json_data = json.load(json_file)
    for summoner in json_data:
        summoner_id.append(summoner['summonerId'])
if len(summoner_id) > 0:
    print("read successfully : {length}".format(length=len(summoner_id)))
else:
    print('error')

### get puuid, puuid data가 없다면 실행시켜줍니다.
# summoner_puuid = []
# for summonerId in summoner_id:
#     url = GET("kr", "lol/summoner/v4/summoners/{encryptedSummonerId}".format(encryptedSummonerId=summonerId), False)
#     res = requests.get(url)
#     # requests는 1초에 20개, 2분에 100개로 제한되기에 딜레이를 넣어줍니다.
#     if ++LENGTH_OF_REQUESTS % 20 == 0:  
#         sleep(1)
#         if LENGTH_OF_REQUESTS == 100:
#             sleep(120)
#             LENGTH_OF_REQUESTS = 0
#     if res.status_code == 200:
#         json_data = json.loads(res.text)
#         summoner_puuid.append(json_data['puuid'])
#     else:
#         print("error : {code}".format(code=res.status_code))    # errorCode 429: too many requests
# if len(summoner_puuid) > 0:
#     print("read successfully : {length}".format(length=len(summoner_puuid)))
#     # puuid data를 저장합니다.
#     with open(PUUID_FILE_NAME, 'w') as outfile:
#         json.dump(summoner_puuid, outfile, indent=4)
# else:
#     print('error')

### get puuid by JSON file, puuid data가 있다면 실행시켜줍니다.
summoner_puuid = []
with open(PUUID_FILE_NAME, "r") as json_file:
    json_data = json.load(json_file)
    for puuid in json_data:
        summoner_puuid.append(puuid)
if len(summoner_puuid) > 0:
    print("read successfully : {length}".format(length=len(summoner_puuid)))
else:
    print('error')

### get matchId
matches = []
for puuid in summoner_puuid:
    url = GET("asia", "lol/match/v5/matches/by-puuid/{puuid}/ids".format(puuid=puuid), False)
    res = requests.get(url)
    # requests는 1초에 20개, 2분에 100개로 제한되기에 딜레이를 넣어줍니다.
    if ++LENGTH_OF_REQUESTS % 20 == 0:  
        sleep(1)
        if LENGTH_OF_REQUESTS == 100:
            sleep(120)
            LENGTH_OF_REQUESTS = 0
    if res.status_code == 200:
        json_data = json.loads(res.text)
        matches.append(json_data)
    else:
        print("error : {code}".format(code=res.status_code))    # errorCode 429: too many requests
if len(matches) > 0:
    print("read successfully : {length}".format(length=len(matches)))
    with open(MATCH_FILE_NAME, 'w') as outfile:
        json.dump(matches, outfile, indent=4)
else:
    print('error')

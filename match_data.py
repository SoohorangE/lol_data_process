import json

with open("match_0.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("매치 데이터의 수:", len(data))
print("데이터 타입:", type(data))

single_match = data[0]
print("하나의 매치에 대한 데이터 타입:", type(single_match))

metadata = single_match["metadata"]
info = single_match["info"]

print("매치 -> metadata 데이터 타입:", type(metadata))
print("매치 -> info 데이터 타입:", type(info))
print("매치의 소환사 수:", len(metadata["participants"]))

import datetime
time = info["gameCreation"] // 1000
print(time)
real_time = datetime.datetime.fromtimestamp(time, datetime.UTC)
print(real_time)

print("### LOL 솔로랭크 매치 데이터 정보 ###")
print(f"Match Id: {metadata['matchId']}")
print(f"매치 생성 시간: {real_time.strftime('%Y년 %m월 %d일 %h시 %m분')}")
print(f"매치 플레이 시간: {info['gameDuration'] // 60 }분 {info["gameDuration"]%60}초")


participants = info["participants"]
first_player = participants[0]

if first_player["win"]:
    wintime = "블루" if first_player["teamId"] == 100 else "레드"
else:
    wintime = "레드" if first_player["teamId"] == 200 else "블루"
print(f"승리한 팀: {wintime}\n")

print(f" ## 플레이어 정보 ##")
for player in participants:
    print(f"포지션: {player['teamPosition']}")
    print(f"팀: {"블루" if player["teamId"] == 100 else "레드"}")
    print(f"팀 내부의 고유 아이디: {player["participantId"]}")
    print(f"챔피언: {player["championName"]}")

    # kda 구하기
    k = player["kills"]; d = player["deaths"]; a = player["assists"]
    kda = (k+a) / (1 if d==0 else d)

    print(f"K/D/A: {k}, {d}, {a}, KDA: {kda:.1f}")

    print(f"챔피언에게 가한 데미지: {player["totalDamageDealtToChampions"]}")
    print(f"  - 분당 데미지: {player['totalDamageDealtToChampions'] // info["gameDuration"] * 60}")
    print(f"골드 획득량: {player["goldEarned"]}")
    print(f"경험치 획득량: {player["champExperience"]}")
    

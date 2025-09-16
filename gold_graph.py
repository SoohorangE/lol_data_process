import json

from gold_win_loss import to_extract

with open("match_0.json", "r", encoding="utf-8") as f:
    data_match = json.load(f)

with open("timeline_0.json", "r", encoding="utf-8") as f:
    data_timeline = json.load(f)

match = data_match[0]['info']
timeline = data_timeline[0]['info']

players = match['participants']

blue_team = {}
red_team = {}

for p in players:
    teamId = p['teamId']
    teamPosition = p['teamPosition']
    pid = p['participantId']
    if teamId == 100: blue_team[pid] = teamPosition
    else: red_team[pid] = teamPosition
    print(f"teamId = {teamId}, teamPosition = {teamPosition}, pid = {pid}")

print(f"blue_team = {blue_team}")
print(f"red_team = {red_team}")

# to do 해야할 것
# minute = [0,1,2,3,4...., 20]
# blue_score = [x0, x1, x2, ... x25] < 25분까지 분단위로 합산할 블루팀의 스코어
# red_score = [y0, y1, y2, ... y25]
# x3의미 : 3분 시점에서 블루팀의 특정 지표(totalGold, xp, 등 < to_extract)의 총 합산량
# y20의미: 20분 시점에서 레드팀의 특정 지표의 총 합산량

minutes = []
blue_score = []
red_score = []
to_extract = "totalGold"
frames = timeline['frames']

for frame in frames:
    time = frame['timestamp'] // 60000
    minutes.append(time)

    # 여기서부터 blue_score와 red_score를 계산해보기

print(minutes)
print(blue_score)
print(red_score)



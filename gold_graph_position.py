# gold_graph.py 참고
# position 변수에 맞는 특정 포지션의 불루팀과 레드팀의 그래프를 비교

import json

from gold_win_loss import to_extract, total_blue

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
    if teamId == 100:
        blue_team[pid] = teamPosition
    else:
        red_team[pid] = teamPosition
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

position = "MIDDLE"

for frame in frames:
    time = frame['timestamp'] // 60000
    minutes.append(time)

    # # 여기서부터 blue_score와 red_score를 계산해보기
    # participants = frame['participantFrames']
    #
    # total_blue_gold = 0
    # total_red_gold = 0
    #
    # for i in range(1, len(participants) + 1):
    #     if i < 6: total_blue_gold += participants[str(i)][to_extract]
    #     else: total_red_gold += participants[str(i)][to_extract]
    #
    # blue_score.append(total_blue_gold)
    # red_score.append(total_red_gold)

    blue_score_1min, red_score_1min = 0, 0
    for pid, item in frame['participantFrames'].items():
        if int(pid) in blue_team:
            if blue_team[int(pid)] == position : blue_score_1min += item[to_extract]
            #blue_score_1min += item[to_extract]
            print(f"time = {time:2d}, pid = {pid:2s}, team=blue, score={item[to_extract]}")
        else:
            if red_team[int(pid)] == position : red_score_1min += item[to_extract]
            #red_score_1min += item[to_extract]
            print(f"time = {time:2d}, pid = {pid:2s}, team=red, score={item[to_extract]}")

    print(f"blue = {blue_score_1min}, red = {red_score_1min}")

    blue_score.append(blue_score_1min)
    red_score.append(red_score_1min)

print(minutes)
if minutes[-1] == minutes[-2]: minutes[-1] += 1
print(minutes)
print(blue_score)
print(red_score)

import matplotlib.pyplot as plt

plt.plot(minutes, blue_score, label=f"blue: {to_extract}", marker="o", linewidth=2)
plt.plot(minutes, red_score, label=f"red: {to_extract}", marker="o", linewidth=2)

plt.xlabel("Minutes (m)")
plt.ylabel(f"Team {to_extract}")
plt.title(f"Feature {to_extract}, {position} graph")
plt.legend()
plt.grid(True)
plt.show()

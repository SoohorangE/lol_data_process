import json

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



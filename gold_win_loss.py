# match_0.json
# to_extract 라는 변수에 지정된 항목의 합산으로
# 레드팀과 블루팀의 값을 비교하여, 승패를 예측해본다

import json

with open("match_0.json", "r", encoding="utf-8") as f:
    data = json.load(f)

correct_pred = 0
to_extract = "goldEarned"

for j, match in enumerate(data):
    total_red, total_blue = 0, 0

    # winner: 실제로 이긴 팀
    # pred_winner: to_extract를 팀별로 합산한 것을 단순비교하여 큰 것이 이긴팀으로 예측
    # winner와 pred_winnder가 같으면 correct_pred += 1

    #채워넣기 2시까지

    info = match["info"]
    players = info["participants"]

    for p in players:
        score = p[to_extract]
        if p['teamId'] == 100: total_blue += score
        else: total_red += score

    # winner 실제로 이긴 팀
    if players[0]['win']: winner="블루" if players[0]['teamId'] == 100 else "레드"
    else : winner="레드" if players[0]['teamId'] == 100 else "블루"

    # pred_winner: to_extract를 팀별로 합산한 것을 단순비교하여 큰 것이 이긴팀으로 예측
    pred_winner = "블루" if total_blue > total_red else "레드"

    # winner와 pred_winner가 같으면 correct_pred += 1
    if winner == pred_winner: correct_pred += 1

    print(f"{j+1:2d}번쨰 매치: 승리팀 - {winner}, 예측 - {pred_winner}")
    print(f"{to_extract} 변수: 블루 - {total_blue}, 레드 - {total_red}")



    # for p in players:
    #     if players["teamId"] == 100:
    #         total_red += players[to_extract]
    #     else:
    #         total_blue += players[to_extract]
    #
    #     if winner is None:
    #         if players["win"] == True:
    #             winner = "red" if players["teamId"] == 100 else "blue"
    #
    # pred_winner = "red" if total_red > total_blue else "blue"
    #
    # print(total_red, total_blue, winner, pred_winner)
    #
    # if winner == "red" and pred_winner == "red":
    #     correct_pred += 1
    # elif winner == "blue" and pred_winner == "blue":
    #     correct_pred += 1


print(f"{to_extract} 변수의 승패 예측 정확도: {correct_pred/len(data):.2f}")
# AchievementRank
import json
import jsonsearch
import pandas
import requests
import time

uidTable = []
mergedData = []

r = open('Achievement/uidList.txt')
line = r.readline()
while line:
    uidData = eval(line)
    uidTable.append(uidData)
    line = r.readline()
r.close()

for i in uidTable:
    
    url = 'https://api.mihomo.me/sr_info_parsed/' + str(i)
    response = requests.get(url)
    response = json.loads(response.content)
    
    uid = response['player']['uid']
    nickname = response['player']['nickname']
    level = response['player']['level']
    signature = response['player']['signature']
    achievementCount = response['player']['space_info']['achievement_count']
    
    data = {
        'uid': uid,
        'nickname': nickname,
        'level': level,
        'signature': signature,
        'achievementCount': achievementCount
    }
    
    mergedData.append(data)

    time.sleep(3)

mergedData = sorted(mergedData, key = lambda j: j['nickname'])
mergedData = sorted(mergedData, key = lambda j: j['achievementCount'], reverse = True)

mergedData = '{"achievementData":' + str(json.dumps(mergedData, ensure_ascii = False)) + '}'

jsonData = jsonsearch.JsonSearch(object = mergedData, mode = 's')

uidArr = jsonData.search_all_value(key = 'uid')
nicknameArr = jsonData.search_all_value(key = 'nickname')
levelArr = jsonData.search_all_value(key = 'level')
signatureArr = jsonData.search_all_value(key = 'signature')
achievementCountArr = jsonData.search_all_value(key = 'achievementCount')

htmlText = '<p style:"display: none;">更新时间戳:' + str(time.time()) + '</p><table><thead><tr><th class="rank">排名</th><th class="uid">UID</th><th class="nickname">昵称</th><th class="level">开拓等级</th><th class="sign">签名</th><th class="achievementCount">成就数</th></thead><tbody>'

df = pandas.DataFrame(achievementCountArr)
df = df.rank(method = 'min')
dfArr = df.values
rankArr = dfArr.tolist()

for j in range(0, len(achievementCountArr)):
    tempElement = str(rankArr[j]).replace("[", "").replace("]", "").replace(".0", "")
    rankArr[j] = tempElement

for k in range(0, len(achievementCountArr)):
    tempText = '<tr><td class="rank">' + str(rankArr[k]) + '</td><td class="uid">'+ str(uidArr[k]) +'</td><td class="nickname">'+ str(nicknameArr[k]) +'</td><td class="level">'+ str(levelArr[k]) +'</td><td class="sign">'+ str(signatureArr[k]) +'</td><td class="achievementCount">'+ str(achievementCountArr[k]) +'</td></tr>'
    htmlText = htmlText + tempText
    
htmlText = htmlText + '</tbody></table>'

file = open('AchievementRank.html', 'w', encoding = 'utf-8')
file.write(htmlText)
file.close()

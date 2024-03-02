# AchievementRank
import json
import time
import requests

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
        'achievementCount': achievementCount,
        'ticks': time.time()
    }
    
    mergedData.append(data)

    time.sleep(3)

mergedData = sorted(mergedData, key = lambda j: j['nickname'])
mergedData = sorted(mergedData, key = lambda j: j['achievementCount'], reverse = True)

mergedData = json.dumps(mergedData, ensure_ascii = False)

file = open('AchievementRank.json', 'w', encoding = 'utf-8')
file.write(mergedData)
file.close()

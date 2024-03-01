# AchievementRank
import json
import time
import requests

uidTable = []
mergedData = []

r = open('Achievement/uidList.txt', encoding = 'GB2312')
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
    
    uid = str(response['player']['uid'])
    nickname = str(response['player']['nickname'])
    level = str(response['player']['level'])
    signature = str(response['player']['signature'])
    achievementCount = str(response['player']['space_info']['achievement_count'])
    
    data = {
        'uid': uid,
        'nickname': nickname,
        'level': level,
        'signature': signature,
        'achievementCount': achievementCount,
        'ticks': time.time()
    }
    
    mergedData.append(data)

mergedData = json.dumps(mergedData, ensure_ascii = False)

file = open('AchievementRank.json', 'w', encoding = 'GB2312')
file.write(mergedData)
file.close()

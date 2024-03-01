# AchievementRank
import json
import requests

mergedData = []

for line in open('uidList.txt'):
    
    url = 'https://api.mihomo.me/sr_info_parsed/' + str(line)
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
        'achievementCount': achievementCount
    }
    
    mergedData.append(data)

mergedData = json.dumps(mergedData, ensure_ascii = False)

file = open('AchievementRank.js', 'w', encoding = 'utf-8')
file.write(mergedData)
file.close()

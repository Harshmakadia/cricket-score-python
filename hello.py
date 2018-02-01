import json
import urllib.request
import threading
import requests
wekbook_url = 'https://hooks.slack.com/services/XXXXXXXXXXXXXXXXXX'

def getScore():
    with urllib.request.urlopen('http://www.cricbuzz.com/match-api/19160/commentary.json') as f:
        score_details = (f.read())
        json_data = json.loads(score_details)
        info = ("Ongoing series :" + json_data['series']['name'])
        short = ("Short name :" + json_data['series']['short_name'])
        bat = ("South Africa Batting Score :" + json_data['score']['batting']['score'])
        rr = ("Current Run Rate :" + json_data['score']['crr'])

        data = {
            'text': info + "\n" + short + "\n" + bat + "\n" + rr + "\n",
            'username': 'ScoreBot',
            'icon_emoji': ':robot_face:'
        }

        response = requests.post(wekbook_url, data=json.dumps(
            data), headers={'Content-Type': 'application/json'})

        print('Response: ' + str(response.text))
        print('Response code: ' + str(response.status_code))


def printit():
  threading.Timer(10.0, printit).start()
  getScore()


getScore()

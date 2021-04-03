import json
import requests
from datetime import datetime

def post_message(token, channel, text, attach_list):
    response = requests.post("https://slack.com/api/chat.postMessage",
                             headers={
                                 "Content-type": "application/json; charset=utf-8",
                                 "Authorization": "Bearer " + token},
                             data=json.dumps({
                                 "channel": channel,
                                 "text": text,
                                 "attachments": attach_list})
                             )
    # respos 200 : true
    print(response)

# slack token
myToken = "xoxb-1894883360068-1925505421906-ZdnxQBnNw4hIQ0zOr27TQfw2"

attach_dict = {
    'color'      :'#ff0000',
    'author_name':'INVESTAR',
    "author_link":'https://github.com/investar',
    'title'      :'오늘의 증시 KOSPI',
    'title_link' :'http://finance.naver.com/sise/sise_index.nhn?code=KOSPI',
    'text'       :'2,326.13 △11.89 (+0.51%)',
    'image_url'  :'https://ssl.pstatic.net/imgstock/chart3/day/KOSPI.png'
}

attach_list = [attach_dict]

def send_slack(message):
    """인자로 받은 문자열을 파이썬 셸과 슬랙으로 동시에 출력한다."""
    print(datetime.now().strftime('[%m/%d %H:%M:%S]'), message)
    strbuf = datetime.now().strftime('[%m/%d %H:%M:%S] ') + message
    post_message(myToken, "#mystock", strbuf, attach_list)

send_slack("hahaha")

from os import name
import requests
import uiautomator2 as u2
import time,random,configparser,os,random,warnings
warnings.filterwarnings("ignore")
# import chardet
print('''

 ▀█▀ █ █▄▀ ▀█▀ ▄▀▄ █▄▀   ▄▀▀ ▄▀▄ █▄ ▄█ █▄ ▄█ ██▀ █▄ █ ▀█▀   █   █ █▄▀ ██▀
  █  █ █ █  █  ▀▄▀ █ █   ▀▄▄ ▀▄▀ █ ▀ █ █ ▀ █ █▄▄ █ ▀█  █    █▄▄ █ █ █ █▄▄

version=tiktok version v28.6.5
''')
#tiktok version v28.6.5

def get_hashtag_id(hashtag):
     

    url = "https://m.tiktok.com/api/challenge/detail/"

    querystring = { "challengeName": hashtag }

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36",
        "accept-encoding": "gzip, deflate, br",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "connection": "keep-alive",
        "host": "m.tiktok.com",
        "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "upgrade-insecure-requests": "1",
        "sec-fetch-site": "none",
        "sec-fetch-mode": "navigate",
        "sec-fetch-user": "?1",
        "sec-fetch-dest": "document",
        "accept-language": "en-US,en;q=0.9"
    }

    response = requests.get(url, headers=headers, params=querystring)

    ch_id=response.json()["challengeInfo"]["challenge"]["id"]
    return int(ch_id)

def get_hashtag_videos(hashtag, count=5):
    ch_id=get_hashtag_id(hashtag)
    cursor=0
    post_urls=[]
    for x in range(count):
            params = {
                "source": "challenge_video",
                "cursor": cursor,
                "count": "20",
                'ch_id':ch_id,
                "query_type": "1",
                "carrier_region": "US",
                "locale": "en_US",
                "op_region": "US",
                "region": "US",
                "carrier_region_v2": "310"
            }
            url = "https://api16-normal-useast5.us.tiktokv.com/tiktok/tv/challenge/aweme/v1/"
            headers = {
                "host": "api16-normal-useast5.us.tiktokv.com",
                "user-agent": "okhttp/3.10.0.1",
                "accept-encoding": "gzip",
                "accept": "*/*",
                "connection": "Keep-Alive",
                "passport-sdk-version": "17",
                "sdk-version": "2"
            }

            response = requests.get(url, headers=headers, params=params)
            cursor=response.json()['cursor']
            data=response.json()['aweme_list']
            for i in data:
                shareurl=i["aweme_id"]
                post_urls.append(shareurl)


    return post_urls


config=configparser.ConfigParser()

config.read("config.ini")

device_id=config.get("settings","device_id")
tiktok_username=config.get("settings","tiktok_username")
time_pause=int(config.get("settings","time_pause"))
daily_limit=int(config.get("settings","daily_limit"))
numberofreplies=int(config.get("settings","reply"))
d=u2.connect(device_id)
hastage_title=config.get("settings","hastage_title").split(",")
number_of_post_each_hashtag=int(config.get("settings","number_of_post_each_hashtag"))


# e=post_url
# post_intent="am start -a android.intent.action.VIEW -d {} com.zhiliaoapp.musically/com.ss.android.ugc.aweme.deeplink.AppLinkHandlerV2".format(post_url)
# d.shell(post_intent)
# time.sleep(5)


    
# try:
#     search=d(className="android.view.ViewGroup",index=9).child(className="android.widget.ImageView",index=0).click()
# except:
#     search=d(className="android.view.ViewGroup",index=10).child(className="android.widget.ImageView",index=0).click()
 

# print(d.dump_hierarchy())
# combutton=d(resourceId="com.zhiliaoapp.musically:id/ax1")
# combutton.click()
# exit()
    ## nextbutton=d(className="android.widget.FrameLayout").sibling(className=	"	android.view.ViewGroup").sibling(className="	android.widget.ImageView",index="0").click()
d.session("com.zhiliaoapp.musically")
for i in hastage_title:
    print("\n[++] Scrpaing hashaag #{} posts\n".format(i))
    posts=get_hashtag_videos(i)
    random_posts = random.sample(posts, number_of_post_each_hashtag)
    for cc, post in enumerate(random_posts):
        print(f"\n[++]On post {cc+1} of total {len(random_posts)} for #{i}")
        if post in open("record_posts.txt").read().split("/n"):
            print("post already commented")
            continue
        time.sleep(4)
        
        # search_intent="snssdk1128://search/user/?keyword=%23{}".format(i)
        

        post_intent="am start -a android.intent.action.VIEW -d https://m.tiktok.com/v/{}.html com.zhiliaoapp.musically/com.ss.android.ugc.aweme.deeplink.AppLinkHandlerV2".format(post)
        # print(post_intent)
        d.shell(post_intent)
        # d.send_keys(i)
        time.sleep(3)
        # d(className="android.widget.FrameLayout",index=3).click()
        # time.sleep(4)
        # clickpost=d(className="androidx.recyclerview.widget.RecyclerView",index=0).sibling(className="android.widget.FrameLayout",index=0).click()
        # time.sleep(2)

        try:
            combutton=d(resourceId="com.zhiliaoapp.musically:id/ax1")
            combutton.click()
        except:
            combutton=d(resourceId="com.zhiliaoapp.musically:id/axi")
            combutton.click()
             
        time.sleep(4)

        counter_comment=0
        counter_like=0
        for i in range(10):
            if counter_comment>=int(numberofreplies):
                break  
            for i in d(className="android.view.ViewGroup",index=0):
                    reco=open("record.txt",encoding="utf-8")
                    record=[line.rstrip() for line in reco]
                    like=i.sibling(className="android.widget.ImageView",index="6")
                    # print("up")
                    # if like.exists():
                    #         # try:
                    #         like.click(timeout=2)
                    #         # except:
                    #         #     pass
                    #         counter_like+=1
                    
                    checkname=i.sibling(resourceId="com.zhiliaoapp.musically:id/title")
                    if checkname.exists():
                        name=checkname.get_text()
                        if name in record:
                            continue
                        if name==tiktok_username:
                            continue
                        reply=i.sibling(className="android.widget.LinearLayout",index="5").sibling(text="Reply")
                        if reply.exists():
                            reply.click()
                            time.sleep(2)
                            random_line = random.choice([line.rstrip() for line in open("message_replies.txt", encoding="utf-8")])
                            # print("Cdcd")
                            edit=d(className="android.widget.EditText").send_keys(random_line)
                            send_button=d(className="android.view.ViewGroup",index=0).sibling(className="android.widget.FrameLayout",index=5)
                            send_button.click()
                            counter_comment+=1
                            print("[+] {} replied . total {} commented".format(name,str(counter_comment)))
                            # print(counter_comment,numberofreplies)
                            if counter_comment>=int(numberofreplies):
                                break 
                        if counter_like%30==0:
                            print("[--] Pausing for 30 seconds after every 30 Likes")
                            time.sleep(30)
                        if counter_comment>=int(daily_limit):
                            print("[-] Daily Limit Reached")
                            exit(0)
                        with open("record.txt","a+", encoding="utf-8") as rec:             
                                rec.write(name+"\n")
                        with open("record_posts.txt","a+", encoding="utf-8") as rec:             
                                rec.write(post+"\n")
                        # if counter_comment>=int(numberofreplies):
                        #     break  
                
            scrollable = d(scrollable=True, className="androidx.recyclerview.widget.RecyclerView", instance=0)
            scrollable.scroll.toEnd(max_swipes=1) 
   

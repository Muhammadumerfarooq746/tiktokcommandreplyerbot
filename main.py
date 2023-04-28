
from os import name
import requests
import uiautomator2 as u2
import time,random,configparser,os,random,warnings
warnings.filterwarnings("ignore")
# import chardet


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
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

def get_hashtag_videos(hashtag, count=20):
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

    cursor=0
    for i in range(5):
        url = "https://api16-normal-useast5.us.tiktokv.com/aweme/v1/search/tv/general/single/"

        querystring = {
            "storage_type": "2",
            "manifest_version_code": "110908",
            "_rticket": "1680110003545",
            "app_language": "en",
            "app_type": "normal",
            # "iid": "7192576472099800875",
            "channel": "googleplay",
            "device_type": "sdk_gphone64_arm64",
            "language": "en",
            "cpu_support64": "true",
            "host_abi": "arm64-v8a",
            "locale": "en_US",
            "resolution": "2220*1014",
            "openudid": "2492242a58fac36b",
            "update_version_code": "110908",
            "ac2": "wifi",
            "cdid": "c372b197-86d7-4543-a23e-a9eea17a8411",
            "sys_region": "US",
            "os_api": "33",
            "uoo": "0",
            "timezone_name": "Asia/Karachi",
            "dpi": "440",
            "carrier_region": "US",
            "ac": "wifi",
            "device_id": "7185834406062409262",
            "pass-route": "1",
            "os_version": "13",
            "timezone_offset": "18000",
            "version_code": "110908",
            "carrier_region_v2": "310",
            "app_name": "tiktok_tv",
            "ab_version": "11.9.8",
            "version_name": "11.9.8",
            "device_brand": "google",
            "op_region": "US",
            "ssmix": "a",
            "pass-region": "1",
            "device_platform": "android",
            "build_number": "11.9.8",
            "region": "US",
            "aid": "4082",
            "ts": "1680110003"
        }

        payload = "keyword=%23{}&search_source=normal_search&cursor={}&count=10&query_correct_type=1".format(hashtag,str(cursor))
        headers = {
            "host": "api16-normal-useast5.us.tiktokv.com",
            "connection": "keep-alive",
            # "cookie": "store-idc=useast2a; store-country-code=pk; store-country-code-src=uid; odin_tt=caa491fb21fb86802e539fe0ce4d8a958d7369daea673bc2bd721718b628b659e20e01012da88ac17de2ad8837deac882495dbc541ea019fbc74ca5e9f566f03eb907b2359aa87873c4cb576c83dc75d; sid_guard=7c12a115d457427b13597c225440fb83%7C1672816668%7C5184000%7CSun%2C+05-Mar-2023+07%3A17%3A48+GMT; install_id=7192576472099800875; ttreq=1$a1ab1ef371a719d5062d2272030d686a449b04e8; uid_tt=fb259592c1f21de770c8a03fe733c1affd03f89ac9c52b8b42d0a5d88ff46a0e; uid_tt_ss=fb259592c1f21de770c8a03fe733c1affd03f89ac9c52b8b42d0a5d88ff46a0e; sid_tt=7c12a115d457427b13597c225440fb83; sessionid=7c12a115d457427b13597c225440fb83; sessionid_ss=7c12a115d457427b13597c225440fb83",
            "sdk-version": "2",
            # "x-tt-token": "047c12a115d457427b13597c225440fb83054f14cded39676b06ebe9acb72fa477bffe10002c6ca4ebd659d2f67d10c39d06aa3f79537e4def0e5e8ce8e64b0909ac1cabbddf1000be375a3528a59cbbd5f9a-1.0.0",
            "passport-sdk-version": "17",
            "x-ss-req-ticket": "1680110003545",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "x-ss-stub": "CB803E9F51B049E5DCF67162FFB45A06",
            "x-tt-store-idc": "useast5",
            "x-tt-store-region": "us",
            "x-tt-store-region-src": "did",
            "x-ss-dp": "4082",
            # "x-tt-trace-id": "00-2e5c26e41063b93651f421462e570ff2-2e5c26e41063b936-01",
            "user-agent": "com.tiktok.tv/110908 (Linux; U; Android 13; en_US; sdk_gphone64_arm64; Build/TPB4.220624.004; Cronet/TTNetVersion:a6246045 2021-11-26 QuicVersion:705d0b81 2021-08-12)",
            "accept-encoding": "gzip, deflate",
            # "x-khronos": "1680110003",
            # "x-gorgon": "84049009401015db7ff8a609674776e1b105eb3bec35920c7ce7"
        }

        response = requests.post(url, data=payload, headers=headers, params=querystring)
        cursor+=10
        for j in response.json()['data']:
            # print("whi")
            try:
                post_urls.append(j['aweme_info']["aweme_id"])
            except:
                return post_urls
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
existing_posts = open("record_posts.txt").read().split("\n")
for j in hastage_title:
    print("\n[++] Scrpaing hashaag #{} posts. This can take a while\n".format(j))
    j=j.replace("#","")
    posts=get_hashtag_videos(j)
    print("[++] Total {} posts Scraped".format(str(len(posts))))

    new_posts = [post for post in posts if post not in existing_posts]
    random.shuffle(new_posts)
    random_posts = random.sample(new_posts, number_of_post_each_hashtag)
    print(f"[++] {len(random_posts)} Random posts selected from {len(posts)}")

    for cc, post in enumerate(random_posts):
        try:
            print(f"\n[++] On post {cc+1} of total {len(random_posts)} for #{j}")
            if post in open("record_posts.txt").read().split("/n"):
                print("post already commented")
                continue
            time.sleep(4)
            
            # search_intent="snssdk1128://search/user/?keyword=%23{}".format(i)
            

            post_intent="am start -a android.intent.action.VIEW -d https://m.tiktok.com/v/{}.html com.zhiliaoapp.musically/com.ss.android.ugc.aweme.deeplink.AppLinkHandlerV2".format(post)
            d.shell(post_intent)

            time.sleep(3)


            try:
                combutton=d(resourceId="com.zhiliaoapp.musically:id/ax1")
                combutton.click()
            except:
                combutton=d(resourceId="com.zhiliaoapp.musically:id/axi")
                combutton.click()
                 
            time.sleep(4)

            counter_comment=0
            counter_like=0
            for k in range(10):
                # if counter_comment>=int(numberofreplies):
                #     break  
                for i in d(resourceId="com.zhiliaoapp.musically:id/e2g"):
                        reco=open("record.txt",encoding="utf-8")
                        record=[line.rstrip() for line in reco]
                        # like=i.sibling(resourceId="com.zhiliaoapp.musically:id/dl3")
                        # if like.exists():
                        #         # try:
                        #         like.click()
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
                            like=i.sibling(resourceId="com.zhiliaoapp.musically:id/dl3")
                            if like.exists():
                                    # try:
                                    like.click()
                                    # except:
                                    #     pass
                                    counter_like+=1
                            reply=i.sibling(resourceId="com.zhiliaoapp.musically:id/aya")
                            if reply.exists():
                                reply.click()
                                time.sleep(1)
                                random_line = random.choice([line.rstrip() for line in open("message_replies.txt", encoding="utf-8")])
                                edit=d(className="android.widget.EditText").send_keys(random_line)
                                send_button=d(resourceId="com.zhiliaoapp.musically:id/ayg")
                                send_button.click()
                                counter_comment+=1
                                print("[+] {} replied . total {} commented".format(name,str(counter_comment)))
                                countdown(int(time_pause))
                                if counter_comment>=int(numberofreplies):
                                    break 
                            if counter_comment>=int(daily_limit):
                                print("[-] Daily Limit Reached")
                                exit(0)
                            with open("record.txt","a+", encoding="utf-8") as rec:             
                                    rec.write(name+"\n")
                            with open("record_posts.txt","a+", encoding="utf-8") as rec:             
                                    rec.write(post+"\n")
                if counter_comment>=int(numberofreplies):
                    # print("break2")
                    break  
                    
                scrollable = d(scrollable=True, className="androidx.recyclerview.widget.RecyclerView", instance=0)
                scrollable.scroll.toEnd(max_swipes=1) 
        except Exception as e:
            print(e)
            print("Switching to next post")
            with open("record.txt","a+", encoding="utf-8") as rec:             
                    rec.write(name+"\n")
            with open("record_posts.txt","a+", encoding="utf-8") as rec:             
                    rec.write(post+"\n")
            continue
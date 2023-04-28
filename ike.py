from os import name
import uiautomator2 as u2
import time,random,configparser,os


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print('\rSleeping for {}...'.format(timeformat), end='', flush=True)
        time.sleep(1)
        t -= 1

print('''

 ▀█▀ █ █▄▀ ▀█▀ ▄▀▄ █▄▀   ▄▀▀ ▄▀▄ █▄ ▄█ █▄ ▄█ ██▀ █▄ █ ▀█▀   █   █ █▄▀ ██▀
  █  █ █ █  █  ▀▄▀ █ █   ▀▄▄ ▀▄▀ █ ▀ █ █ ▀ █ █▄▄ █ ▀█  █    █▄▄ █ █ █ █▄▄

version=tiktok version v28.6.5
''')
#tiktok version v28.6.5

config=configparser.ConfigParser()

config.read("config.ini")

device_id=config.get("settings","device_id")
tiktok_username=config.get("settings","tiktok_username")
post_url="https://vt.tiktok.com/ZS8bA5wV4/".split(",")#config.get("settings","post_url").split(",")
time_pause=int(config.get("settings","time_pause"))
daily_limit=int(config.get("settings","daily_limit"))
rest_between_likes_min=2#int(config.get("settings","rest_between_likes_min"))
rest_between_likes_max=3#int(config.get("settings","rest_between_likes_max"))
swipes="3".split(",")#(config.get("settings","swipes")).split(",")
d=u2.connect(device_id)

def check_keyboard(d):
    key=d(packageName="com.touchtype.swiftkey")
    if key.exists():
        d.press("back")
        time.sleep(0.3)
    else:
        return

for j,sw in zip(post_url,swipes):
    try:
        e=post_url
        post_intent="am start -a android.intent.action.VIEW -d {} com.zhiliaoapp.musically/com.ss.android.ugc.aweme.deeplink.AppLinkHandlerV2".format(j)
        d.shell(post_intent)
        time.sleep(8)
        post_intent="am start -a android.intent.action.VIEW -d {} com.zhiliaoapp.musically/com.ss.android.ugc.aweme.deeplink.AppLinkHandlerV2".format(j)
        d.shell(post_intent)
        time.sleep(8)
        # dq=d.dump_hierarchy()
        # with open("dump.xml","w") as f:
            
        combutton=d(resourceId="com.zhiliaoapp.musically:id/axi")
        combutton.click()
        # exit(1)
        # exit(1)
        time.sleep(4)
        counter=0
        for s in range(int(sw)):
            print("swipe number {}".format(str(s)))
            for i in d(className="android.view.ViewGroup",index=0):
                check_keyboard(d)

                reco=open("record.txt",encoding="utf8")
                record=[line.rstrip() for line in reco]
                
                checkname=i.sibling(resourceId="com.zhiliaoapp.musically:id/title")
                if checkname.exists():
                    # print("yes")
                    name=checkname.get_text()
                    na=name+","+j
                    if na in record:
                        # print("{} already liked".format(name))
                        continue
                    # print(name)å
                    check_keyboard(d)
                    like=i.sibling(className="android.widget.ImageView",index="6")
                    if like.exists():
                        like.click()
                        check_keyboard(d)
                        counter+=1
                        print("[+] {} comment liked. total {} liked".format(name,str(counter)))
                        countdown(random.randint(rest_between_likes_min,rest_between_likes_max))
                    else:
                        like=i.sibling(className="android.widget.ImageView",index="7")
                        if like.exists():
                            check_keyboard(d)
                            like.click()
                            counter+=1
                            print("[+] {} comment liked. total {} liked".format(name,str(counter)))
                            countdown(random.randint(rest_between_likes_min,rest_between_likes_max))
                            check_keyboard(d)
                    if counter%30==0:
                        print("[--] Pausing for {} seconds after every 30 Likes")
                        countdown(time_pause)
                    if counter>=int(daily_limit):
                        print("[-]]Daily Limit Reached")
                        exit(0)
                    with open("record.txt","a+",encoding="utf8") as rec:             
                            rec.write(name+","+j+"\n")
            # print("=============================================")
            try:
                scrollable = d(scrollable=True, className="androidx.recyclerview.widget.RecyclerView", instance=0)
                scrollable.scroll.toEnd(max_swipes=1)
            except:
                scrollable = d(scrollable=True, className="androidx.recyclerview.widget.RecyclerView", instance=0)
                scrollable.scroll.toEnd(max_swipes=1) 
    except Exception as e:
        print(e)
        print("\n[==]Switiching to next post\n")
        continue













# # for i in d(className="android.widget.FrameLayout").child(className="android.view.ViewGroup",index="0"):
# #     # print(i)
# #     morereply=i.sibling(resourceId="com.zhiliaoapp.musically:id/nz")
# #     # ddd=morereply.info
# #     # print(ddd)
# #     if morereply.exists():
# #         continue
# #     name=i.sibling(resourceId="com.zhiliaoapp.musically:id/title").get_text()
# #     print("Replying to User {}".format(name))
# #     ff=i.sibling(text="Reply",className="android.widget.TextView")
# #     if not  ff.exists():
# #         continue
# #     ff.click()
# #     time.sleep(2)
# #     d.press("back")
# #     time.sleep(2)

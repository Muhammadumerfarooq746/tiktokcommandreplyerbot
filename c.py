import requests

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

payload = "keyword=%23funny&search_source=normal_search&cursor=0&count=10&query_correct_type=1"
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

print(response.text)
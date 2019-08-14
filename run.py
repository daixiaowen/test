# coding:utf-8

# import logging
#
# basic_format = "%(asctime)s - %(levelname)s - %(message)s"
# logging.basicConfig(filename=r"all.log", format=basic_format)
#
# logging.info("this is a info...")



# import requests
#
#
# # url = "https://pay.kliwu.com/testpays"
# # res = requests.get(url)
# # print(res.text)
#
# url2 = "https://pay.kliwu.com/testpays/Home/OrderPay"
# payload = {
#     "PaySceneCode": "WeChatPay.KuaiFama",
#     "PayBankCode": "ICBC_DEBIT"
# }
# res2 = requests.post(url2, payload)
# print(res2.text)






# import requests
#
#
# url = "https://sdccbtest.kliwu.com/hf2/index.aspx"
#
# headers = {
#     "Content-Type": "application/x-www-form-urlencoded",
#     "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) "
#                   "Version/11.0 Mobile/15A372 Safari/604.1",
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/"
#               "signed-exchange;v=b3",
#     "Referer": "https://sdccbtest.kliwu.com/hf2/index.aspx",
#     "Cookie": "waits=93; Hm_lvt_b6bba2430fd1fc6259d2f1cdc6201a12=1565660468; ASP.NET_SessionId=riixry2a3fbcgejc4qmakvcj;"
#               " Hm_lpvt_b6bba2430fd1fc6259d2f1cdc6201a12=1565682526"
# }
#
# payload = {
#     # "__VIEWSTATE": "/wEPDwUKMTA3NDQ3ODM5Ng9kFgJmD2QWAgIDD2QWBAIBD2QWAgIHDxYCHgRUZXh0BZ4OPGRp"
#     #                "diBjbGFzcz0iYWN0aXZlX2Zsb2F0Ij4NCjxkaXYgY2xhc3M9Im1hc2siPiZuYnNwOzwvZGl2Pg0KPGRpd"
#     #                "iBjbGFzcz0iYWN0aXZlX2JnIj4NCjxpIGNsYXNzPSJjb2xzZV9idG4iPjwvaT4NCjxkaXYgY2xhc3M9ImZs"
#     #                "b2F0X3RleHQiPg0KPGgzPuS4gOOAgea0u+WKqOaXtumXtDwvaDM+DQoyMDE55bm0MeaciDHml6UtMjAxO"
#     #                "eW5tDPmnIgzMeaXpTxiciAvPg0KPGgzPuS6jOOAgea0u+WKqOWvueixoTwvaDM+DQrmtLvliqjmnJ/"
#     #                "pl7TvvIzmiJHooYzvvIjkuI3lkKvpnZLlspvvvInmiYvmnLrpk7booYzmlrDnrb7nuqblrqLmiLfkuIvo"
#     #                "vb3miYvmnLrpk7booYzlrqLmiLfnq6/ljbPlj6/mlK/ku5gx5YiG6ZKx6aKG5Y+W5paw5a6i5oi35aSn56S"
#     #                "85YyF44CC5aSn56S85YyF5YaF5a655YyF5ous77yaOTnotaLliLjjgIEy5byg5ruhMTDlh4815oq155So5Yi"
#     #                "477yI6aKG5Y+W5pel56ys5LqM5aSp55Sf5pWI77yM5pyJ5pWI5pyf5LiA5Liq5pyI77yJ5Y+K5ZaE6J6N"
#     #                "5ZWG5YqhMeWFg+i0rei1hOagvOOAgjxiciAvPg0KPGgzPuS4ieOAgea0u+WKqOWGheWuuTwvaDM+DQrmiYvmnLr"
#     #                "pk7booYznrb7nuqblrqLmiLflrozmiJDmiYvmnLrpk7booYzkuqTmmJPpobXpnaLngrnlh7vlub/lkYrmoI/ov5"
#     #                "vlhaUgICAgICAgICAgICAgICAgIOa0u+WKqOmhtemdou+8jOaUr+S7mDAuMDHlhYPljbPlj6/ojrflvpcxMOWF"
#     #                "g+ivnei0ueOAgg0KPGgzPuWbm+OAgea0u+WKqOinhOWImTwvaDM+DQoxLuacrOa0u+WKqOS7hemZkOWxseS4nO"
#     #                "WIhuihjO+8iOS4jeWQq+mdkuWym++8ieaJi+acuumTtuihjOaWsOetvue6puWPguS4ju+8jOavj+S6uuS7hemZkO"
#     #                "WPguS4jjHmrKHvvJvvvIjpnIDorr7liLbkuLrmlrDlrqLmiLflj4LkuI7vvIzlt7LmnInnuqbmg6DpvZDpsoHl"
#     #                "uJDlj7fnmoTlrqLmiLfkuI3og73lj4LliqDvvIk8YnIgLz4NCjIu5omL5py66K+d6LS55ruhMTDlh4815Yi444CC7"
#     #                "7yI55Sf5pWI5pel5pyf5Li66aKG5Y+W5pel5qyh5pel77yM5pyJ5pWI5pyf5LiA5Liq5pyI44CC77yJPGJyIC8+D"
#     #                "QozLuacrOa0u+WKqOS7heaUr+aMgeW7uuihjOWAn+iusOWNoeaUr+S7mO+8jOS4jeaUr+aMgeS/oeeUqOWNoeaUr+"
#     #                "S7mO+8mzxiciAvPg0KNC7nlKjmiLflpoLmnInkuIvov7Dku7vkvZXkuIDnp43mg4XlhrXnmoTov53op4TooYzkuL"
#     #                "rvvIzlhbblj4LliqDmnKzmrKHmtLvliqjnmoTotYTmoLzlsIbooqvlj5bmtojvvIzlkIzml7blj5bmtojmiYDmnI"
#     #                "nlm6Dov53op4TooYzkuLrmiYDkuqfnlJ/nmoTmlLbnm4rjgILov53op4TooYzkuLrljIXlkKvkvYbkuI3pmZDkuo"
#     #                "7vvJrpgJrov4fpnZ7ms5XmiYvmrrXov5vooYzoiJ7lvIrjgIHomZrlgYfkuqTmmJPjgIHov53ms5XkuqTmmJPjgIE"
#     #                "g6LSm5oi354q25oCB5LiN5q2j5bi45Y+K5YW25LuW55u45YWz6L+d6KeE6KGM5Li644CCPGJyIC8+DQo1LuW7uuih"
#     #                "jOWxseS4nOecgeWIhuihjOWSjOS4iua1t+WcqOi1ouerr+eUteWtkOWVhuWKoeaciemZkOWFrOWPuOWcqOazleW+i+"
#     #                "iuuOWPr+iMg+WbtOWGheS/neeVmeWvueacrOa0u+WKqOWGheWuueeahOacgOe7iOino+mHiuadg+WSjOWPmOabtOadg"
#     #                "+OAgjxiciAvPg0K5oiR6KGM5pyJ5p2D5qC55o2u6ZyA6KaB6LCD5pW055u45YWz5rS75Yqo6KeE5YiZ77yM5bm26YC"
#     #                "a6L+H55u45YWz6YCU5b6E77yI5aaC5rS75Yqo572R56uZ44CB5YiG5pSv572R54K5562J77yJ5YWs5ZGK5ZCO55Sf5pW"
#     #                "I44CCPGJyIC8+DQrmtLvliqjlpZblk4HnlLHlkIjkvZzlhazlj7jkuIrmtbflnKjotaLnq6/nlLXlrZDllYbliqHmnI"
#     #                "npmZDlhazlj7jmj5DkvpvvvIzlrqLmnI3ng63nur/vvJo0MDAtMDIxLTgxMTUuPC9kaXY+DQo8L2Rpdj4NCjwvZGl2Pm"
#     #                "QCAw8WAh8ABaUCPHNjcmlwdCB0eXBlPSJ0ZXh0L2phdmFzY3JpcHQiPg0KdmFyIF9iZGhtUHJvdG9jb2wgPSAoKCJodH"
#     #                "RwczoiID09IGRvY3VtZW50LmxvY2F0aW9uLnByb3RvY29sKSA/ICIgaHR0cHM6Ly8iIDogIiBodHRwOi8vIik7DQpkb"
#     #                "2N1bWVudC53cml0ZSh1bmVzY2FwZSgiJTNDc2NyaXB0IHNyYz0nIiArIF9iZGhtUHJvdG9jb2wgKyAiaG0uYmFpZHU"
#     #                "uY29tL2guanMlM0ZiNmJiYTI0MzBmZDFmYzYyNTlkMmYxY2RjNjIwMWExMicgdHlwZT0ndGV4dC9qYXZhc2NyaXB0"
#     #                "JyUzRSUzQy9zY3JpcHQlM0UiKSk7DQo8L3NjcmlwdD5kZMNfIXlmZ9eWyz5Vy4GeutEqFf/vxFugRUfaOnBObl1+",
#     # "__VIEWSTATEGENERATOR": "ED91D3D3",
#     # "__EVENTVALIDATION": "/wEdAASqQO0BB/5tbf9qdhsRPoXCPfHTZG3A71qJiM2NqVK39bDG4LetRO2ErbZBKvDEd2zhILSyFbY3gvx"
#     # "yd+dUIDZWk30meCAs0LITwuMkdPGDNYFzaJlLE7AtkqziifIjfLI=",
#     "ctl00$ContentPlaceHolder1$mobile": "18702172937",
#     "ctl00$ContentPlaceHolder1$code": "392064",
#     # "ctl00$ContentPlaceHolder1$btnPay": "立即领取大礼包"
# }
#
# res = requests.post(url, headers, payload)
# print(res.history)
# print(res.text)



import webbrowser
webbrowser.open("http://www.baidu.com")
webbrowser.open_new("http://news.baidu.com")
webbrowser.open_new_tab("http://map.baidu.com")


# w = webbrowser.get("http://www.baidu.com")





















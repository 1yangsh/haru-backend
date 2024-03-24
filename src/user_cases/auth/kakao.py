import json
import os
import requests


class UserKakaoAuthHandler:
    def __init__(self, code):
        self.code = code
        self.default_header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Cache-Control": "no-cache",
        }
    
    def handle(self):
        token = self.get_token(self.code)
        print(token)
        self.get_userInfo(token["access_token"])
    
    def get_authorize(self):
        url = "https://kauth.kakao.com/oauth/authorize"
        data = {
            "client_id": os.getenv("OAUTH_KAKAO_SECRET"),
            "client_secret": os.getenv("OAUTH_KAKAO_SECRET"),
            "redirect_url": os.getenv("OAUTH_KAKAO_REDIRECT_URL"),
            "response_type": "code",
        }
        response = requests.get(url, data=data)
        print(response)
    
    def get_token(self, code):
        url = "https://kauth.kakao.com/oauth/token"
        data = {
            "grant_type": "authorization_code",
            "client_id": os.getenv("OAUTH_KAKAO_REST_API_KEY"),
            "client_secret": os.getenv("OAUTH_KAKAO_SECRET"),
            "redirect_uri": os.getenv("OAUTH_KAKAO_REDIRECT_URL"),
            "code": code
        }
        response = requests.post(url, data=data)
        tokens = response.json()
        
        # 토큰을 파일로 저장하기
        if "access_token" in tokens:
            with open(f"kakao_token_{code}.json", "w") as fp:
                json.dump(tokens, fp)
                print("Tokens saved successfully")
        else:
            print(tokens)
        return tokens
            
    def get_userInfo(self, token):
        url = "https://kapi.kakao.com/v2/user/me"
        response = requests.post(
            url=url,
            headers={
                **self.default_header,
                **{"Authorization": f"Bearer {token}"}
            },
            data={}
        )
        user_info = response.json()
        print(user_info)
        
            
        
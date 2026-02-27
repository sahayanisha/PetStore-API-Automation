import requests
import logging



class APIClient:
    def __init__(self, baseurl):
        self.baseurl = baseurl
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})



    def request(self,method,endpoint,payload = None, params = None):
        url = f'{self.baseurl}{endpoint}'
        response = self.session.request(method=method,url=url,json=payload,params=params)
        logging.info(f"{method}{url}")
        logging.info(f"Status code: {response.status_code}")
        logging.info(f"Response text: {response.text}")
        return response

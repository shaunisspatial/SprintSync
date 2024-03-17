# imports
import requests
from .models import TimeEntry

#class
class TogglClient:
    def __init__(self):
        self.root_url = 'https://api.track.toggl.com'
        self.api_version = 'v9'
        self.base_headers = {'Content-Type': 'application/json'}
    def _req(self, verb, endpoint, headers, params = None, data = None, auth=None):
        s = requests.Session()
        auth_tuple = (auth, 'api_token')
        url = self.root_url+f'/api/{self.api_version}/{endpoint}'
        if verb == 'GET':
            r = s.get(url=url, headers=headers, auth=auth_tuple)
            return r
        if verb == 'POST':
            print('nothing here')
        if verb == 'PUT':
            print('nothing here')

    def get_time_entries(self, auth):
        endpoint = 'me/time_entries'
        req= self._req(verb='GET', endpoint=endpoint, headers=self.base_headers, auth=auth)
        req.raise_for_status()
        req_json = req.json()
        resp_list = []
        for json in req_json:
            time_entry = TimeEntry(**json)
            resp_list.append(time_entry)
        return resp_list

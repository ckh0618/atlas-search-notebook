import requests
from requests.auth import HTTPDigestAuth
import json 

class SearchIndexManager:

    def __init__(self, pub: str, pri: str, project_id: str, cluster_name: str):
        self.pub = pub
        self.pri = pri
        self.base_url = "https://cloud.mongodb.com/api/atlas/v1.0/groups/{}/clusters/{}/fts/indexes". \
            format(project_id, cluster_name)
        self.headers = {'Content-Type': 'application/json'}

    def create_index(self, d: dict):
        return requests.post(self.base_url, auth=HTTPDigestAuth(self.pub, self.pri),
                             headers=self.headers,
                             data=json.dumps(d)).status_code

    def get_indexes(self, db: str, coll: str):
        get_url = self.base_url + "/{}/{}".format(db, coll)
        return requests.get(get_url, auth=HTTPDigestAuth(self.pub, self.pri), headers=self.headers).json()

    def delete_index(self, id):
        delete_url = self.base_url + "/{}".format(id)
        return requests.delete(delete_url, auth=HTTPDigestAuth(self.pub, self.pri), headers=self.headers).status_code

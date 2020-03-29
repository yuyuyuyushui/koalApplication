from core.rest_client2 import *

class Config_first(RestClient2):
    def __init__(self,**kwargs):
        super(Config_first, self).__init__(**kwargs)

    def get_key(self, appTag, nodeId, profileTag, **kwargs):
        return self.get("/v1/api/config/{}/{}/{}/hello".format(appTag, nodeId, profileTag), **kwargs)

    def get_token(self,appTag, nodeId, profileTag,**kwargs):
        # self.session.headers["Content-Type"] = "application/json"
        print(self.session.headers)
        return self.post("/v1/api/config/{}/{}/{}/hello".format(appTag,nodeId,profileTag),**kwargs)

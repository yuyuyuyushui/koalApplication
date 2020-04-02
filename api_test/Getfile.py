from core.rest_client2 import *


class Config_seconde(RestClient1):
    def __init__(self,**kwargs):
        super(Config_seconde, self).__init__(**kwargs)

    def Authentication(self,appTag,nodeId,profileTag):
        print(self.session.headers)
        return self.get("/v1/api/config/{}/{}/{}/all".format(appTag,nodeId,profileTag))

    def query_config(self,appTag,nodeId,profileTag):
        return self.get("/v1/api/config/{}/{}/{}/update".format(appTag,nodeId,profileTag))
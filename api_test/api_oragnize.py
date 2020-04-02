from core.rest_client2 import *


class Api_orage(RestClient2):
    def __init__(self,**kwargs):
        super(Api_orage,self).__init__(**kwargs)

    def dept_sync(self,**kwargs):
        """
        组织机构同步接口
        :param kwargs:
        :return:
        """
        return self.post("/v1/app/third/sync/dept",**kwargs)

    def user_account_sync(self, **kwargs):

        return self.post("/v1/app/third/sync/user",**kwargs)

    def abs_sync(self, **kwargs):

        return self.post("/v1/app/third/sync/abis",**kwargs)

    def res_sync(self, **kwargs):

        return self.post("/v1/app/third/sync/res", **kwargs)

    def res_account_sync(self, **kwargs):

        return self.post("/v1/app/third/sync/account", **kwargs)

    def query_res_account_secure(self, **kwargs):

        return self.post("/v1/app/third/sync/queryPwd", **kwargs)

    def authorize_relation(self, **kwargs):

        return self.post("/v1/app/third/sync/authorized", **kwargs)

    def session_post(self,**kwargs):
        return self.post("/v1/app/third/session/submit",**kwargs)

    def history_session(self, **kwargs):
        return self.post("/v1/app/third/session/list",**kwargs)

    def reply_data(self, **kwargs):
        return self.post("/v1/app/third/session/replay",**kwargs)

    def cmd_session(self, **kwargs):
        return self.post("/v1/app/third/session/record",**kwargs)
if __name__=="__main__":
    pass
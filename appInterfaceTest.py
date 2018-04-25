#!/usr/bin/evn python3
# -*- coding: UTF-8 -*-
from cpxApp import createSign
import json

class appInterfaceTest(createSign):
    def __init__(self):
        self.loginToken=''
        super(appInterfaceTest,self).__init__()

    def cpxlogin(self):
        result=self.post('/app/user/login')
        self.loginToken = (json.loads(result.text)['data']['token'])
        return result

    def cpxSystem(self):
        return self.get('/app/user/system',self.loginToken)

    def cpxVersion(self):
        return self.get('/app/system/version',self.loginToken)

    def cpxGetSpinnerLaunchList(self):
        return self.get('/app/expense/getSpinnerLaunchList',self.loginToken)

    def cpxInviteNum(self):
        return self.get('/app/shop/inviteNum',self.loginToken)

    def cpxGetWaitDealCount(self):
        return self.get('/app/expense/getWaitDealCount',self.loginToken)

    def cpxPersonCenter(self):
        return self.get('/app/user/personCenter',self.loginToken)

    def cpxAppIndex(self):
        return self.get('/app/user/personCenter',self.loginToken)

    def cpxViewInventoryShopList(self):
        return self.get('/app/statistics/viewInventoryShopList',self.loginToken)

    def cpxGetAllShopCategoryList(self):
        return self.get('/app/statistics/getAllShopCategoryList',self.loginToken)


result=appInterfaceTest()
result.cpxlogin()
# result.cpxSystem()
# result.cpxVersion()
# result.cpxGetSpinnerLaunchList()
# result.cpxInviteNum()
# result.cpxGetWaitDealCount()
# result.cpxPersonCenter()
# result.cpxAppIndex()
print('===========================登录模块接口完成==========================')
#result.cpxViewInventoryShopList()
result.cpxGetAllShopCategoryList()

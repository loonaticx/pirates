# uncompyle6 version 3.2.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.login.AccountServerConstants
from pandac.PandaModules import *
from RemoteValueSet import *
from direct.directnotify import DirectNotifyGlobal
import TTAccount, HTTPUtil

class AccountServerConstants(RemoteValueSet):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('AccountServerConstants')

    def __init__(self, cr):
        self.expectedConstants = [
         'minNameLength', 'minPwLength', 'allowNewAccounts', 'freeTrialPeriodInDays', 'priceFirstMonth', 'pricePerMonth', 'customerServicePhoneNumber', 'creditCardUpFront']
        self.defaults = {'minNameLength': '1', 'minPwLength': '1', 'allowNewAccounts': '1', 'creditCardUpFront': '0', 'priceFirstMonth': '9.95', 'pricePerMonth': '9.95'}
        noquery = 1
        if cr.productName == 'DisneyOnline-US':
            if base.config.GetBool('tt-specific-login', 0):
                pass
            else:
                noquery = 0
        if cr.accountOldAuth or base.config.GetBool('default-server-constants', noquery):
            self.notify.debug('setting defaults, not using account server constants')
            self.dict = {}
            for constantName in self.expectedConstants:
                self.dict[constantName] = 'DEFAULT'

            self.dict.update(self.defaults)
            return
        url = URLSpec(AccountServerConstants.getServer())
        url.setPath('/constants.php')
        self.notify.debug('grabbing account server constants from %s' % url.cStr())
        RemoteValueSet.__init__(self, url, cr.http, expectedHeader='ACCOUNT SERVER CONSTANTS', expectedFields=self.expectedConstants)

    def getBool(self, name):
        return self.__getConstant(name, RemoteValueSet.getBool)

    def getInt(self, name):
        return self.__getConstant(name, RemoteValueSet.getInt)

    def getFloat(self, name):
        return self.__getConstant(name, RemoteValueSet.getFloat)

    def getString(self, name):
        return self.__getConstant(name, RemoteValueSet.getString)

    def __getConstant(self, constantName, accessor):
        if constantName not in self.expectedConstants:
            self.notify.warning("requested constant '%s' not in expected constant list; if it's a new constant, add it to the list" % constantName)
        return accessor(self, constantName)

    @staticmethod
    def getServer():
        return TTAccount.getAccountServer().cStr()

    @staticmethod
    def getServerURL():
        return TTAccount.getAccountServer()
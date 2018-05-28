# uncompyle6 version 3.2.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.login.LoginTTAccount
from pandac.PandaModules import *
from direct.distributed.MsgTypes import *
from direct.directnotify import DirectNotifyGlobal
import LoginBase, TTAccount
from TTAccount import TTAccountException
from direct.distributed.PyDatagram import PyDatagram

class LoginTTAccount(LoginBase.LoginBase, TTAccount.TTAccount):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('LoginTTAcct')

    def __init__(self, cr):
        LoginBase.LoginBase.__init__(self, cr)
        TTAccount.TTAccount.__init__(self, cr)
        self.useTTSpecificLogin = base.config.GetBool('tt-specific-login', 0)
        self.notify.info('self.useTTSpecificLogin =%s' % self.useTTSpecificLogin)

    def supportsRelogin(self):
        return 1

    def sendLoginMsg(self):
        cr = self.cr
        datagram = PyDatagram()
        if self.useTTSpecificLogin:
            datagram.addUint16(CLIENT_LOGIN_TOONTOWN)
            self.__addPlayToken(datagram)
            datagram.addString(cr.serverVersion)
            datagram.addUint32(cr.hashVal)
            self.__addTokenType(datagram)
            datagram.addString(cr.wantMagicWords)
        else:
            datagram.addUint16(CLIENT_LOGIN_2)
            self.__addPlayToken(datagram)
            datagram.addString(cr.serverVersion)
            datagram.addUint32(cr.hashVal)
            self.__addTokenType(datagram)
            datagram.addString(cr.validateDownload)
            datagram.addString(cr.wantMagicWords)
        cr.send(datagram)

    def resendPlayToken(self):
        cr = self.cr
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_SET_SECURITY)
        self.__addPlayToken(datagram)
        self.__addTokenType(datagram)
        cr.send(datagram)

    def __addPlayToken(self, datagram):
        self.playToken = self.playToken.strip()
        datagram.addString(self.playToken)

    def __addTokenType(self, datagram):
        if self.useTTSpecificLogin:
            datagram.addInt32(CLIENT_LOGIN_3_DISL_TOKEN)
        else:
            if self.playTokenIsEncrypted:
                datagram.addInt32(CLIENT_LOGIN_2_PLAY_TOKEN)
            else:
                datagram.addInt32(CLIENT_LOGIN_2_PLAY_TOKEN)

    def getErrorCode(self):
        return self.response.getInt('errorCode', 0)

    def needToSetParentPassword(self):
        return self.response.getBool('secretsPasswordNotSet', 0)

    def authenticateParentPassword(self, loginName, password, parentPassword):
        if base.cr.withParentAccount:
            self.notify.error('authenticateParentPassword called, but with parentAccount')
            try:
                errorMsg = self.talk('authenticateParentUsernameAndPassword', data=self.makeLoginDict(loginName, parentPassword))
                if not errorMsg:
                    return (1, None)
                if self.response.getInt('errorCode') in (5, 72):
                    return (0, None)
                return (
                 0, errorMsg)
            except TTAccountException, e:
                return (
                 0, str(e))

        else:
            if self.useTTSpecificLogin:
                try:
                    errorMsg = self.talk('authenticateParentPasswordNewStyle', data=self.makeLoginDict(loginName, parentPassword))
                    if not errorMsg:
                        return (1, None)
                    if self.response.getInt('errorCode') in (5, 72):
                        return (0, None)
                    return (
                     0, errorMsg)
                except TTAccountException, e:
                    return (
                     0, str(e))

            else:
                return TTAccount.TTAccount.authenticateParentPassword(self, loginName, password, parentPassword)
        return

    def authenticateDelete(self, loginName, password):
        if self.useTTSpecificLogin:
            try:
                errorMsg = self.talk('authenticateDeleteNewStyle', data=self.makeLoginDict(loginName, password))
                if not errorMsg:
                    return (1, None)
                if self.response.getInt('errorCode') in (5, 72):
                    return (0, None)
                return (
                 0, errorMsg)
            except TTAccountException, e:
                return (
                 0, str(e))

        else:
            self.notify.info('using old style authenticate delete')
            result = TTAccount.TTAccount.authenticateDelete(self, loginName, password)
            return result
        return
# uncompyle6 version 3.2.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)]
# Embedded file name: pirates.teleport.DistributedTeleportActor
from pirates.teleport.DistributedFSM import DistributedFSM

class DistributedTeleportActor(DistributedFSM):
    __module__ = __name__

    def __init__(self, cr, name):
        DistributedFSM.__init__(self, cr, name)
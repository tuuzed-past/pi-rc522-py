# coding=utf8
from rc522 import MFRC522
import util


class Reader(object):
    def __init__(self, dev='/dev/spidev0.0', speed=500000):
        self.reader = MFRC522(dev, speed)
        self.MI_OK = self.reader.MI_OK
        self.MI_NO_TAG_ERR = self.reader.MI_NO_TAG_ERR
        self.MI_ERR = self.reader.MI_ERR

    def __common(self, sector, block, key=None, data=None):
        if key is None:
            key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
        uid = None
        backData = None
        status, TagType = self.reader.MFRC522_Request(self.reader.PICC_REQIDL)
        if status == self.MI_OK:
            status, uid = self.reader.MFRC522_Anticoll()
            if status == self.MI_OK:
                self.reader.MFRC522_SelectTag(uid)
                blockAddr = util.toBlockAddr(sector, block)
                status = self.reader.MFRC522_Auth(self.reader.PICC_AUTHENT1A, blockAddr, key, uid)
                if status == self.MI_OK:
                    if data is not None:
                        self.reader.MFRC522_Write(blockAddr, data)
                    status, backData, backLen = self.reader.MFRC522_Read(blockAddr)
                    self.reader.MFRC522_StopCrypto1()
        return status, uid, backData

    def read(self, sector, block, key=None):
        return self.__common(sector, block, key)

    def write(self, sector, block, data, key=None, ):
        return self.__common(sector, block, key, data)

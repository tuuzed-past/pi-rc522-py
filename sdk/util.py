# coding=utf8
def toBlockAddr(sector, block):
    return 4 * (sector - 1) + block


def __hex2oct(arg):
    if type(arg) == int:
        temp = str(arg)
    else:
        temp = int(arg, 16)
    temp = str(temp)
    if len(temp) == 1:
        temp = '00' + temp
    elif len(temp) == 2:
        temp = '0' + temp
    return temp


def __oct2hex(arg):
    if type(arg) == int:
        temp = hex(arg)
    else:
        temp = hex(int(arg))
    temp = temp.upper().replace('0X', '')
    if len(temp) == 1:
        temp = '0' + temp
    return temp


def hex2oct(args):
    if type(args) != list:
        args = [args, ]
    temp = ''
    for arg in args:
        temp += __hex2oct(arg)
        temp += ','
    return temp[:-1]


def oct2hex(args):
    if type(args) != list:
        args = [args, ]
    temp = ''
    for arg in args:
        temp += __oct2hex(arg) + ','
    return temp[:-1]


def __test():
    hexData = [0xC5, 0xF2, 0x94, 0x35, 0x96]
    hexData2 = ['0xC5', '0xF2', '0x94', '0x35', '0x96']
    octData = [197, 242, 148, 053, 150]
    octData2 = ['197', '242', '148', '053', '150']
    print hex2oct(hexData)
    print hex2oct(hexData2)
    print oct2hex(octData)
    print oct2hex(octData2)


if __name__ == '__main__':
    __test()
    import time

    print time.time()

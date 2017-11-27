# coding=utf8
import os
import signal

import time

from sdk import reader as sdk_reader, util as sdk_util


def end_read(sig, frame):
    global continue_reading
    print('Ctrl+C captured, ending read.')
    continue_reading = False


signal.signal(signal.SIGINT, end_read)

continue_reading = True

print('Press Ctrl-C to stop.')

while continue_reading:
    reader = sdk_reader.Reader()
    status, uid, data = reader.read(2, 4)
    if status == reader.MI_OK and len(uid) == 5 and len(data) == 16:
        if not os.path.exists('data'):
            os.mkdir('data')
        UID = sdk_util.oct2hex(uid)
        DATA = sdk_util.oct2hex(data)
        print 'UID: ' + UID
        print 'DATA: ' + DATA
        with open('data/data.txt', 'a') as f:
            f.write('type=read;uid=%s;data=%s;time=%s\n' % (UID, DATA, time.time()))

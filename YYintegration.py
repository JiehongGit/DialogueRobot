# coding: utf-8

import os
import time
import YYsynthesis
import Turling
import YYrecognition

tok = YYrecognition.get_access_token()

switch = True
while switch:
    os.system('sudo arecord -D "plughw:1" -f S16_LE -r 16000 -d 3 /home/pi/Desktop/voice.wav')
    time.sleep(0.5)
    info = YYrecognition.asr_main("/home/pi/Desktop/voice.wav",tok)
    if '关闭'.encode("utf-8") in info:
        while True:
            os.system('sudo arecord -D "plughw:1" -f S16_LE -r 16000 -d 10 /home/pi/Desktop/voice.wav')
            time.sleep(10)

            info = YYrecognition.asr_main("/home/pi/Desktop/voice.wav",tok)
            if '开启'.encode("utf-8") in info:
                break

        url = "http://tsn.baidu.com/text2audio?tex=开启成功&lan=zh&cuid=B8-27-EB-BA-24-14&ctp=1&tok="+tok+"&per=3"
        os.system('mpg123 "%s"'%url)


    elif '暂停'.encode("utf-8") in info:
        url = "http://tsn.baidu.com/text2audio?tex=开始暂停&lan=zh&cuid=B8-27-EB-BA-24-14&ctp=1&tok="+tok+"&per=3"
        os.system('mpg123 "%s"'%url)
        time.sleep(10)

        url = "http://tsn.baidu.com/text2audio?tex=暂停结束&lan=zh&cuid=B8-27-EB-BA-24-14&ctp=1&tok="+tok+"&per=3"
        os.system('mpg123 "%s"'%url)
        continue


    else:
        tex = Turling.Tuling(info)
        url = YYsynthesis.YYsynthesis_api(tok,tex)
        os.system('mpg123 "%s"'%url)
        time.sleep(0.5)
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket
import json
import time
import os

def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8700))
    return client

def stop(client):
    data = {}
    params = {}
    params['all'] = True
    data['type'] = "stop"
    data['params'] = params
    js = json.dumps(data)
    client.send((js + '\n#End\n').encode('utf-8'))

def playText(client, zIndex, content, top, left, width, height, screenMode, screenRotate, color, bgcolor, font_size, align, style):
    data = {}
    params = {}
    params['zIndex'] = zIndex
    params['content'] = content
    params['top'] = top
    params['left'] = left
    params['width'] = width
    params['height'] = height
    params['screen_mode'] = screenMode
    params['screen_rotate'] = screenRotate
    params['color'] = color
    params['bgcolor'] = bgcolor
    params['font_size'] = font_size
    params['align'] = align
    params['style'] = style
    data['id'] = ("PLAY_TEXT_%d") % (int(round(time.time() * 1000)))
    data['type'] = "play"
    data['libName'] = 'text'
    data['params'] = params
    js = json.dumps(data)
    client.send((js + '\n#End\n').encode('utf-8'))

def playScroll(client, zIndex, content, top, left, width, height, screenMode, screenRotate, color, font_size, style, speed):
    data = {}
    params = {}
    params['zIndex'] = zIndex
    params['content'] = content
    params['top'] = top
    params['left'] = left
    params['width'] = width
    params['height'] = height
    params['screen_mode'] = screenMode
    params['screen_rotate'] = screenRotate
    params['color'] = color
    params['font_size'] = font_size
    params['style'] = style
    params['speed'] = speed
    data['id'] = ("PLAY_SCROLL_%d") % (int(round(time.time() * 1000)))
    data['type'] = "play"
    data['libName'] = 'scroll'
    data['params'] = params
    js = json.dumps(data)
    client.send((js + '\n#End\n').encode('utf-8'))

def playScrollBackground(client, zIndex, top, left, width, height, screenMode, screenRotate, bgcolor):
    data = {}
    params = {}
    params['zIndex'] = zIndex
    params['top'] = top
    params['left'] = left
    params['width'] = width
    params['height'] = height
    params['screen_mode'] = screenMode
    params['screen_rotate'] = screenRotate
    params['bgcolor'] = bgcolor
    data['id'] = ("PLAY_BACKGROUND_%d") % (int(round(time.time() * 1000)))
    data['type'] = "play"
    data['libName'] = 'background'
    data['params'] = params
    js = json.dumps(data)
    client.send((js + '\n#End\n').encode('utf-8'))
    
def play(client, libName, zIndex, path, top, left, width, height, screenMode, screenRotate):
    data = {}
    params = {}
    params['zIndex'] = zIndex
    params['path'] = path
    params['top'] = top
    params['left'] = left
    params['width'] = width
    params['height'] = height
    params['screen_mode'] = screenMode
    params['screen_rotate'] = screenRotate
    data['id'] = ("PLAY_VIDEO_%d") % (int(round(time.time() * 1000)))
    data['type'] = "play"
    data['libName'] = libName
    data['params'] = params
    js = json.dumps(data)
    client.send((js + '\n#End\n').encode('utf-8'))

def getFiles(str):
    fs = []
    for root,dirs,files in os.walk(str):
        for file in files:
            fs.append(str + '/' + file)
    return fs

if __name__ == '__main__':

    # ????????????
    client = connect()

    # ????????????
    stop(client)

    # ????????????
    playText(client,
             3,
             '???????????????(Raspberry Pi)???????????????????????????',
             0, 0, 1920, 50,
             'landscape', 0,
             'rgba(255, 0, 0, 100%)', 'rgba(255, 255, 255, 20%)', 30, 'center', 'bold')

    # ??????????????????
    playScroll(client,
               4,
               '???????????????(Raspberry Pi)????????????????????????????????????(?????????????????????????????????????????????????????????????????????????????????????????????)',
               100, 0, -1, 50,
               'landscape', 0, 'rgba(0, 0, 255, 100%)', 18, 'bold', 2)

    # ??????????????????????????????
    playScrollBackground(client,
                         5,
                         100, 0, 1920, 50,
                         'landscape', 0, 'rgba(255, 255, 255, 20%)')

    # ????????????
    while True:

        # ????????????????????????
        fs = getFiles(r'E:\test')
        if len(fs) == 0 :
            time.sleep(5)
            continue

        # ????????????
        for f in fs:
            # ???????????????
            if f.endswith(".mp4") :
                # ????????????
                play(client, "video", 10, f, 0, 0, 1920, 1080, "landscape", 0)
            # ???????????????
            if f.endswith(".jpg") or f.endswith(".png") :
                # ????????????
                play(client, "pic", 10, f, 0, 0, 1920, 1080, "landscape", 0)
            # ??????5s??????
            time.sleep(5)

    # ????????????
    client.close()


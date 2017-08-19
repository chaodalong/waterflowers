# -*- coding: utf-8 -*-
def md5(str=None):
    import hashlib
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()

def playVoice(file=None):
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(1, start=0.0)

def run_order(order):
    import flask
    current_app = flask.current_app
    ORDERS = current_app.config.get('ORDERS')
    if order in ORDERS:
        voice_file = current_app.root_path + '/' + ORDERS[order]['voice']
        # 播放声音
        #print voice_file
        playVoice(voice_file)
        if order == 'begin_water' or order == 'stop_water':
            # 发送GPIO信号
            send_gpio_order(ORDERS[order]['gpio_info'])
    else:
        return False

'''
    type in(GPIO.IN) out(GPIO.OUT)
    value 1 GPIO.HIGH 0 GPIO.LOW
'''
def send_gpio_order(param):
    channel, type, value = param
    try:
        import RPi.GPIO as GPIO
    except RuntimeError:
        print("引入错误")
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    if type == 'in':
        GPIO.setup(channel, GPIO.IN)
        GPIO.input(channel, value)
    else:
        GPIO.setup(channel, GPIO.OUT)
        GPIO.output(channel, value)

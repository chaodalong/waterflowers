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
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(1, start=0.0)
    # 阻塞进程
    while True:
        if not pygame.mixer.music.get_busy():
            break
    # 关闭播放
    pygame.mixer.music.stop()

def run_order(order):
    import flask,time
    current_app = flask.current_app
    ORDERS = current_app.config.get('ORDERS')
    if order in ORDERS:
        voice_file = current_app.root_path + '/' + ORDERS[order]['voice']
        if order == 'begin_water':
            ''' 
            开始浇花：先播放声音，再接通水泵
            '''
            playVoice(voice_file)
            time.sleep(1)
            send_gpio_order(ORDERS[order]['gpio_info'])
        elif order == 'auto_stop_water' or order == 'stop_water':
            ''' 
            停止浇花：先断开水泵，再播放声音（防止水益处）
            '''
            send_gpio_order(ORDERS[order]['gpio_info'])
            playVoice(voice_file)
    else:
        return False

'''
    type in(GPIO.IN) out(GPIO.OUT)
    value 1 GPIO.HIGH 0 GPIO.LOW
'''
def send_gpio_order(param):
    print param
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

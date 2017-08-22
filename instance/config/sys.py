HOST="127.0.0.1"

DEBUG = True

SECRET_KEY = "A0Zr98j/3yX R~XLL!jmN]LWX/,?RT"

# 指令
ORDERS = {
    'begin_water': {
        'voice': 'static/voice/begin_water.mp3',
        'gpio_info': (22, 'out', 1)  # 22引脚 输出 高电平
    },
    'stop_water': {
        'voice': 'static/voice/stop_water.mp3',
        'gpio_info': (22, 'out', 0)
    },
    'auto_stop_water': {
        'voice': 'static/voice/auto_stop_water.mp3',
        'gpio_info': (22, 'out', 0)
    },
}

DATABASE = 'mysql+pymysql://root:123456@127.0.0.1:3306/waterflowers?charset=utf8'

# 指令
ORDERS = {
    'begin_water': {
        'voice': 'static/voice/begin_water.mp3',
        'gpio_info': (22, 'out', 1) # 22引脚 输出 高电平
    },
    'stop_water': {
        'voice': 'static/voice/stop_water.mp3',
        'gpio_info': (22, 'out', 0)
    },
    'auto_stop_water': {
        'voice': 'static/voice/auto_stop_water.mp3',
        'gpio_info': (22, 'out', 0)
    },
}


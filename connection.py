import nonebot
import config
from os import path
if __name__ == "__main__":
    nonebot.init(config)
    nonebot.load_builtin_plugins()
    nonebot.load_plugins(path.join(path.dirname(__file__), 'plugins','example'), 'plugins.example')
    nonebot.load_plugins(path.join(path.dirname(__file__), 'plugins','management'), 'plugins.management')
    nonebot.load_plugins(path.join(path.dirname(__file__), 'plugins','repeat'), 'plugins.repeat')
    nonebot.load_plugins(path.join(path.dirname(__file__), 'plugins','twitter','notification'), 'plugins.twitter.notification')
    nonebot.load_plugins(path.join(path.dirname(__file__), 'plugins','twitter','translation'), 'plugins.twitter.translation')
    nonebot.load_plugins(path.join(path.dirname(__file__), 'plugins','call'), 'plugins.call')
    nonebot.run(host='127.0.0.1', port = 8087)

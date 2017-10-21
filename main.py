#coding: UTF-8
import os
import web
import menu

from weixinInterface import WeixinInterface

urls = (
'/wx','WeixinInterface'
)

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
    
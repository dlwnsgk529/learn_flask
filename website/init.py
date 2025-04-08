# __name__ : 현재 .py 파일의 이름을 이 변수가 문자열로 가지고 있게 된다.
# if __name__ == '__main__': 현재 스크립트 파일이 시작점인지 판단

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'meh'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_refix='/')

    return app
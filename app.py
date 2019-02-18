# -*- coding: utf-8 -*-

from sanic import Sanic
from sanic.response import json
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User

app = Sanic()

# 数据库配置
app.config.DB_HOST = 'localhost'
app.config.DB_PORT = '5433'
app.config.DB_NAME = 'logodesigner'
app.config.DB_USER = 'logo'
app.config.DB_PASSWORD = 'logo'

url = 'postgresql+psycopg2://%s:%s@%s:%s/%s'%(
    app.config.DB_USER,
    app.config.DB_PASSWORD,
    app.config.DB_HOST,
    app.config.DB_PORT,
    app.config.DB_NAME,
)
engine = create_engine(url)
DBSession = sessionmaker(bind=engine)

@app.route('/')
async def test(request):
    return json({
        'hello': 'world',
        'sqlalchemy.version': sqlalchemy.__version__
    })

@app.route('/testnewuser', methods=['POST'])
async def testnewuser(request):
    # 创建 session
    session = DBSession()
    # 新建 user
    user = User(tel='18668122344')
    # 添加到 session
    session.add(user)
    # 提交数据
    session.commit()
    # 关闭 session
    session.close()

    return json({
        'id': user.id,
        'tel': user.tel,
        'created_at': user.created_at
    })

@app.route('/testqueryuser', methods=['GET'])
async def testqueryuser(request):
    # 创建 session
    session = DBSession()
    # 查询数据
    user = session.query(User).filter(User.id == request.args['id'][0]).one()
    # 关闭 session
    session.close()

    return json({
        'id': user.id,
        'tel': user.tel,
        'created_at': user.created_at
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

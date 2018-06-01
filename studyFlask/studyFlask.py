from flask import Flask,render_template

app = Flask(__name__)     # 创建一个Flask对象，__name__传成其他字符串也行。


app.config['DEBUG'] = True  # 打开调试模式，以字典的方式配置
# app.debug = True  # 调试模式
# app.config.update({...})  #更新这个字典的方式

app.config.from_pyfile('settings.py')

# app.config.from_envvar('环境变量名')
# 如果环境变量名为py文件，会自动调用app.config.from_pyfile()

# app.config.from_json('json文件')            # json文件形式

# app.config.from_mapping({"DEBUG": True})    # 字典形式

# app.config.from_object('python类或者类的路径')
app.config.from_object('settings.TestConfig')

# 在settings.py中：

@app.route('/user/<int:uid>')
def hello_world(uid):
    print("UID:", uid)
    return 'Hello World!'

# app.add_url_rule("/", view_func=hello_world, endpoint="xxx", methods=['GET', 'POST'])
# endpoint 这里用来反向生成url，默认是函数名
# methods 指的是支持的请求方式

if __name__ == '__main__':
    app.run()

'''
def __init__(
        self,
        import_name,                        # 可以写任意字符串，一般写__name__，这样不会重名
        static_url_path=None,               # 静态文件前缀，如果该项配置成static_url_path='/yyy',访问静态文件的目录则为http://127.0.0.1:5000/sss/**.jpg
        static_folder='static',             # 静态文件路径，比如在项目目录下创建static目录，存放静态文件。访问通过http://127.0.0.1:5000/static/**.jpg
        static_host=None,
        host_matching=False,
        subdomain_matching=False,
        template_folder='templates',        # 模板文件夹，视图函数中需要引入from flask import render_template
        instance_path=None,                 # 当前路径/instance
        instance_relative_config=False,     # 如果该项为True,则会到 上面这个路径下去找配置文件
        root_path=None                      # 根目录
    ):
'''
# 路由管理
from flask import Flask, request, render_template, jsonify
from appservice import AppServer

appServer = AppServer.Instance()
app = appServer.GetFlask()

# 在第一次请求之前调用，可以在此方法内部做一些初始化操作
@app.before_first_request
def before_first_request():
    print("before_first_request")
    
# 在每一次请求之前调用，这时候已经有请求了，可能在这个方法里面做请求的校验
# 如果请求的校验不成功，可以直接在此方法中进行响应，直接return之后那么就不会执行视图函数
@app.before_request
def before_request():
    print("before_request")

# 在执行完视图函数之后会调用，并且会把视图函数所生成的响应传入,可以在此方法中对响应做最后一步统一的处理
@app.after_request
def after_request(response):
    print("after_request")
    return response

# 请每一次请求之后都会调用，会接受一个参数，参数是服务器出现的错误信息
@app.teardown_request
def teardown_request(e):
    print("teardown_request")


# 主页
@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("web_home.html")

# 登录
@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    if request.method == "GET":
        return render_template("web_login.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "admin" and password == "123456":
            return render_template("web_ok.html", username=username)
        return render_template("web_login.html", message="username or password error!", username=username)

@app.route("/test", methods=["POST"])
def submit_test():
    rdoTestValue = request.form.get("rdoTest")
    cbxTest = request.form.getlist("cbxTest")
    selTest = request.form.get("selTest")
    txtName = request.form.get("txtName")
    txtPassword = request.form.get("txtPassword")
    data = {
        "username": "admin",
        "rdoTestValue": rdoTestValue,
        "cbxTest": cbxTest,
        "selTest": selTest,
        "txtName": txtName,
        "txtPassword": txtPassword
    }
    return jsonify(data)

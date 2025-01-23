from flask import Flask, render_template

app = Flask(__name__)

# 首页路由


@app.route("/")
def home():
    return render_template("index.html")

# 关于我们页面


@app.route("/about")
def about():
    return render_template("about.html")

# 服务页面


@app.route("/services")
def services():
    return render_template("services.html")

# 联系页面


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)

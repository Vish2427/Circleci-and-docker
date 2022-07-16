from flask import Flask
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    return "This app is running and running"


if __name__ == "__main__":
    app.run(host="0.0.0.0" , port =5001)

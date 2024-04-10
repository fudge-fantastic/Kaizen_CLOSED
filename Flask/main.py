from flask import Flask

# Similar to FastAPI

app = Flask(__name__)

@app.route("/")
def fpage():
    return "This is the intial page, use: /welcome/demo or <username>"

@app.route("/welcome")
def intro():
    return "<h1> Hello there! Use '/demo' after the port number to proceed to next page </h1>"

@app.route("/welcome/demo")
def demo():
    return "<h2> This is a test page, you can head back or check out the test app user intro </h2>"

@app.route("/welcome/<user>")
def user(user):
    return f"<h3> Hi there {user}. This is a test page for the app, you can head back now </h3>"

# Use the command when not using __name__: flask --app main run
# Use this command when using __name__: python main.py
if __name__ == "__main__":
    app.run()
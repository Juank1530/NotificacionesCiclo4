from flask import Flask, request

#Here we create a flask object
app = Flask(__name__)

#Here we create our first web service
@app.route('/', methods=['GET'])
def test():
    return "Hello word"

#This is a web service with parameters 
@app.route('/greeting/<string:name>', methods=['GET'])
def greeting(name: str):
    return "Hello word " + name

#Here we execute the server on port 5000 to can use the webs service
if __name__ == '__main__':
    app.run()

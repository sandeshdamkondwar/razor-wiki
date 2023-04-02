from flask import Flask
from queryResolver import ask_ai

app = Flask(__name__)

@app.route('/health-check')
def checkHealth():
    return 'true'

@app.route('/query/<search_param>')
def getQuery(search_param):
    ask_ai(search_param)

if __name__ == '__main__':
    app.run()
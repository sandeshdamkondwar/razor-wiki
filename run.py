from flask import Flask,make_response,jsonify
from llama_index import GPTSimpleVectorIndex

index = GPTSimpleVectorIndex.load_from_disk('gptModel.json')

app = Flask(__name__)

@app.route('/health-check')
def checkHealth():
    return 'true'

@app.route('/query/<search_param>')
def getQuery(search_param):
    results = index.query(search_param, response_mode="compact")
    response = make_response(jsonify(results))
    return response

if __name__ == '__main__':
    app.run()
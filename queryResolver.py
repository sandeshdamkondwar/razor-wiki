
import shutil
from llama_index import GPTSimpleVectorIndex

def ask_ai(query):
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    while True: 
      response = index.query(query, response_mode="compact")
      return response
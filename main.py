# from msilib.schema import Directory
from distutils import filelist
import shutil
from llama_index import GPTSimpleVectorIndex
from langchain import OpenAI
import sys
import os, shutil
from gptModel  import *

absolute_path = os.path.dirname(__file__)

# os.environ["OPENAI_API_KEY"] = input("Paste your OpenAI key here and hit enter:")

def getRazorpayDoscAccountAndSettingPath():
    originPath =["/Users/shubham.k/Desktop/Razorpay2/docs/production/content/routes/payments/dashboard/account-settings"]
    return originPath

def saveRazorpayDoscFileInCurrentDirectory(razorpayDoscDirectorypath):
    new_directory_path = "docs/data"

    destinationDirectory = os.path.join(absolute_path, new_directory_path)

    filelist = []

    for path in razorpayDoscDirectorypath:
        for root, dirs, files in os.walk(path):
            for file in files:
                filelist.append(os.path.join(root,file))
    

    i = 0

    for trlFile in filelist:
        if trlFile.endswith(".md"):
            shutil.copy(trlFile, destinationDirectory)
            os.rename(destinationDirectory+'/index.md',destinationDirectory+'/'+str(i)+'index.md')
            i=i+1

    return destinationDirectory


razorpayDoscDirectorypath = getRazorpayDoscAccountAndSettingPath()

destinationDirectory = saveRazorpayDoscFileInCurrentDirectory(razorpayDoscDirectorypath)

gptAiModel = GPTModel(destinationDirectory)

# gptAiModel.construct_index()
    
index = GPTSimpleVectorIndex.load_from_disk('gptModel.json')
def ask_ai():
    while True: 
        query = input("What do you want to ask? ")
        response = index.query(query, response_mode="compact")
        print(response.response)

ask_ai()

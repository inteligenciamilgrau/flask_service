from flask import Flask, jsonify
from langchain_community.tools import DuckDuckGoSearchRun, DuckDuckGoSearchResults
import os

search_tool = DuckDuckGoSearchRun()

app = Flask(__name__)

@app.route('/')
def index():
    search = DuckDuckGoSearchResults()
    result = search.run("site:www.youtube.com agent swarm")

    return jsonify({"resultados": result})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))

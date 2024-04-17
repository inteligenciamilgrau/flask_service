from flask import Flask, jsonify
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
import os
#from dotenv import load_dotenv
#load_dotenv()

search_tool = DuckDuckGoSearchRun()

app = Flask(__name__)

agente1 = Agent(
            role="Seu papel é fazer buscas",
            backstory=f"""Você é um especialista em buscas na internet""",
            goal=f"""Escolha o melhor site da busca recebida""",
            tools=[search_tool],
            allow_delegation=False,
            verbose=True,
            llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7),
        )

tarefa = Task(
    description=
f"""
    Faça uma busca sobre novidades de inteligência artificial
    Escolha a melhor notícia entre as notícias recebidas
""",
    agent=agente1,
    expected_output="Link da melhor notícia. Responda em PT-BR"
)


@app.route('/')
def index():
    crew = Crew(
        agents=[agente1],
        tasks=[tarefa],
        verbose=True,
    )

    result = crew.kickoff()
    return jsonify({"bob": result})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))

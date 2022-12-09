# -*- coding: utf-8 -*-
"""chatbot_to_submit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XQugifvmdtaLgyTNvty-tVHw4suXlvlk
"""

pip install --upgrade openai

import os
import openai

openai.api_key = "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"

!pip install resume-parser

!pip install nltk

!pip install spacy==2.3.5

!pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.1/en_core_web_sm-2.3.1.tar.gz

!pip install pyresparser!

from google.colab import files
uploaded = files.upload()

from resume_parser import resumeparse

#replace with file path of resume
cleaned_resume = 0
data = resumeparse.read_file('/content/Elena Turing Resume.docx (1).pdf')
data

#run this cell to clean resume  
cleaned_resume = 1 
uni = data['university']
skills = data['skills']
degree = data['degree']
exp =  data['Companies worked at']

def behavorial_questions():
  intro = "Hi, I'm Bobby, the chatbox. I'll be your mock interviewer today for behavorial questions! How many questions do you have time to practice? (I recommend 3 for a quick demo): "
  num_questions = int(input(intro).strip())
  if cleaned_resume != 1: 
    print("I don't have your resume right now so I need you to answer some basic questions first")
    degree = input("What's your major? ").strip()
    exp = input("Where have you worked? ").strip()
    skills = input("What technical skills do you have? (Python, SQL, etc)").strip()
    uni = "UCSD"

  txt = f"The following is a conversation with an AI assistant. \
  The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you? \
  \nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: \
  I am a data science student looking for a internship. I went to school at {uni} and I have a degree in {degree}. I have worked at {exp} and my skills are {skills}. \
  Do a mock interview by asking me questions about my education and experiences. Wait until I answer a question before asking me another one\
  After I answer a question, you need to ask me another question. Do not answer any questions. \
  Do not ask similar questions. \
  Ask only 1 question at a time. \nAI:"

  txt2 = f"I am going to give you a question. Pretend you are a college student that studied at {uni}, \
  majored in {degree}, has experience working at {exp}, and has skills in {skills}. Answer this question like you are in a job interview: "

  for i in range(num_questions):
    input_prompts = txt
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt=input_prompts,
      temperature=0.9,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0.0,
      presence_penalty=0.6,
      stop=[" Human:", " AI:"]
    )

    ai_response = dict(response.get("choices")[0])["text"].strip()
    user_response = input(ai_response + ": ").strip()

    ideal_answer = openai.Completion.create(
      model="text-davinci-002",
      prompt=txt2+ai_response,
      temperature=0.9,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0.0,
      presence_penalty=0.6,
      stop=[" Human:", " AI:"]
    )
    auto_answer = dict(ideal_answer.get("choices")[0])["text"].strip()
    see_answer = int(input("Would you like to see a sample answer to the question you were just asked. Enter 1 if yes, 2 if no: ").strip())
    if see_answer==1:
      print(auto_answer)

  print(f"\n Well it was great learning more about you! Good luck on your behavorial interview :)")

behavorial_questions()
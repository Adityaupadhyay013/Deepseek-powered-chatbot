from work import api_key
import requests
import pyttsx3
import speech_recognition as sr
from File import Top_headlines
api_url = 'https://openrouter.ai/api/v1/chat/completions'
def chatbot_api(text):
  headers = {
    'Authorization':f'Bearer {api_key}',
    'Content-Type': 'application/json'
 }
  data = {
    "model": "deepseek/deepseek-chat:free",
    "messages": [{"role": "user", "content": text}]
 }
  response = requests.post(api_url , json = data  , headers = headers)
  answer = response.json()['choices'][0]['message']['content']
  Key_char = ["*" , "/" , '\'', "#"]
  for i in range(0 , len(Key_char)):
   answer = answer.replace(Key_char[i] , "")
  return answer
def Text_to_speech(answer):
    engine = pyttsx3.init()
    engine.say(answer)
    engine.runAndWait()
def starter():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("Speak...")
    audio_text = r.listen(source)
    print("Processing....")
  try:
    text = r.recognize_google(audio_text)
    return text
  except:
    return 0
def speech_to_text():
 r = sr.Recognizer()
 with sr.Microphone() as source:
    print("Speak...")
    audio_text = r.listen(source)
    print("Processing....")
 try:
    text = r.recognize_google(audio_text)
    return text
 except:
    Text_to_speech("Sorry but i did not get it...")
    return 0
Starters = ["Hello" , "Hi" , "hi" , "hello"]
L = ["top bullteins" , "Top headlines" , "news" , "top headlines"]
while True:
 Starter = starter()
 if Starter in Starters:
  Text_to_speech("Ask me what do you want to know: ")
  isflag = 0
  Text = speech_to_text()
  S = Text.split(" ")
  for items in S:
    if items in L:
      isflag = 1
  if(isflag == 1):
   Text_to_speech("Here are todays top Headlines")
   R = Top_headlines()
   Text_to_speech(R)
  if(isflag != 1):
   if(Text == 0):
    Text_to_speech("You should try again...")
   else:
     Response = chatbot_api(Text)
     Text_to_speech(Response)
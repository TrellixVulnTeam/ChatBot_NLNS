from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading


engine = pp.init()

voices = engine.getProperty('voices')
print(voices)

#engine.setProperty('voice', voices[0].id)


def speak(word):
    engine.say(word)
    engine.runAndWait()


# pyttsx3
bot = ChatBot("My Bot")

con = [
    'hii',
    'hi,how could i help you !',
    'hello',
    'hi,how could i help you !',
    'how are you ?',
    'I am doing great these days',
    'thank you',
    'In which city you live ?',
    'I am an Artificial Intelligence Bot',
    'In which language you talk?',
    ' I mostly talk in english'
    'can we go out for coffee ?',
    'sorry, i am an Artificial Intelligence',
    'who are you ?',
    'I am An EDITH',
    'Hey',
    'hi there , how could i help you?',
    'i am doing great!',
    'advice for covid',
    'stay home wear mask stay safe ',
    'who designed you?',
    'Akash And Shashwat designed Me',
    'what is DRS?',
    'DRS is DHONI REVIEW SYSTEM',
    'Tell me something about Amogh , who is Amogh?',
    'Amogh is the greatest personality of our class every one loves him especially Danny. Danny is a great admirer of amogh. Amogh is energetic person and always ready to do anything.',
    'Who is Piyush?',
    'Piyush is the most nonsense person of our class. He is so disgusting that he can even eat candies even after it fall on the ground.',
    'Who is Praveen?',
    'Praveen is the lover boy or I can say devdas of our class. He is always after different girls. He buys them oreo shake everyday but still no girl gives him importance. I feel very bad for him',
    'bye',
    'good bye',
    'What is AI',
    'Artificial intelligence (AI) is a wide-ranging branch of computer science ',
    'Thankyou for helping',
    'Anytime :-)'
]

trainer = ListTrainer(bot)

# now training the bot with the help of trainer

trainer.train(con)

# answer = bot.get_response("what is your name?")
# print(answer)

# print("Talk to bot ")
# while True:
#     query = input()
#     if query == 'exit':
#         break
#     answer = bot.get_response(query)
#     print("bot : ", answer)

main = Tk()

main.geometry("500x650")

main.title("My Chat bot")
img = PhotoImage(file="bot1.png")

photoL = Label(main, image=img)

photoL.pack(pady=5)


# takey query : it takes audio as input from user and convert it to string..

def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    print("your bot is listening try to speak")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("not recognized")

def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you : " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "bot : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)


frame = Frame(main)

sc = Scrollbar(frame)
msgs = Listbox(frame, width=200, height=20, yscrollcommand=sc.set)

sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()

# creating text field

textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)

btn = Button(main, text="Ask from Amogh", font=("Verdana", 20), command=ask_from_bot)
btn.pack()


# creating a function
def enter_function(event):
    btn.invoke()


# going to bind main window with enter key...

main.bind('<Return>', enter_function)


def repeatL():
    while True:
        takeQuery()


t = threading.Thread(target=repeatL)

t.start()

main.mainloop()

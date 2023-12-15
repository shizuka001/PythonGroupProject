import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os
import pyautogui
import weatherforecast
import requests
import numberfact
import sendEmail

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    print("The current time is ", Time)

def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)
    print("The current date is " + str(day) + "/" + str(month) + "/" + str(year))

def wishme():
    print("Welcome back!!")
    speak("Welcome back!!")
    hour = datetime.datetime.now().hour
    if hour >= 4 and hour < 12:
        speak("Good Morning!!")
        print("Good Morning!!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon!!")
        print("Good Afternoon!!")
    elif hour >= 16 and hour < 24:
        speak("Good Evening!!")
        print("Good Evening!!")
    else:
        speak("Good Night, See You Tommorrow")

    speak("please tell me how may I help you.")
    print("please tell me how may I help you.")

def screenshot():
    img = pyautogui.screenshot()
    import os

    # Specify the directory path you want to create (replace 'new_directory' with the desired name)
    directory_path = 'C:\\Users\\saksh\\Desktop\\Command Screenshots'
    # Create the directory
    if not(os.path.exists(directory_path)):
        os.mkdir(directory_path)
        speak('new directory command screenshots has been created on desktop')
        print('new directory command screenshots has been created on desktop')
    
    filePath = "C:\\Users\\saksh\\Desktop\\Command Screenshots\\screenshot 1.png"
    count = 1
    while True:
    # Code to be executed in the loop
        
        filePath = "C:\\Users\\saksh\\Desktop\\Command Screenshots\\screenshot "+str(count)+".png"
        if os.path.exists(filePath):
            count +=1
        else:
            break  # Exit the loop if the user enters "no"

    # Code after the loop
    img.save(filePath)
    speak('screenshot has been saved ad screenshot'+str(count)+'P N G please check it')
    print("screenshot has been saved as screenshot"+str(count)+".png")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)

    except Exception as e:
        print(e)
        speak("Please say that again")
        return "Try Again"

    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "who are you" in query:
            speak("I'm virtual assistant created by sakshi and team")
            print("I'm virtual assistant created by sakshi and team")

        elif "how are you" in query:
            speak("I'm fine, What about you?")
            print("I'm fine, What about you?")

        elif "fine" in query:
            speak("Glad to hear that!!")
            print("Glad to hear that!!")

        elif "good" in query:
            speak("Glad to hear that!!")
            print("Glad to hear that!!")
        
        elif "open youtube" in query:
            wb.open("youtube.com") 

        elif "open google" in query:
            wb.open("google.com") 
   
        elif "open stack overflow" in query:
            wb.open("stackoverflow.com")

        elif "open chrome" in query:
            chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(chromePath)
        
        elif "remember that" in query:
            speak("What should I remember")
            data = takecommand()
            speak("You said me to remember that" + data)
            print("You said me to remember that " + str(data))
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you remember anything" in query:
            remember = open("data.txt", "r")
            speak("You told me to remember that" + remember.read())
            print("You told me to remember that " + str(remember))

        elif "screenshot" in query:
            screenshot()
            # speak("I've taken screenshot, please check it")
        
        elif "what is the current temperature" in query:
            forecastValues = weatherforecast.forecast()
            speak("Currently the temperature is" + str(int(forecastValues))+" farenheit")

        elif "tell me a joke" in query:
            url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"

            headers = {
                "accept": "application/json",
                "X-RapidAPI-Key": "85002f489dmshace7493952edcd4p17598ajsn90c8e819583e",
                "X-RapidAPI-Host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
            }

            response = requests.get(url, headers=headers)
            print(response.json()['value'])
            speak(response.json()['value'])
        
        elif "number facts" in query:
            speak("tell me the number you want to hear the facts about")
            value = takecommand()
            try:
                value.replace(",", "")
                int_value = int(value)
                speak(numberfact.numfacts(str(int_value)))
                print(numberfact.numfacts(str(int_value)))
            except ValueError:
                speak('The given number is not an integer, Please try again')

        elif "write email" in query:
            speak("tell me subject of email")
            print("tell me subject of email")
            subject = takecommand()
            speak("tell me content of the email")
            print("tell me content of the email")
            content = takecommand()
            speak("are you sure you want to send this email")
            isConfirm = takecommand()
            if isConfirm == 'yes':
                emailoffset = sendEmail.send_email(subject, content)
                if(emailoffset):
                    speak('email sent successfully')
                    print('email sent successfully')
                else:
                    speak('error encountered while sending email')
                    print('error encountered while sending email')

        elif "offline" or "bye" or "shut up" in query:
            quit()



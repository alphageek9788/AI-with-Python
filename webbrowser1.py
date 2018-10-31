import speech_recognition as sr
import webbrowser
recording = sr.Recognizer()


with sr.Microphone() as source:
    recording.adjust_for_ambient_noise(source)
    print("Say something!")
    audio = recording.listen(source)
    rec = recording.recognize_google(audio)

if rec == "open browser":
    url = 'http://www.python.org/'

    webbrowser.open(url)

    # # Open URL in a new tab, if a browser window is already open.
    # webbrowser.open_new_tab(url + 'doc/')
    #
    # # Open URL in new window, raising the window if possible.
    # webbrowser.open_new(url)
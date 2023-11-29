import openai
import pyttsx3
import speech_recognition as sr 
import webbrowser
import time

openai.api_key="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"

#initial the text-to-speech engine
engine = pyttsx3.init()

def transcribe_audio_to_text(filename):
    recognizer=sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
        try:
            return recognizer.recognize_google(audio)
        except:
            print('skipping unknown error')

def generate_respond(prompt):
    response=openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_token=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response["choice"][0]["text"]

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
    #Waiting for user to say "genuis"
     print("say 'Genius' to start recording question....")
     with sr.Microphone() as source:
         recognizer =sr.Recognizer()
         audio = recognizer.listen(source)
         try:
            transcription = recognizer.recognize_google(audio)
            if transcription.lower == 'genius':
                #Record audio
                filename = "input.wav"
                print("What are you curious about......?")
                with sr.Recognizer() as source:
                    source.pause_threshold=1
                    audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                    with open(filename, "wb") as f:
                        f.write(audio.get_wav_data())
                #Transcribe text to audio
                text = transcribe_audio_to_text(filename)
                if next:
                    print(f"Your said: {text}")
                
                    #Generate respnds using GPT_3
                    response = generate_respond(text)
                    print=(f"GPT-3 Sa: {response}" )

                    #Read response using text-to-speech
                    speak_text(response)
         except Exception as e:
            print("an error occurred: {}".format(e))


if __name__=="_main_":
    main()
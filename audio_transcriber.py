'''
pip install SpeechRecognition
pin install python-docx
'''
import docx
import SpeechRecognition

print("Please make sure you have done a installed all of the dependencies")
print("Please make sure you are in the correct directory")
print("Finally, please make sure that you have the files saved in the same directory you are in.")

r = speech_recognition.Recognizer()

message_file = str(input("please input audio filename here (just file name)"))

doc_file = str(input('please input doc file PATH to transcribe to here'))

doc = docx.Document()

phone_call = speech_recognition.AudioFile(message_file)

with message_file as source:
	audio = r.record(source)

print(r.recognize_google(audio))

doc.add_paragraph(str(r.recognize_google(audio)))
doc.save(doc_file)
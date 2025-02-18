import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Paths to the uploaded files
file_paths = [
    ''
]

# Function to transcribe audio from file
def transcribe_audio(file_path):
    try:
        with sr.AudioFile(file_path) as source:
            audio = recognizer.record(source)
            # Perform the transcription
            return recognizer.recognize_google(audio)
    except Exception as e:
        return f"Transcription error: {e}"

# Transcribe each file
transcriptions = [transcribe_audio(path) for path in file_paths]
transcriptions

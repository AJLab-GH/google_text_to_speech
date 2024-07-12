from google.cloud import texttospeech
from pathlib import Path

# Paths
base_folder_path = Path(__file__).parent
audio_folder_path = base_folder_path / "audio"
text_folder_path = base_folder_path / "text"

# Create folders if they don't exist
audio_folder_path.mkdir(parents=True, exist_ok=True)
text_folder_path.mkdir(parents=True, exist_ok=True)

# File paths
filename = "002"
speech_file_path = audio_folder_path / f"{filename}.mp3"
text_file_path = text_folder_path / f"{filename}.txt"

# Text input
text_input = '''and that's why you don't mess with the three billy goats gruff!'''

# Write text to file
with open(text_file_path, 'w') as text_file:
    text_file.write(text_input)

# Initialize Google Cloud Text-to-Speech client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text=text_input)

# Build the voice request, select the language code and ssml voice gender
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",
    ssml_gender=texttospeech.SsmlVoiceGender.MALE,
    name="en-US-Wavenet-D"  # Specify a specific voice name if desired
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with the selected voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
with open(speech_file_path, "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print(f'Audio content written to file "{speech_file_path}"')

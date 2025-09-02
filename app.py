import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

transcribed = openai.Audio.transcribe("whisper-1", audio_file)


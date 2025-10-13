from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
import os

load_dotenv()

elevenlabs = ElevenLabs(
  api_key=os.getenv("JUSTLEARNINGKEY"),
)

def pronounce_word(word):
    if word.isalpha():
        audio = elevenlabs.text_to_speech.convert(
            text=word,
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        return audio
    return None



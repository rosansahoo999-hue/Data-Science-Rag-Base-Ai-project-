import whisper
import json

model = whisper.load_model("base")

result = model.transcribe(audio = 'audio/12_Exercise 1 - Pure HTML Media Player.mp3', language='hi', task='translate', word_timestamps=False)

# with open("output.json", "w") as f:
#     json.dump(f, result)

chunks = []
for segments in result["segments"]:
    chunks.append({"start": segments["start"], "end": segments["end"], "text": segments["text"]})

print(chunks)

with open("output.json", "w") as f:
    json.dump(chunks, f)
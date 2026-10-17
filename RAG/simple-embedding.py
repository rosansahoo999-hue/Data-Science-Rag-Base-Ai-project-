import requests

r = requests.post("http://localhost:11434/api/embeddings", json={
    "model": "bge-m3",
    "prompt": "Rosan is a good boy",
})

embedding = r.json()['embedding']
print(embedding[0:5])
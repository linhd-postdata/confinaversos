with open("corpus.txt", "r") as f:
    txt = f.read()

for chunk in txt.split("---"):
    poem = chunk.strip().split("\n")
    author = poem[0].split("autor:")[1].strip()
    title = poem[1].split("título:")[1].strip()
    text = "\n".join(poem[2:]).strip()
    with open(f"corpus/{author}_{title.replace('/', '-')}.txt".lower(), "w") as f:
        f.write(text)


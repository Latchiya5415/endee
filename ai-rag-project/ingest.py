import sys
import os
sys.path.append(os.path.abspath("../src"))

import endee
from rag import embed

db = endee.Client()

docs = []

with open("data/knowledge.txt") as f:
    for line in f:
        line = line.strip()
        if line:
            docs.append(line)

vectors = []

for d in docs:
    vectors.append({
        "text": d,
        "vector": embed(d)
    })

db.insert(vectors)

print("Documents stored in Endee database")
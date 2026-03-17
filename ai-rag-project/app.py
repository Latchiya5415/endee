import endee
from rag import embed

db = endee.Client()

query = input("Ask something: ")

query_vector = embed(query)

results = db.search(query_vector)

print("Answer:", results)
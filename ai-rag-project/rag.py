with open("data/knowledge.txt", "r") as f:
    docs = f.readlines()

query = input("Ask a question: ").lower()
query_words = query.split()

results = []

for doc in docs:
    doc_lower = doc.lower()
    
    # count matching words
    score = sum(1 for word in query_words if word in doc_lower)
    
    if score > 0:
        results.append((score, doc.strip()))

# sort by best match
results.sort(reverse=True)

print("\n🔍 Results:")
for score, r in results:
    print("-", r)
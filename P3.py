sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
max_words = 0
for sentence in sentences:
    words = sentence.split()
    max_words = max(max_words, len(words))
print("Output: ",max_words)

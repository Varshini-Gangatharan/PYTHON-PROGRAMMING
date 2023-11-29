def rem(s1, s2):
    words_s1 = set(s1.split())
    words_s2 = set(s2.split())
    common_words = words_s1.intersection(words_s2)
    result_s1 = ' '.join(word for word in s1.split() if word not in common_words)
    result_s2 = ' '.join(word for word in s2.split() if word not in common_words)
    return result_s1, result_s2
S1 = "sky is blue in color"
S2 = "Raj likes sky blue color"
output_s1, output_s2 = rem(S1, S2)
print("Output:", output_s1)
print(output_s2)

text = "machine learning is great machine learning is fun machine learning is powerful"

words = text.split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1    
    else:
        word_count[word] = 1

print("\n 출력 기댓값 그대로")
print(word_count)


print("\n보기 편한 단어 빈도수:")
for word, count in word_count.items():
    print(f"{word}: {count}번") 
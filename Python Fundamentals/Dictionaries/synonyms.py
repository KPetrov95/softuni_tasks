count = int(input())
synonyms = {}

for i in range(count):
    word = input()
    synonym = input()

    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)

for word in synonyms.keys():
    print(f'{word} - {", ".join(synonyms[word])}')

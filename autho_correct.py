import nltk


def read_file(path):
    with open(path, 'r', encoding="utf-8") as f:
        words = f.read().split()

    return words


words=read_file('big.txt')


text = input("Paste your text: ")
new_text = ""

for sntnce in text.rsplitlines():
    sntnce_splited = sntnce.rsplit()
    for x in sntnce_splited:
        if x not in words:
            for word in words:
                corrected_word = nltk.edit_distance(x,word)
            sntnce_splited[sntnce_splited.index(x)] = corrected_word
    new_text += sntnce_splited.join(" ") + "\n"


print(new_text)



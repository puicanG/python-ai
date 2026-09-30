
def search_word(lookup_word):
    with open("paragraphs.txt","r") as file:
        content = file.read()

    words = content.split()

    total_words = len(words)
    words_found = 0

    for word in words:
        clean_word = word.lower()
        if lookup_word.lower() in clean_word:
            words_found = words_found + 1

    report = f"Word Search Report: \n Word Lookup: {lookup_word.lower()} \n Words Found: {words_found} times \n File total word count: {total_words} words"
    return report

result = search_word("marcus")
print(result)
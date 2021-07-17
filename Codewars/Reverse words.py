def reverse_words(text):
    return ' '.join([i[::-1] for i in text.split()])
    # FIXME double spaces strings


print(reverse_words('The quick brown fox jumps over the lazy dog.'))

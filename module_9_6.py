def all_variants(text):
    len_ = len(text)
    for b in range(1, len_ + 1):
        for c in range(len_ - b + 1):
            yield text[c:c + b]


a = all_variants("abc")
for i in a:
    print(i)

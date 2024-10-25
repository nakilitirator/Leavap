def all_variants(text):
    x = 0
    y = 0
    for x in range(len(text)):
        for y in range(x + 1, len(text) + 1):
            yield text[x:y]


if __name__ == "__main__":
    a = all_variants("abcd")
    for i in a:
        print(i)



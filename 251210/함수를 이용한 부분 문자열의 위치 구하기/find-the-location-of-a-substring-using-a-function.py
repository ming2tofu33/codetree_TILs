text = input()
pattern = input()

# Please write your code here.

def patter_in_text(text, pattern):
    idx = -1
    if pattern in text:
        idx = text.index(pattern)

    return idx

print(patter_in_text(text, pattern))
def generate_document(chars, doc):
    kv = {}

    for ch in chars:
        if ch not in kv:
            kv[ch] = 0

        kv[ch] += 1

    for ch in doc:
        if ch not in kv or kv[ch] == 0:
            return False

        kv[ch] -= 1

    return True


def main():
    print(generate_document("mI locksher", "Im sherlock"))

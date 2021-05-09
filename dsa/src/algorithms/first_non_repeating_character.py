def first_non_repeating_character(string):
    kv = {}

    for ch in string:
        if ch not in kv:
            kv[ch] = 0

        kv[ch] += 1

    for idx, ch in enumerate(string):
        if kv[ch] == 1:
            return idx

    return -1


def main():
    print(first_non_repeating_character("abcdcaf"))

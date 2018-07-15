import random
import string


def active_keys_generate():
    alphabet_list = []
    active_keys = []
    for chars in string.ascii_lowercase:
        alphabet_list.append(chars)
    while len(active_keys) < 200:
        key = ''.join(random.sample(alphabet_list, 5))
        if key in active_keys:
            continue
        else:
            active_keys.append(key)
    print(active_keys)


if __name__ == "__main__":
    active_keys_generate()

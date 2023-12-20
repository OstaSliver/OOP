def char_count(str):
    return {i: str.count(i) for i in str}

print(char_count("language"))
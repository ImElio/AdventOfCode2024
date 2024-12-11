def run_length_encode(input_string):
    if not input_string:
        return ""

    encoded = []
    count = 1

    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            encoded.append(f"{input_string[i - 1]}{count}")
            count = 1

    encoded.append(f"{input_string[-1]}{count}")
    return "".join(encoded)

def run_length_decode(encoded_string):
    decoded = []
    i = 0

    while i < len(encoded_string):
        char = encoded_string[i]
        j = i + 1
        while j < len(encoded_string) and encoded_string[j].isdigit():
            j += 1
        count = int(encoded_string[i + 1:j])
        decoded.append(char * count)
        i = j

    return "".join(decoded)

if __name__ == "__main__":
    test_string = "AAABBBCCDAA"
    encoded = run_length_encode(test_string)
    print("Stringa originale:", test_string)
    print("Stringa compressa:", encoded)
    print("Stringa decompressa:", run_length_decode(encoded))

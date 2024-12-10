def text_to_ascii_art(input_file, output_file):
    ascii_art = {
        "A": "  A  \n A A \nAAAAA\nA   A\nA   A\n",
        "B": "BBBB \nB   B\nBBBB \nB   B\nBBBB \n",
        "C": " CCC \nC   C\nC    \nC   C\n CCC \n"
    }

    with open(input_file, "r") as f:
        text = f.read().upper()

    with open(output_file, "w") as f:
        for char in text:
            if char in ascii_art:
                f.write(ascii_art[char] + "\n")
            else:
                f.write(char + "\n")

if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "ascii_art.txt"
    with open(input_file, "w") as f:
        f.write("ABC")
    text_to_ascii_art(input_file, output_file)
    print(f"ASCII art generata in: {output_file}")

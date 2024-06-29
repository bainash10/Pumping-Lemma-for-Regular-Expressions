import re

def check_regular(expression, pumping_length):
    # Generate strings from the regular expression up to 2*pumping_length in length
    for length in range(pumping_length, 2 * pumping_length + 1):
        strings = generate_strings(expression, length)
        if strings:
            for s in strings:
                # Check if s satisfies the pumping lemma
                if satisfies_pumping_lemma(s, pumping_length):
                    print(f"The string '{s}' satisfies the pumping lemma for regular languages with expression '{expression}'.")
                    return True
    print(f"No string found that satisfies the pumping lemma for regular languages with expression '{expression}'.")
    return False

def generate_strings(expression, length):
    # Generate all strings matching the regular expression up to given length
    return [s for s in generate_all_strings_up_to_length(expression, length) if re.fullmatch(expression, s)]

def generate_all_strings_up_to_length(expression, max_length):
    # Generate all strings of length up to max_length based on the given regular expression
    results = []
    alphabet = extract_alphabet(expression)

    def generate(current_string):
        if len(current_string) <= max_length:
            results.append(current_string)
        else:
            return
        for letter in alphabet:
            new_string = current_string + letter
            generate(new_string)

    generate('')
    return results

def extract_alphabet(expression):
    # Extract the alphabet used in the regular expression
    return list(set(re.findall(r'[a-zA-Z0-9]', expression)))

def satisfies_pumping_lemma(s, pumping_length):
    # Check if the string s satisfies the pumping lemma conditions
    length = len(s)
    for i in range(1, pumping_length + 1):
        if length > pumping_length and length - i > pumping_length:
            # Split s into x, y, z where |xy| <= pumping_length and |y| > 0
            x = s[:i]
            y = s[i:length-i]
            z = s[length-i:]
            if len(y) > 0:
                # Check if xy^i z still belongs to the language defined by the regular expression
                if re.fullmatch(f"{x}(?:{y}){{{i}}}{z}", s):
                    return True
    return False

# Example usage:
def main():
    regular_expression = input("Enter a regular expression (e.g., '(a|b)*a'): ").strip()
    pumping_length = int(input("Enter the pumping length (e.g., 2): ").strip())

    check_regular(regular_expression, pumping_length)

if __name__ == "__main__":
    main()

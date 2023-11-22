def convert_to_hindi(text):
    # Define a dictionary mapping English to Hindi alphabets with matras
    english_to_hindi = {
        'a': 'अ', 'aa': 'आ', 'i': 'इ', 'ii': 'ई', 'u': 'उ', 'uu': 'ऊ',
        'e': 'ए', 'ai': 'ऐ', 'o': 'ओ', 'au': 'औ',
        'k': 'क', 'kh': 'ख', 'g': 'ग', 'gh': 'घ', 'ng': 'ङ',
        'ch': 'च', 'chh': 'छ', 'j': 'ज', 'jh': 'झ', 'ny': 'ञ',
        't': 'त', 'th': 'थ', 'd': 'द', 'dh': 'ध', 'n': 'न',
        't': 'त', 'th': 'थ', 'd': 'द', 'dh': 'ध', 'n': 'न',
        'p': 'प', 'ph': 'फ', 'b': 'ब', 'bh': 'भ', 'm': 'म',
        'y': 'य', 'r': 'र', 'l': 'ल', 'v': 'व',
        'sh': 'श', 'shh': 'ष', 's': 'स', 'h': 'ह',
        'aa': 'ा', 'i': 'ि', 'ii': 'ी', 'u': 'ु', 'uu': 'ू',
        'e': 'े', 'ai': 'ै', 'o': 'ो', 'au': 'ौ',
    }

    # Convert each character in the input text
    hindi_text = ''
    i = 0
    while i < len(text):
        char = text[i]
        # Check for two-character combinations
        if i + 1 < len(text):
            two_chars = char + text[i + 1]
            if two_chars in english_to_hindi:
                hindi_text += english_to_hindi[two_chars]
                i += 2
                continue

        # Check for one-character combinations
        hindi_text += english_to_hindi.get(char, char)
        i += 1

    return hindi_text

if __name__ == "__main__":
    # Example usage
    english_text = "ag "
    hindi_text = convert_to_hindi(english_text)
    print(f"English Text: {english_text}")
    print(f"Hindi Text: {hindi_text}")

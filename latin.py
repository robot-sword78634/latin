def to_pig_latin(word):
    vowels = "aeiouAEIOU"
    if word[0] in vowels:
        return word + "way"
    else:
        for i, letter in enumerate(word):
            if letter in vowels:
                return word[i:] + word[:i] + "ay"
        return word + "ay"  # fallback if no vowels found

def translate_sentence(sentence):
    words = sentence.split()
    translated = []

    for word in words:
        # Preserve punctuation
        prefix = ""
        suffix = ""
        core_word = word

        # Strip punctuation from the beginning
        while core_word and not core_word[0].isalnum():
            prefix += core_word[0]
            core_word = core_word[1:]

        # Strip punctuation from the end
        while core_word and not core_word[-1].isalnum():
            suffix = core_word[-1] + suffix
            core_word = core_word[:-1]

        if core_word:
            # Preserve capitalization
            is_capitalized = core_word[0].isupper()
            pig_word = to_pig_latin(core_word.lower())
            if is_capitalized:
                pig_word = pig_word.capitalize()
            translated.append(prefix + pig_word + suffix)
        else:
            translated.append(word)

    return ' '.join(translated)

# Get input from the user
user_input = input("Enter a sentence to translate into Pig Latin:\n> ")
translated = translate_sentence(user_input)
print("\nPig Latin translation:")
print(translated)



def clean_text(text: str) -> str:
    return ' '.join(text.split())

def contains_word(text: str, word: str) -> bool:
    text = text.split()
    for w in text:
        if w == word:
            return True
    return False

def replace_word(text: str, old_word: str, new_word: str) -> str:
    return text.replace(old_word,new_word)

def get_first_10_chars(text: str) -> str:
    return text[:10]

def mask_email(email: str) -> str:
    email = email.split('@')
    return email[0][0] + '*'*(len(email[0])-2) +email[0][-1] + '@' + email[1]

print(clean_text("  hello   world  ",))
print(contains_word("badword should be hidden", 'hidden'))
print(replace_word("badword should be hidden", 'hidden','horn'))
print(get_first_10_chars("badword should be hidden"))
print(mask_email('bulat@example.com'))





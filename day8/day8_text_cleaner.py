def clean_text(text: list[str]) -> list[str]:
    msg_clear = []
    for part in text:
        msg_clear.append(' '.join(part.split()))
    return msg_clear

def replace_word(text: list[str]) -> list[str]:
    new_messages = []
    for part in text:
        if 'badword' in part:
           new_messages.append(part.replace('badword','***'))
        else:
            new_messages.append(part)
    return new_messages

def mask_email(email: str) -> str:
    email = email.split('@')
    return email[0][0] + '*'*(len(email[0])-2) +email[0][-1] + '@' + email[1]

def mask_email_in_messages(messages: list[str]) -> list[str]:
    result = []
    for message in messages:
        new_message = []
        for word in message.split():
            if '@' in word:
                new_message.append(mask_email(word))
            else:
                new_message.append(word)
        result.append(' '.join(new_message))
    return result

def rebuild_text(text: list[str]) -> str:
    return mask_email_in_messages(replace_word(clean_text(text)))


messages = [
    "  hello   world  ",
    "python is cool",
    "contact me at bulat@example.com",
    "badword should be hidden",
]

print(rebuild_text(messages))

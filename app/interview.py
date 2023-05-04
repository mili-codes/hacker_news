chat = " we are having a discussion"

# ew era gnivah

rev_chat = temp = ''
for c in chat:
    if c !=" ":
        temp += c
    else:
        rev_chat += temp[::-1] + c
        temp = ''
rev_chat += temp[::-1]

print(rev_chat)
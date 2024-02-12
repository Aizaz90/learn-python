message=input(">")
word=message.split(' ')
emojis = {

#PRess control cmd and space on mac
":)": "😀",
":(":"😎"

}
output=""
for i in word:
    output+=emojis.get(i,i)+" "

print(output)
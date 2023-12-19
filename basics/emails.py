with open('message.txt', 'r') as message:
    with open('names.txt', 'r') as names:

        body = message.read()
        for name in names:
            email = 'Hello ' + name + '\n' + body
        
            with open(name.strip()+'.txt', 'w') as uniqueEmail:
                uniqueEmail.write(email)

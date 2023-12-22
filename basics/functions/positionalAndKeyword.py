def greet(name, msg = 'How are you?'):
    print('Hi', name, ',', msg)

# two keywords
greet(name = 'David', msg = 'How you doing?')

# Two unordered keywords
greet(msg = 'What can I do for you?', name = 'David')

# One positional value and one keyword
greet('David', msg = 'How is it going?')

# Two positional values
greet('David', 'Good to see you again')

# One positional value and a defualt parameter
greet('David')
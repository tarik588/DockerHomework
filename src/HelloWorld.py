def hello(name):
    print("Welcome to python! What's your name?")
    input(name)
    if(name.length<2):
        print("I asked for your name not your first initial! Give me a real name please.")
    else:
        print("Hey there "+ name+ "You're welcome to code as much as you want!")

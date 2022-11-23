def messenger(msg):
    print(msg)


messenger('hello first')

first = messenger

second = first

second('hello second')

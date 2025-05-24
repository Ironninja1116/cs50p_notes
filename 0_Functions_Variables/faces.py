# Problem set 0, Problem 3

def convert(message):
    return message.replace(":)","🙂",-1).replace(":(","🙁",-1)

def main():
    textInput = input("Please type anything: ")
    print(convert(textInput))

main()


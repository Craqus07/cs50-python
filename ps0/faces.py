def main():
    text = input("Input emojicons to emojify! :")
    print(convert(text))

def convert(text):
    emoji = text.replace(":)","🙂",-1).replace(":(","🙁",-1)
    return emoji

main()
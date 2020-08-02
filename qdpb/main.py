from . import client


def get_token():
    try:
        with open("token.txt") as file:
            return file.read()
    except FileNotFoundError:
        print("FileNotFoundError: Store your bot's access token in token.txt")
        quit()


client = client.QDPBClient()
client.run(get_token())

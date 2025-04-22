import json
import random
import os


def load_storage():
    filePath = 'urls.json'
    if not os.path.isfile(filePath):
        with open(filePath, "w") as f:
            json.dump({}, f)

    return filePath


def save_storage(data: str):
    storage = load_storage()
    with open(storage, "w+") as f:
        data_to_save = {f"{data}":'http://127.0.0.1:8080'}
        json.dump(data_to_save, f, indent=4)


def generate_short_url(length=6):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(random.choices(letters,k=length))
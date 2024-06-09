import os

import cowsay


def lambda_handler(event, context):
    print(f"event ==> ${event}")
    cowsay.cow(os.environ["TO_SAY"])

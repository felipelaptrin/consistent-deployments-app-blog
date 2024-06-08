import os

import cowsay


def lambda_handler(event, context):
    cowsay.cow(os.environ["TO_SAY"])

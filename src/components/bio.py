import textwrap

import constants


def create() -> None:
    with open(constants.BIO_WRAPPED_MD, "w", encoding="utf-8") as file:
        with open(constants.BIO_MD, encoding="utf-8") as bio_file:
            file.write(textwrap.fill(bio_file.read(), width=constants.BIO_WIDTH) + "\n")

import constants
import textwrap

def create(): 
    with open(constants.BIO_WRAPPED_MD, 'w') as file:
        file.write(textwrap.fill(open(constants.BIO_MD).read(), width=constants.BIO_WIDTH) + "\n")

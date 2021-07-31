"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    # Main entry point of the app
    print("what's popping? i am a fun converter. I convert things to FooBarQix")

def fooBarQix(input):
    result = ""
    if input != 0:
        if input%3 == 0:
            result += "Foo"

            return result

    return 0


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()

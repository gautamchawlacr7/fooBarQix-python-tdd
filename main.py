"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    # Main entry point of the app
    print("what's popping? i am a fun converter. I convert things to FooBarQix")

def divisibilityResult(input):
    result = ""
    if input%3 == 0:
        result += "Foo"

    if input%5 == 0:
        result += "Bar"

    if input%7 == 0:
        result += "Qix"
        
    return result

def fooBarQix(input):
    result = ""
    if input == 0:
        return "0"
    
    result += divisibilityResult(input)

    for element in str(input):
        if int(element) == 3:
            result += "Foo"
        if int(element) == 5:
            result += "Bar"
        if int(element) == 7:
            result += "Qix"

    return result


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()

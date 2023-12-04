#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return sentence[0] is None

    return len(sentence), sentence[0]

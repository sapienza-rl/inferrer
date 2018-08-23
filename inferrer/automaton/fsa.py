import abc
from typing import Set


class FSA(abc.ABC):
    """
    Represents a finite state acceptor that
    accepts or rejects strings of the given
    alphabet.

    The two known implementations of this
    abstract class is dfa.py and nfa.py.
    """
    def __init__(self, alphabet: Set[str]):
        if '' in alphabet:
            raise ValueError('The empty string is not allowed in the alphabet!')
        self.__alphabet = alphabet

    @property
    def alphabet(self):
        return self.__alphabet
#!/usr/bin/python3
"""Module defines a locked class."""
class LockedClass:
    """
    Stops instantiating new LockedClass attributes
    except attributes called 'first_name'.
    """
    __slots__ = ["first_name"]

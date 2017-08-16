# -*- coding: utf-8 -*-

""" General utilities. """

__all__ = ["validate_channel", "validate_city"]


def _validate_shorthand(entry, options):
    r"""
    Validate the input entry from a list of options.

    :param entry:
        A string.

    :param options:
        A list of acceptable string entries.
    """

    entry = entry.strip().lower()

    for option in options:
        if option.lower().strip().startswith(entry):
            # TODO deal with ambiguity
            return option

    raise ValueError("unsupported option: {} (available: {})".format(
        entry, ", ".join(options)))


def validate_channel(channel):
    r"""
    Validate the input for property channel.

    :param channel:
        The property channel. Supported channels include: all, commercial, and
        residential.
    """
    return _validate_shorthand(channel, ("all", "commercial", "residential"))


def validate_city(city):
    r"""
    Validate the input for an Australian city.

    :param city:
        An Australian city. Supported cities include: Adelaide, Brisbane,
        Canberra, Melbourne, and Sydney.
    """
    return _validate_shorthand(city, 
        ("Adelaide", "Brisbane", "Canberra", "Melbourne", "Sydney"))
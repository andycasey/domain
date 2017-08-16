# -*- coding: utf-8 -*-

""" General utilities. """

__all__ = ["validate_channel", "validate_city"]

def validate_channel(channel):
    r"""
    Validate the input for property channel.

    :param channel:
        The property channel. Supported channels include: all, commercial, and
        residential.
    """

    channel = channel.strip().lower()
    supported_channels = ("all", "commercial", "residential")
    for supported_channel in supported_channels:
        if supported_channel.startswith(channel):
            return supported_channel

    raise ValueError("unsupported channel: {} (supported: {})".format(
        channel, ", ".join(supported_channels)))


def validate_city(city):
    r"""
    Validate the input for an Australian city.

    :param city:
        An Australian city. Supported cities include: Adelaide, Brisbane,
        Canberra, Melbourne, and Sydney.
    """

    city = city.strip().title()
    supported_cities = \
        ("Adelaide", "Brisbane", "Canberra", "Melbourne", "Sydney")

    for supported_city in supported_cities:
        if supported_city.startswith(city):
            return supported_city

    raise ValueError("unsupported city: {} (supported cities are: {})".format(
            city, ", ".join(supported_cities)))
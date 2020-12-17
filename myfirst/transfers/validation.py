from datetime import datetime, time, date
from rest_framework import serializers


def isValidNumber(your_element):
    if your_element <= 0:
        raise serializers.ValidationError(
            'Incorrect data. Number must be > 0.')
    return your_element


def isValidName(your_element):
    if not set(your_element).isdisjoint(set("1234567890`,./;[]!@#$%^&*()_+|}{:>?<")):
        raise ValueError(
            'Incorrect data. It must be a correct name, not the '+your_element)
    return your_element


def isValidDate(your_element):
    your_element = your_element.split('-')
    year = int(your_element[0])
    month = int(your_element[1])
    day = int(your_element[2])
    try:
        your_element = date(year, month, day)
    except ValueError:
        raise ValueError('Incorrect data. It must be year-month-day.')
    checker = datetime.now()
    if your_element.year > checker.year:
        raise ValueError('Incorrect data. Year can`t be grater than present.')
    elif your_element.year == checker.year:
        if your_element.month > checker.month:
            raise ValueError(
                'Incorrect data. Month can`t be grater than present.')
        elif your_element.month == checker.month:
            if your_element.day > checker.day:
                raise ValueError(
                    'Incorrect data. Day can`t be grater than present.')
    return str(your_element)


def isValidTime(your_element):
    try:
        your_element = your_element.split(':')
        hour = int(your_element[0])
        minute = int(your_element[1])
        your_element = time(hour, minute)
        your_element = your_element.strftime('%H:%M')
    except:
        raise ValueError('Incorrect data. It must be HH:MM.')
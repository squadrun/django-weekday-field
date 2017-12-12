# django-weekday-field

This is a clone of a project by Matthew Schinckel: [https://bitbucket.org/schinckel/django-weekday-field](https://bitbucket.org/schinckel/django-weekday-field)

This version is simply V1.1.0 refactored to be compatible with Django 2.0 and as such has been 'upissued' to V2.0.

## Original README

A field that encapsulates the handling of selection of 0 or more weekday choices.

Uses Django's CommaSeparatedIntegerField internally.

Usage:

```python
from django.db import models

import weekday_field

class MyModel(models.Model):
    weekdays = weekday_field.fields.WeekdayField()
```

There is also a BitwiseWeekdayFormField, contributed by Andrew Gall <housepage@gmail.com>, which stores the data in a single integer.

Thanks to NaderM <https://bitbucket.org/NaderM>, 1.1.0 includes python3 support, and extensive testing.
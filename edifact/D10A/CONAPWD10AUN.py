#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD10AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'RFF', MIN: 1, MAX: 9},
    {ID: 'DTM', MIN: 1, MAX: 9},
    {ID: 'NAD', MIN: 1, MAX: 3, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 2, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 3},
        ]},
    ]},
    {ID: 'LOC', MIN: 1, MAX: 99},
    {ID: 'FTX', MIN: 1, MAX: 99},
    {ID: 'DOC', MIN: 0, MAX: 9},
    {ID: 'CNT', MIN: 0, MAX: 5},
    {ID: 'AUT', MIN: 0, MAX: 1},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

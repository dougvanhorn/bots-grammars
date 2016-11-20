#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD94BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 3},
    {ID: 'RFF', MIN: 0, MAX: 2, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'NAD', MIN: 1, MAX: 2, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 5},
    ]},
    {ID: 'LIN', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
        ]},
        {ID: 'RCS', MIN: 1, MAX: 10, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 10},
            {ID: 'MOA', MIN: 0, MAX: 1},
            {ID: 'LOC', MIN: 0, MAX: 4},
        ]},
    ]},
    {ID: 'AUT', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

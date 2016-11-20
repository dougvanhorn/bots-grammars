#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD07BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 1},
    {ID: 'TDT', MIN: 1, MAX: 1, LEVEL: [
        {ID: 'LOC', MIN: 1, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9},
    ]},
    {ID: 'EQD', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'CNT', MIN: 0, MAX: 99},
        {ID: 'DTM', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

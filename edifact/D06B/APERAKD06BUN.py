#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD06BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 9},
    {ID: 'FTX', MIN: 0, MAX: 9},
    {ID: 'CNT', MIN: 0, MAX: 9},
    {ID: 'DOC', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 99},
    ]},
    {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'NAD', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 9},
        {ID: 'COM', MIN: 0, MAX: 9},
    ]},
    {ID: 'ERC', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'FTX', MIN: 0, MAX: 1},
        {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

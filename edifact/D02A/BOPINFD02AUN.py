#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD02AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 9},
    {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'NAD', MIN: 1, MAX: 9, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 99},
    ]},
    {ID: 'RFF', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
        {ID: 'RCS', MIN: 1, MAX: 99, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 99},
            {ID: 'MOA', MIN: 0, MAX: 1},
            {ID: 'LOC', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'CNT', MIN: 0, MAX: 9},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

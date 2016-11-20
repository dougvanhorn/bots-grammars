#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD94BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'RFF', MIN: 0, MAX: 9},
    {ID: 'DTM', MIN: 0, MAX: 9},
    {ID: 'NAD', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 5},
        {ID: 'FII', MIN: 0, MAX: 1},
    ]},
    {ID: 'DOC', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'MOA', MIN: 0, MAX: 1},
        {ID: 'CUX', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 5},
        {ID: 'CCD', MIN: 0, MAX: 1},
        {ID: 'PCD', MIN: 0, MAX: 1},
        {ID: 'PAT', MIN: 0, MAX: 1},
        {ID: 'FTX', MIN: 0, MAX: 1},
        {ID: 'RFF', MIN: 0, MAX: 1},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

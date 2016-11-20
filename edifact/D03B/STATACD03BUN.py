#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD03BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 5},
    {ID: 'RFF', MIN: 0, MAX: 5},
    {ID: 'CUX', MIN: 0, MAX: 1},
    {ID: 'NAD', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'DOC', MIN: 1, MAX: 200000, LEVEL: [
        {ID: 'MOA', MIN: 1, MAX: 5},
        {ID: 'DTM', MIN: 0, MAX: 5},
        {ID: 'RFF', MIN: 0, MAX: 5},
    ]},
    {ID: 'UNS', MIN: 1, MAX: 1},
    {ID: 'MOA', MIN: 1, MAX: 9},
    {ID: 'FTX', MIN: 0, MAX: 99},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

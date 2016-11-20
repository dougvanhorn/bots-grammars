#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD96AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 1},
    {ID: 'NAD', MIN: 0, MAX: 9},
    {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'TDT', MIN: 1, MAX: 9, LEVEL: [
        {ID: 'LOC', MIN: 1, MAX: 1},
        {ID: 'DTM', MIN: 1, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 1},
        {ID: 'FTX', MIN: 0, MAX: 1},
    ]},
    {ID: 'LOC', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'MEA', MIN: 1, MAX: 9},
        {ID: 'DIM', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 1},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

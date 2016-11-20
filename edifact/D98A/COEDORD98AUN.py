#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD98AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 1},
    {ID: 'FTX', MIN: 0, MAX: 9},
    {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'NAD', MIN: 1, MAX: 9, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'EQD', MIN: 1, MAX: 9999, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'LOC', MIN: 0, MAX: 9},
        {ID: 'COD', MIN: 0, MAX: 1},
        {ID: 'HAN', MIN: 0, MAX: 9},
        {ID: 'DAM', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COD', MIN: 0, MAX: 1},
        ]},
        {ID: 'TDT', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'LOC', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'CNT', MIN: 0, MAX: 1},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

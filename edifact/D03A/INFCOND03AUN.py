#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD03AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 9},
    {ID: 'FTX', MIN: 0, MAX: 9},
    {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'NAD', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'LOC', MIN: 1, MAX: 999, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'NAD', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'CCI', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'CAV', MIN: 0, MAX: 9},
        ]},
        {ID: 'QTY', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
        ]},
        {ID: 'SCC', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

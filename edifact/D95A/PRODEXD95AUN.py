#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD95AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 2},
    {ID: 'MEA', MIN: 1, MAX: 1},
    {ID: 'NAD', MIN: 1, MAX: 2},
    {ID: 'RFF', MIN: 1, MAX: 5, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'IMD', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'QTY', MIN: 0, MAX: 10},
        {ID: 'LIN', MIN: 0, MAX: 9999, LEVEL: [
            {ID: 'GIS', MIN: 0, MAX: 2},
            {ID: 'LOC', MIN: 0, MAX: 2},
            {ID: 'DTM', MIN: 0, MAX: 1},
            {ID: 'MEA', MIN: 0, MAX: 5},
            {ID: 'QTY', MIN: 0, MAX: 5},
            {ID: 'TDT', MIN: 0, MAX: 5},
            {ID: 'RFF', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

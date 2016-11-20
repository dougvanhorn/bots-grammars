#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD98BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 1},
    {ID: 'GIS', MIN: 1, MAX: 1},
    {ID: 'RFF', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'PNA', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'GIR', MIN: 0, MAX: 1},
        {ID: 'NAT', MIN: 0, MAX: 1},
        {ID: 'DOC', MIN: 0, MAX: 1},
        {ID: 'ADR', MIN: 0, MAX: 2},
        {ID: 'ATT', MIN: 0, MAX: 5},
        {ID: 'DTM', MIN: 0, MAX: 2, LEVEL: [
            {ID: 'ADR', MIN: 0, MAX: 1},
        ]},
        {ID: 'PDI', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 2},
        ]},
    ]},
    {ID: 'FTX', MIN: 0, MAX: 1},
    {ID: 'AUT', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

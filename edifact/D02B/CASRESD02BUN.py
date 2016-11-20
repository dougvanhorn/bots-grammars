#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD02BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 9},
    {ID: 'ERC', MIN: 0, MAX: 9},
    {ID: 'LOC', MIN: 0, MAX: 9},
    {ID: 'RFF', MIN: 0, MAX: 9},
    {ID: 'MOA', MIN: 0, MAX: 99},
    {ID: 'FTX', MIN: 0, MAX: 9},
    {ID: 'NAD', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'SEQ', MIN: 0, MAX: 1},
        {ID: 'FTX', MIN: 0, MAX: 9},
    ]},
    {ID: 'DOC', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'GIR', MIN: 0, MAX: 99},
        {ID: 'PYT', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'MOA', MIN: 0, MAX: 99},
        {ID: 'FTX', MIN: 0, MAX: 9},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

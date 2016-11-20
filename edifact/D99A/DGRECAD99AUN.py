#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD99AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 9},
    {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'TDT', MIN: 1, MAX: 1, LEVEL: [
        {ID: 'DTM', MIN: 1, MAX: 2},
        {ID: 'LOC', MIN: 1, MAX: 2},
        {ID: 'RFF', MIN: 0, MAX: 2},
        {ID: 'MEA', MIN: 0, MAX: 1},
    ]},
    {ID: 'NAD', MIN: 1, MAX: 1, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 3},
        ]},
    ]},
    {ID: 'DGS', MIN: 1, MAX: 999, LEVEL: [
        {ID: 'FTX', MIN: 1, MAX: 9},
        {ID: 'MEA', MIN: 1, MAX: 1},
        {ID: 'LOC', MIN: 0, MAX: 99},
        {ID: 'SGP', MIN: 0, MAX: 99},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]
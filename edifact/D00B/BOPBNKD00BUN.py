#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD00BUN import recorddefs


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
    {ID: 'RFF', MIN: 1, MAX: 999, LEVEL: [
        {ID: 'CUX', MIN: 0, MAX: 1},
        {ID: 'MOA', MIN: 0, MAX: 9},
        {ID: 'LOC', MIN: 0, MAX: 1},
        {ID: 'RCS', MIN: 1, MAX: 999, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 1},
            {ID: 'MOA', MIN: 1, MAX: 9999, LEVEL: [
                {ID: 'ATT', MIN: 0, MAX: 1},
                {ID: 'NAD', MIN: 0, MAX: 1},
                {ID: 'GIR', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'QTY', MIN: 0, MAX: 1},
                    {ID: 'PRI', MIN: 0, MAX: 1},
                ]},
                {ID: 'RFF', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 1},
                ]},
                {ID: 'LOC', MIN: 1, MAX: 9},
            ]},
        ]},
    ]},
    {ID: 'CNT', MIN: 0, MAX: 9},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

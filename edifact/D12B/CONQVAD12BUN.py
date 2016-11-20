#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD12BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 9},
    {ID: 'AUT', MIN: 0, MAX: 2},
    {ID: 'FTX', MIN: 0, MAX: 5},
    {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 5},
    ]},
    {ID: 'NAD', MIN: 1, MAX: 9, LEVEL: [
        {ID: 'LOC', MIN: 0, MAX: 25},
        {ID: 'FII', MIN: 0, MAX: 5},
        {ID: 'RFF', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 5},
        ]},
        {ID: 'DOC', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 5},
        ]},
        {ID: 'CTA', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'BII', MIN: 0, MAX: 100000, LEVEL: [
        {ID: 'RCS', MIN: 0, MAX: 1},
        {ID: 'QTY', MIN: 1, MAX: 6},
        {ID: 'PRI', MIN: 0, MAX: 1},
        {ID: 'LIN', MIN: 1, MAX: 100, LEVEL: [
            {ID: 'IMD', MIN: 0, MAX: 1000, LEVEL: [
                {ID: 'RFF', MIN: 0, MAX: 5},
                {ID: 'GEI', MIN: 0, MAX: 5},
            ]},
        ]},
        {ID: 'TAX', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'MOA', MIN: 0, MAX: 1},
            {ID: 'LOC', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'CNT', MIN: 0, MAX: 5},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD95BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'RFF', MIN: 1, MAX: 2},
    {ID: 'DTM', MIN: 0, MAX: 4},
    {ID: 'MOA', MIN: 0, MAX: 2},
    {ID: 'LOC', MIN: 0, MAX: 3},
    {ID: 'TSR', MIN: 0, MAX: 1},
    {ID: 'FTX', MIN: 0, MAX: 3},
    {ID: 'FII', MIN: 1, MAX: 5, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 2},
        {ID: 'CTA', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 5},
    ]},
    {ID: 'NAD', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 1},
        {ID: 'CTA', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 5},
    ]},
    {ID: 'FCA', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'MOA', MIN: 0, MAX: 2},
        {ID: 'ALC', MIN: 0, MAX: 20, LEVEL: [
            {ID: 'PCD', MIN: 0, MAX: 3},
            {ID: 'MOA', MIN: 0, MAX: 3},
            {ID: 'DTM', MIN: 0, MAX: 1},
            {ID: 'TAX', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'MOA', MIN: 0, MAX: 2},
                {ID: 'DTM', MIN: 0, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'AUT', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

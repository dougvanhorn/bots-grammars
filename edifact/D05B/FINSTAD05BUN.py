#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD05BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 1},
    {ID: 'RFF', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'FII', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 5},
    ]},
    {ID: 'NAD', MIN: 0, MAX: 3, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 5},
    ]},
    {ID: 'LIN', MIN: 1, MAX: 9999, LEVEL: [
        {ID: 'FII', MIN: 1, MAX: 1},
        {ID: 'RFF', MIN: 1, MAX: 1},
        {ID: 'FTX', MIN: 0, MAX: 1},
        {ID: 'MOA', MIN: 1, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
        ]},
        {ID: 'SEQ', MIN: 0, MAX: 9999, LEVEL: [
            {ID: 'RFF', MIN: 1, MAX: 5},
            {ID: 'DTM', MIN: 1, MAX: 2},
            {ID: 'BUS', MIN: 1, MAX: 1},
            {ID: 'MOA', MIN: 1, MAX: 1},
            {ID: 'FTX', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'CNT', MIN: 0, MAX: 5},
    {ID: 'AUT', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

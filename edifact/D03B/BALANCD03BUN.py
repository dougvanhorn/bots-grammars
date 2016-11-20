#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD03BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 99},
    {ID: 'RFF', MIN: 0, MAX: 99},
    {ID: 'CUX', MIN: 0, MAX: 99},
    {ID: 'FTX', MIN: 0, MAX: 1},
    {ID: 'NAD', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'CTA', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'CCI', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'CAV', MIN: 0, MAX: 1},
    ]},
    {ID: 'LIN', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'MOA', MIN: 1, MAX: 999},
        {ID: 'DTM', MIN: 0, MAX: 1},
        {ID: 'RFF', MIN: 0, MAX: 1},
        {ID: 'QTY', MIN: 0, MAX: 10},
        {ID: 'CPT', MIN: 1, MAX: 9, LEVEL: [
            {ID: 'CCI', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'CAV', MIN: 0, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'EQN', MIN: 1, MAX: 1, LEVEL: [
        {ID: 'MOA', MIN: 1, MAX: 9},
    ]},
    {ID: 'AUT', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

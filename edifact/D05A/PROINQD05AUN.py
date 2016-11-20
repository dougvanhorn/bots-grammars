#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD05AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 9},
    {ID: 'CUX', MIN: 0, MAX: 1},
    {ID: 'NAD', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'LIN', MIN: 1, MAX: 9999, LEVEL: [
        {ID: 'CCI', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'CAV', MIN: 0, MAX: 10},
            {ID: 'MEA', MIN: 0, MAX: 10},
        ]},
        {ID: 'IRQ', MIN: 0, MAX: 9999, LEVEL: [
            {ID: 'PIA', MIN: 0, MAX: 10},
            {ID: 'IMD', MIN: 0, MAX: 10},
            {ID: 'MEA', MIN: 0, MAX: 10},
            {ID: 'NAD', MIN: 0, MAX: 10},
            {ID: 'PGI', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 5},
            {ID: 'PRI', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'RNG', MIN: 0, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

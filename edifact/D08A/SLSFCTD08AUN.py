#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD08AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 5},
    {ID: 'NAD', MIN: 1, MAX: 5, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'RFF', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 5},
    ]},
    {ID: 'CUX', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 5},
    ]},
    {ID: 'LOC', MIN: 1, MAX: 200000, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 5},
        {ID: 'LIN', MIN: 0, MAX: 200000, LEVEL: [
            {ID: 'PIA', MIN: 0, MAX: 5},
            {ID: 'IMD', MIN: 0, MAX: 5},
            {ID: 'PAC', MIN: 0, MAX: 5},
            {ID: 'RFF', MIN: 0, MAX: 5},
            {ID: 'DOC', MIN: 0, MAX: 5},
            {ID: 'ALI', MIN: 0, MAX: 5},
            {ID: 'MOA', MIN: 0, MAX: 5},
            {ID: 'PRI', MIN: 0, MAX: 5},
            {ID: 'QTY', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'MKS', MIN: 0, MAX: 1},
                {ID: 'NAD', MIN: 0, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

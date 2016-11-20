#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD98AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 3},
    {ID: 'RFF', MIN: 0, MAX: 2, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'NAD', MIN: 1, MAX: 2, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 5},
    ]},
    {ID: 'LIN', MIN: 1, MAX: 9999, LEVEL: [
        {ID: 'FII', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 1},
        {ID: 'RFF', MIN: 0, MAX: 2, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
        ]},
        {ID: 'NAD', MIN: 0, MAX: 4, LEVEL: [
            {ID: 'CTA', MIN: 0, MAX: 1},
            {ID: 'COM', MIN: 0, MAX: 5},
        ]},
        {ID: 'MOA', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'CUX', MIN: 0, MAX: 1},
        ]},
        {ID: 'DOC', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
        ]},
        {ID: 'RCS', MIN: 1, MAX: 10, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 10},
            {ID: 'MOA', MIN: 0, MAX: 1},
            {ID: 'LOC', MIN: 0, MAX: 4},
        ]},
    ]},
    {ID: 'AUT', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

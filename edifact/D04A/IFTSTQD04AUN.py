#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD04AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 9},
    {ID: 'LOC', MIN: 0, MAX: 99},
    {ID: 'RFF', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'TDT', MIN: 0, MAX: 99},
    {ID: 'EQD', MIN: 0, MAX: 999},
    {ID: 'NAD', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'CNI', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'LOC', MIN: 0, MAX: 99},
        {ID: 'RFF', MIN: 0, MAX: 99},
        {ID: 'TDT', MIN: 0, MAX: 99},
        {ID: 'EQD', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'TPL', MIN: 0, MAX: 9},
        ]},
        {ID: 'NAD', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'GID', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'FTX', MIN: 0, MAX: 1},
                {ID: 'SGP', MIN: 0, MAX: 99},
            ]},
            {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'COM', MIN: 0, MAX: 9},
            ]},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

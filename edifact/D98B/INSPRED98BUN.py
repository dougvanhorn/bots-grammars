#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD98BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 0, MAX: 1},
    {ID: 'RFF', MIN: 0, MAX: 9},
    {ID: 'DTM', MIN: 1, MAX: 9},
    {ID: 'ATT', MIN: 1, MAX: 9, LEVEL: [
        {ID: 'PCD', MIN: 0, MAX: 1},
    ]},
    {ID: 'ICD', MIN: 0, MAX: 1},
    {ID: 'NAD', MIN: 1, MAX: 9, LEVEL: [
        {ID: 'ATT', MIN: 0, MAX: 1},
        {ID: 'CTA', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 3},
        {ID: 'RFF', MIN: 0, MAX: 9},
    ]},
    {ID: 'DTM', MIN: 1, MAX: 3, LEVEL: [
        {ID: 'ICD', MIN: 1, MAX: 99, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 1},
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'MOA', MIN: 1, MAX: 99, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 1},
                {ID: 'IND', MIN: 0, MAX: 2, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 1},
                ]},
                {ID: 'ATT', MIN: 0, MAX: 2, LEVEL: [
                    {ID: 'PCD', MIN: 0, MAX: 1},
                ]},
                {ID: 'TAX', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'PCD', MIN: 0, MAX: 1},
                ]},
            ]},
        ]},
        {ID: 'CUX', MIN: 1, MAX: 1},
    ]},
    {ID: 'MOA', MIN: 1, MAX: 10},
    {ID: 'FTX', MIN: 0, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 15, LEVEL: [
        {ID: 'MOA', MIN: 1, MAX: 1},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

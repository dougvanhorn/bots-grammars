#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD09AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'PAI', MIN: 1, MAX: 1},
    {ID: 'FII', MIN: 1, MAX: 2},
    {ID: 'DTM', MIN: 1, MAX: 4},
    {ID: 'CUX', MIN: 0, MAX: 1},
    {ID: 'PYT', MIN: 0, MAX: 1},
    {ID: 'FTX', MIN: 0, MAX: 5},
    {ID: 'RFF', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'NAD', MIN: 0, MAX: 6, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'GEI', MIN: 1, MAX: 9, LEVEL: [
        {ID: 'RFF', MIN: 1, MAX: 1},
        {ID: 'MOA', MIN: 1, MAX: 9},
        {ID: 'BUS', MIN: 0, MAX: 1},
        {ID: 'CUX', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 1, MAX: 99, LEVEL: [
            {ID: 'UGH', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'NAD', MIN: 0, MAX: 999999, LEVEL: [
                    {ID: 'RFF', MIN: 0, MAX: 9},
                    {ID: 'MOA', MIN: 1, MAX: 9},
                    {ID: 'AJT', MIN: 0, MAX: 9},
                    {ID: 'PYT', MIN: 0, MAX: 1},
                    {ID: 'FTX', MIN: 0, MAX: 3},
                    {ID: 'DTM', MIN: 0, MAX: 9},
                ]},
                {ID: 'UGT', MIN: 1, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'UNS', MIN: 1, MAX: 1},
    {ID: 'MOA', MIN: 1, MAX: 1},
    {ID: 'CNT', MIN: 0, MAX: 9},
    {ID: 'AUT', MIN: 0, MAX: 1},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

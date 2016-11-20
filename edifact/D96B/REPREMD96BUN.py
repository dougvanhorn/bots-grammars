#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD96BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'GIS', MIN: 1, MAX: 5},
    {ID: 'NAD', MIN: 1, MAX: 9, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 5},
        {ID: 'RFF', MIN: 0, MAX: 9},
    ]},
    {ID: 'DTM', MIN: 1, MAX: 9},
    {ID: 'FTX', MIN: 0, MAX: 3},
    {ID: 'REL', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'GIS', MIN: 0, MAX: 5},
        {ID: 'CUX', MIN: 1, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'QTY', MIN: 0, MAX: 9},
        {ID: 'LOC', MIN: 0, MAX: 1},
        {ID: 'PCD', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 3},
        {ID: 'ARD', MIN: 1, MAX: 9, LEVEL: [
            {ID: 'MOA', MIN: 1, MAX: 99, LEVEL: [
                {ID: 'GIS', MIN: 0, MAX: 9},
                {ID: 'PCD', MIN: 0, MAX: 9},
                {ID: 'FTX', MIN: 0, MAX: 2},
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 2},
                    {ID: 'COM', MIN: 0, MAX: 1},
                    {ID: 'FTX', MIN: 0, MAX: 1},
                ]},
                {ID: 'CUX', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'MOA', MIN: 0, MAX: 1},
                    {ID: 'AJT', MIN: 1, MAX: 1},
                ]},
            ]},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

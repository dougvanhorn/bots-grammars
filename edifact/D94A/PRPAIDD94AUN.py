#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD94AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 0, MAX: 1},
    {ID: 'GIS', MIN: 1, MAX: 1},
    {ID: 'RFF', MIN: 1, MAX: 9},
    {ID: 'DTM', MIN: 1, MAX: 9},
    {ID: 'NAD', MIN: 1, MAX: 2, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 3},
        {ID: 'RFF', MIN: 0, MAX: 9},
    ]},
    {ID: 'DOC', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'GIS', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 1},
        ]},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'NAD', MIN: 0, MAX: 1},
        {ID: 'MOA', MIN: 1, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
            {ID: 'PCD', MIN: 0, MAX: 1},
        ]},
        {ID: 'RFF', MIN: 1, MAX: 9},
        {ID: 'ICD', MIN: 0, MAX: 1},
        {ID: 'ATT', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'PCD', MIN: 0, MAX: 1},
        ]},
        {ID: 'CUX', MIN: 0, MAX: 1},
    ]},
    {ID: 'MOA', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'GIS', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 1},
        {ID: 'RFF', MIN: 0, MAX: 1},
        {ID: 'ATT', MIN: 0, MAX: 1},
        {ID: 'ICD', MIN: 0, MAX: 1},
        {ID: 'CUX', MIN: 0, MAX: 1},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

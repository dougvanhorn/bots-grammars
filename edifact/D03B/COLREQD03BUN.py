#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD03BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 1},
    {ID: 'FCA', MIN: 1, MAX: 1},
    {ID: 'DOC', MIN: 1, MAX: 40},
    {ID: 'INP', MIN: 0, MAX: 20},
    {ID: 'FTX', MIN: 0, MAX: 15},
    {ID: 'FII', MIN: 1, MAX: 7, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 1},
        {ID: 'CTA', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 5},
    ]},
    {ID: 'NAD', MIN: 1, MAX: 9, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 3},
        {ID: 'CTA', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 5},
    ]},
    {ID: 'PYT', MIN: 1, MAX: 1, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
        {ID: 'FTX', MIN: 0, MAX: 1},
    ]},
    {ID: 'MOA', MIN: 1, MAX: 5, LEVEL: [
        {ID: 'FTX', MIN: 0, MAX: 1},
    ]},
    {ID: 'TDT', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
        {ID: 'LOC', MIN: 0, MAX: 3},
    ]},
    {ID: 'GEI', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'MOA', MIN: 0, MAX: 1},
        {ID: 'LOC', MIN: 0, MAX: 2},
        {ID: 'NAD', MIN: 0, MAX: 1},
        {ID: 'RCS', MIN: 0, MAX: 1},
        {ID: 'FTX', MIN: 0, MAX: 10},
    ]},
    {ID: 'AUT', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

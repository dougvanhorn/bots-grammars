#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD95BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 5},
    {ID: 'FII', MIN: 0, MAX: 10},
    {ID: 'FTX', MIN: 0, MAX: 5},
    {ID: 'RFF', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'NAD', MIN: 0, MAX: 2, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'UNS', MIN: 1, MAX: 1},
    {ID: 'NAD', MIN: 0, MAX: 200000, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 5},
        {ID: 'FII', MIN: 0, MAX: 10},
        {ID: 'LOC', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 2},
        ]},
        {ID: 'RFF', MIN: 0, MAX: 15, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
        ]},
        {ID: 'CTA', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 5},
        ]},
        {ID: 'SCC', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 2},
        ]},
        {ID: 'TOD', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'LOC', MIN: 0, MAX: 1},
        ]},
        {ID: 'PAI', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'PAT', MIN: 0, MAX: 1},
            {ID: 'CUX', MIN: 0, MAX: 2},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

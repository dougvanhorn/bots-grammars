#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD95BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'RFF', MIN: 1, MAX: 6},
    {ID: 'PAI', MIN: 0, MAX: 1},
    {ID: 'CUX', MIN: 0, MAX: 1},
    {ID: 'FII', MIN: 0, MAX: 2},
    {ID: 'DTM', MIN: 0, MAX: 9},
    {ID: 'PAT', MIN: 0, MAX: 1},
    {ID: 'FTX', MIN: 0, MAX: 5},
    {ID: 'NAD', MIN: 0, MAX: 6, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'UNS', MIN: 1, MAX: 1},
    {ID: 'NAD', MIN: 1, MAX: 999999, LEVEL: [
        {ID: 'ATT', MIN: 0, MAX: 1},
        {ID: 'RFF', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 1},
        {ID: 'EMP', MIN: 0, MAX: 1},
        {ID: 'LOC', MIN: 0, MAX: 1},
        {ID: 'FTX', MIN: 0, MAX: 3},
        {ID: 'PAT', MIN: 1, MAX: 9, LEVEL: [
            {ID: 'MOA', MIN: 0, MAX: 1},
            {ID: 'CUX', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 3},
            {ID: 'FTX', MIN: 0, MAX: 3},
            {ID: 'COT', MIN: 1, MAX: 99, LEVEL: [
                {ID: 'MOA', MIN: 1, MAX: 1},
                {ID: 'DTM', MIN: 0, MAX: 3},
                {ID: 'FTX', MIN: 0, MAX: 3},
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

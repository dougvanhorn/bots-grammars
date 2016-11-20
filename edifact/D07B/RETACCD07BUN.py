#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD07BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'GEI', MIN: 1, MAX: 6},
    {ID: 'NAD', MIN: 1, MAX: 9, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 5},
        {ID: 'RFF', MIN: 0, MAX: 9},
    ]},
    {ID: 'DTM', MIN: 1, MAX: 4},
    {ID: 'FTX', MIN: 0, MAX: 5},
    {ID: 'CUX', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'RFF', MIN: 1, MAX: 5},
        {ID: 'FTX', MIN: 0, MAX: 1},
        {ID: 'MOA', MIN: 1, MAX: 999, LEVEL: [
            {ID: 'DTM', MIN: 1, MAX: 10},
            {ID: 'PCD', MIN: 0, MAX: 2},
            {ID: 'GEI', MIN: 0, MAX: 10},
            {ID: 'LOC', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 3},
            {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 1},
                {ID: 'COM', MIN: 0, MAX: 1},
                {ID: 'FTX', MIN: 0, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'UNS', MIN: 1, MAX: 1},
    {ID: 'MOA', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'GEI', MIN: 0, MAX: 1},
        {ID: 'NAD', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'PCD', MIN: 0, MAX: 1},
            {ID: 'RFF', MIN: 0, MAX: 2},
            {ID: 'GEI', MIN: 0, MAX: 1},
            {ID: 'MOA', MIN: 0, MAX: 1},
        ]},
        {ID: 'PAI', MIN: 1, MAX: 1},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 3},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

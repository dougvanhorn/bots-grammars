#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD97BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 9},
    {ID: 'CNT', MIN: 1, MAX: 1},
    {ID: 'FTX', MIN: 0, MAX: 5},
    {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'TDT', MIN: 1, MAX: 1, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
        {ID: 'CTA', MIN: 0, MAX: 1},
    ]},
    {ID: 'NAD', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'LOC', MIN: 1, MAX: 3, LEVEL: [
        {ID: 'NAD', MIN: 0, MAX: 1},
        {ID: 'RFF', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'EQD', MIN: 0, MAX: 9999, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'SEL', MIN: 0, MAX: 1},
    ]},
    {ID: 'CNI', MIN: 1, MAX: 9999, LEVEL: [
        {ID: 'LOC', MIN: 0, MAX: 2},
        {ID: 'RFF', MIN: 0, MAX: 2},
        {ID: 'NAD', MIN: 0, MAX: 2},
        {ID: 'GID', MIN: 1, MAX: 9999, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 5},
            {ID: 'PCI', MIN: 0, MAX: 1},
            {ID: 'DGS', MIN: 1, MAX: 1, LEVEL: [
                {ID: 'FTX', MIN: 1, MAX: 9},
                {ID: 'LOC', MIN: 0, MAX: 99},
                {ID: 'MEA', MIN: 1, MAX: 9},
                {ID: 'SGP', MIN: 0, MAX: 9999, LEVEL: [
                    {ID: 'LOC', MIN: 0, MAX: 1},
                    {ID: 'MEA', MIN: 0, MAX: 2},
                ]},
            ]},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

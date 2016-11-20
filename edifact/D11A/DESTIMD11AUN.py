#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD11AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 9},
    {ID: 'GEI', MIN: 0, MAX: 1},
    {ID: 'CUX', MIN: 0, MAX: 9},
    {ID: 'RFF', MIN: 0, MAX: 9},
    {ID: 'FTX', MIN: 0, MAX: 9},
    {ID: 'EQD', MIN: 1, MAX: 1, LEVEL: [
        {ID: 'DIM', MIN: 0, MAX: 1},
        {ID: 'IMD', MIN: 0, MAX: 9},
    ]},
    {ID: 'NAD', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'MOA', MIN: 0, MAX: 9},
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'TDT', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'LOC', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'UNS', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'LOC', MIN: 0, MAX: 1},
        {ID: 'NAD', MIN: 0, MAX: 9},
    ]},
    {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
        {ID: 'NAD', MIN: 0, MAX: 9},
        {ID: 'MOA', MIN: 0, MAX: 1},
    ]},
    {ID: 'LIN', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'DIM', MIN: 0, MAX: 1},
        {ID: 'QTY', MIN: 0, MAX: 1},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'DAM', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'COD', MIN: 0, MAX: 1},
        ]},
        {ID: 'RTE', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'QTY', MIN: 1, MAX: 1},
        ]},
        {ID: 'NAD', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'MOA', MIN: 1, MAX: 9, LEVEL: [
                {ID: 'TAX', MIN: 0, MAX: 1},
                {ID: 'MEA', MIN: 0, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'CNT', MIN: 0, MAX: 9},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

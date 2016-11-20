#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD02BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 5},
    {ID: 'AUT', MIN: 0, MAX: 2},
    {ID: 'AGR', MIN: 0, MAX: 2},
    {ID: 'FTX', MIN: 0, MAX: 10},
    {ID: 'RFF', MIN: 1, MAX: 5, LEVEL: [
        {ID: 'DOC', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 1},
        {ID: 'FTX', MIN: 0, MAX: 5},
    ]},
    {ID: 'NAD', MIN: 1, MAX: 999, LEVEL: [
        {ID: 'LOC', MIN: 0, MAX: 99},
        {ID: 'FTX', MIN: 0, MAX: 10},
        {ID: 'RFF', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'CED', MIN: 0, MAX: 10},
            {ID: 'DTM', MIN: 0, MAX: 1},
        ]},
        {ID: 'CTA', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 5},
            {ID: 'LOC', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'DOC', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'INP', MIN: 0, MAX: 99},
        {ID: 'RFF', MIN: 0, MAX: 1},
        {ID: 'MEA', MIN: 0, MAX: 1},
        {ID: 'EFI', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'CED', MIN: 0, MAX: 10},
            {ID: 'DTM', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'BII', MIN: 0, MAX: 100000, LEVEL: [
        {ID: 'GEI', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 1},
        {ID: 'IMD', MIN: 0, MAX: 1},
        {ID: 'RFF', MIN: 0, MAX: 5},
        {ID: 'QTY', MIN: 0, MAX: 1},
        {ID: 'LOC', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'DIM', MIN: 0, MAX: 5},
            {ID: 'QTY', MIN: 0, MAX: 5},
            {ID: 'MEA', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

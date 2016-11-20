#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD96AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'NAD', MIN: 0, MAX: 5},
    {ID: 'LOC', MIN: 0, MAX: 5},
    {ID: 'DTM', MIN: 0, MAX: 7},
    {ID: 'GIS', MIN: 0, MAX: 10},
    {ID: 'FTX', MIN: 0, MAX: 5},
    {ID: 'EQD', MIN: 0, MAX: 999},
    {ID: 'ERP', MIN: 0, MAX: 50, LEVEL: [
        {ID: 'ERC', MIN: 0, MAX: 50},
    ]},
    {ID: 'PAC', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'PCI', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'TAX', MIN: 0, MAX: 50, LEVEL: [
        {ID: 'MOA', MIN: 0, MAX: 2},
        {ID: 'GIS', MIN: 0, MAX: 1},
    ]},
    {ID: 'RFF', MIN: 1, MAX: 9999, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
        {ID: 'MEA', MIN: 0, MAX: 20},
        {ID: 'EQD', MIN: 0, MAX: 99},
        {ID: 'MOA', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'CUX', MIN: 0, MAX: 1},
        ]},
        {ID: 'TAX', MIN: 0, MAX: 20, LEVEL: [
            {ID: 'MOA', MIN: 0, MAX: 2},
            {ID: 'GIS', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'DOC', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 2},
        {ID: 'LOC', MIN: 0, MAX: 1},
    ]},
    {ID: 'AUT', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD02BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 9},
    {ID: 'FTX', MIN: 0, MAX: 9},
    {ID: 'RFF', MIN: 0, MAX: 9},
    {ID: 'NAD', MIN: 1, MAX: 9, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'TDT', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'MEA', MIN: 0, MAX: 99},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'LOC', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
        ]},
        {ID: 'GOR', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'NAD', MIN: 0, MAX: 99},
        ]},
    ]},
    {ID: 'TSR', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'QTY', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'LOC', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'MEA', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'QTY', MIN: 0, MAX: 9},
            {ID: 'POC', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 9},
            {ID: 'HAN', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'NAD', MIN: 0, MAX: 9},
                {ID: 'GDS', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'FTX', MIN: 0, MAX: 9},
                    {ID: 'MEA', MIN: 0, MAX: 9},
                    {ID: 'EQN', MIN: 0, MAX: 9},
                    {ID: 'DGS', MIN: 0, MAX: 9},
                ]},
            ]},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

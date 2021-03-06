#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD01BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 99},
    {ID: 'RFF', MIN: 0, MAX: 9999, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 99},
    ]},
    {ID: 'NAD', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
        ]},
        {ID: 'CTA', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'DOC', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'LIN', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'PIA', MIN: 0, MAX: 99},
            {ID: 'IMD', MIN: 0, MAX: 99},
            {ID: 'DTM', MIN: 0, MAX: 99},
            {ID: 'ALI', MIN: 0, MAX: 9},
            {ID: 'RFF', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 9},
            ]},
            {ID: 'NAD', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'COM', MIN: 0, MAX: 9},
                ]},
            ]},
            {ID: 'CCI', MIN: 0, MAX: 9999, LEVEL: [
                {ID: 'CAV', MIN: 0, MAX: 99},
                {ID: 'FTX', MIN: 0, MAX: 99},
            ]},
        ]},
    ]},
    {ID: 'CNT', MIN: 0, MAX: 99},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD08BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 99},
    {ID: 'RFF', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'NAD', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'LOC', MIN: 0, MAX: 99},
    ]},
    {ID: 'DOC', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 99},
        ]},
        {ID: 'NAD', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'CTA', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'COM', MIN: 0, MAX: 99},
            ]},
        ]},
        {ID: 'LIN', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'PIA', MIN: 0, MAX: 99},
            {ID: 'IMD', MIN: 0, MAX: 99},
            {ID: 'DTM', MIN: 0, MAX: 99},
            {ID: 'RFF', MIN: 0, MAX: 99},
            {ID: 'FTX', MIN: 0, MAX: 9},
            {ID: 'NAD', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'GEI', MIN: 0, MAX: 99},
                {ID: 'LOC', MIN: 0, MAX: 99},
                {ID: 'QTY', MIN: 0, MAX: 99},
                {ID: 'QVR', MIN: 0, MAX: 99},
                {ID: 'RFF', MIN: 0, MAX: 99},
                {ID: 'FTX', MIN: 0, MAX: 9},
                {ID: 'GIN', MIN: 0, MAX: 999, LEVEL: [
                    {ID: 'RFF', MIN: 0, MAX: 99},
                ]},
            ]},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

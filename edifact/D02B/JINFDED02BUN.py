#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD02BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 2},
    {ID: 'PNA', MIN: 1, MAX: 9, LEVEL: [
        {ID: 'ADR', MIN: 0, MAX: 1},
        {ID: 'LOC', MIN: 0, MAX: 5},
        {ID: 'DTM', MIN: 0, MAX: 5},
        {ID: 'CTA', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'RFF', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 5},
    ]},
    {ID: 'GEI', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'FTX', MIN: 0, MAX: 1},
    ]},
    {ID: 'UNS', MIN: 1, MAX: 1},
    {ID: 'RFF', MIN: 1, MAX: 999, LEVEL: [
        {ID: 'PNA', MIN: 1, MAX: 999, LEVEL: [
            {ID: 'ADR', MIN: 0, MAX: 1},
            {ID: 'LOC', MIN: 0, MAX: 2},
            {ID: 'DTM', MIN: 0, MAX: 5},
            {ID: 'NAT', MIN: 0, MAX: 9},
            {ID: 'PDI', MIN: 0, MAX: 1},
            {ID: 'DOC', MIN: 0, MAX: 9},
            {ID: 'CTA', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'COM', MIN: 0, MAX: 5},
            ]},
        ]},
        {ID: 'RFF', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 5},
        ]},
        {ID: 'FTX', MIN: 1, MAX: 30},
        {ID: 'GEI', MIN: 0, MAX: 30, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

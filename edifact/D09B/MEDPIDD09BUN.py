#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD09BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 9},
    {ID: 'RFF', MIN: 0, MAX: 9},
    {ID: 'FTX', MIN: 0, MAX: 99},
    {ID: 'PNA', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'ADR', MIN: 0, MAX: 9},
        {ID: 'CTA', MIN: 0, MAX: 9},
        {ID: 'COM', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 99},
        {ID: 'LAN', MIN: 0, MAX: 9},
    ]},
    {ID: 'GEI', MIN: 1, MAX: 9999, LEVEL: [
        {ID: 'PNA', MIN: 0, MAX: 1},
        {ID: 'ADR', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 99},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'IHC', MIN: 0, MAX: 9},
        {ID: 'NAT', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'LAN', MIN: 0, MAX: 9},
        {ID: 'HAN', MIN: 0, MAX: 9},
        {ID: 'LOC', MIN: 0, MAX: 9},
        {ID: 'FII', MIN: 0, MAX: 9},
        {ID: 'CTA', MIN: 0, MAX: 9},
        {ID: 'PDI', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
        ]},
        {ID: 'COM', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'CTA', MIN: 0, MAX: 9},
        ]},
        {ID: 'REL', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'PNA', MIN: 0, MAX: 1},
            {ID: 'ADR', MIN: 0, MAX: 9},
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'PDI', MIN: 0, MAX: 1},
            {ID: 'IHC', MIN: 0, MAX: 9},
            {ID: 'NAT', MIN: 0, MAX: 9},
            {ID: 'LAN', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'AUT', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

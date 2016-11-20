#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD08AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'RFF', MIN: 0, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 9},
    {ID: 'LOC', MIN: 0, MAX: 9},
    {ID: 'NAD', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 9},
    ]},
    {ID: 'TDT', MIN: 1, MAX: 10, LEVEL: [
        {ID: 'DTM', MIN: 1, MAX: 1},
        {ID: 'LOC', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'NAD', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'ATT', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'MEA', MIN: 0, MAX: 9},
        {ID: 'GEI', MIN: 0, MAX: 5},
        {ID: 'FTX', MIN: 0, MAX: 99},
        {ID: 'LOC', MIN: 0, MAX: 25},
        {ID: 'COM', MIN: 0, MAX: 1},
        {ID: 'EMP', MIN: 0, MAX: 9},
        {ID: 'NAT', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 1},
        {ID: 'DOC', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 5},
            {ID: 'GEI', MIN: 0, MAX: 9},
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'LOC', MIN: 0, MAX: 2},
            {ID: 'CPI', MIN: 0, MAX: 1},
            {ID: 'QTY', MIN: 0, MAX: 9},
        ]},
        {ID: 'GID', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 9},
            {ID: 'QTY', MIN: 0, MAX: 9},
        ]},
        {ID: 'TDT', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'CNT', MIN: 0, MAX: 1},
    {ID: 'AUT', MIN: 0, MAX: 1},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

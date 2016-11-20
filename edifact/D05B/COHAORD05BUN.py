#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD05BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 9},
    {ID: 'FTX', MIN: 0, MAX: 9},
    {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'NAD', MIN: 1, MAX: 9, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'EQD', MIN: 1, MAX: 9999, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'LOC', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'GOR', MIN: 0, MAX: 9},
        {ID: 'HAN', MIN: 0, MAX: 9},
        {ID: 'MEA', MIN: 0, MAX: 9},
        {ID: 'PCD', MIN: 0, MAX: 9},
        {ID: 'TDT', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'LOC', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 9},
            ]},
        ]},
        {ID: 'NAD', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'COM', MIN: 0, MAX: 9},
            ]},
        ]},
        {ID: 'DGS', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 9},
            {ID: 'MEA', MIN: 0, MAX: 9},
            {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'COM', MIN: 0, MAX: 9},
            ]},
        ]},
        {ID: 'TMP', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'RNG', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'CNT', MIN: 0, MAX: 1},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

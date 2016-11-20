#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD12BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 1},
    {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'NAD', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'TDT', MIN: 1, MAX: 3, LEVEL: [
        {ID: 'LOC', MIN: 1, MAX: 1},
        {ID: 'DTM', MIN: 1, MAX: 99},
        {ID: 'RFF', MIN: 0, MAX: 1},
        {ID: 'FTX', MIN: 0, MAX: 1},
    ]},
    {ID: 'HAN', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'LOC', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'RFF', MIN: 1, MAX: 99},
            {ID: 'FTX', MIN: 0, MAX: 9},
            {ID: 'MEA', MIN: 0, MAX: 9},
            {ID: 'DIM', MIN: 0, MAX: 9},
            {ID: 'LOC', MIN: 0, MAX: 9},
            {ID: 'NAD', MIN: 1, MAX: 99},
            {ID: 'TMP', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'RNG', MIN: 0, MAX: 1},
            ]},
            {ID: 'EQD', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'EQN', MIN: 0, MAX: 1},
            ]},
            {ID: 'EQA', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'EQN', MIN: 0, MAX: 1},
            ]},
            {ID: 'GID', MIN: 0, MAX: 9999, LEVEL: [
                {ID: 'GDS', MIN: 0, MAX: 1},
            ]},
            {ID: 'RFF', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'DGS', MIN: 1, MAX: 99, LEVEL: [
                    {ID: 'FTX', MIN: 0, MAX: 1},
                ]},
            ]},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

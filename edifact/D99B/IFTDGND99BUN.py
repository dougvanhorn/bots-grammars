#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD99BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 9},
    {ID: 'FTX', MIN: 0, MAX: 9},
    {ID: 'HAN', MIN: 0, MAX: 1},
    {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'TDT', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'LOC', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'NAD', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'EQD', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'MEA', MIN: 0, MAX: 9},
    ]},
    {ID: 'CNI', MIN: 1, MAX: 999, LEVEL: [
        {ID: 'HAN', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 4},
        {ID: 'LOC', MIN: 0, MAX: 4},
        {ID: 'TDT', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'LOC', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 9},
            ]},
        ]},
        {ID: 'NAD', MIN: 0, MAX: 2, LEVEL: [
            {ID: 'CTA', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'COM', MIN: 0, MAX: 1},
            ]},
            {ID: 'RFF', MIN: 0, MAX: 1},
        ]},
        {ID: 'GID', MIN: 1, MAX: 99, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 2},
            {ID: 'PCI', MIN: 0, MAX: 1},
            {ID: 'SGP', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'MEA', MIN: 0, MAX: 9},
            ]},
            {ID: 'DGS', MIN: 1, MAX: 1, LEVEL: [
                {ID: 'FTX', MIN: 1, MAX: 9},
                {ID: 'MEA', MIN: 1, MAX: 9},
                {ID: 'LOC', MIN: 0, MAX: 99},
                {ID: 'RFF', MIN: 0, MAX: 9},
                {ID: 'SGP', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'LOC', MIN: 0, MAX: 1},
                    {ID: 'MEA', MIN: 0, MAX: 2},
                ]},
            ]},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

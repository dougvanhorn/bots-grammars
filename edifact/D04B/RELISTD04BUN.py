#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD04BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 9},
    {ID: 'AGR', MIN: 1, MAX: 1},
    {ID: 'RFF', MIN: 1, MAX: 1},
    {ID: 'PNA', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'ATT', MIN: 0, MAX: 1},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'IDE', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'ROD', MIN: 1, MAX: 999, LEVEL: [
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 9},
            {ID: 'PNA', MIN: 0, MAX: 99},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'QTY', MIN: 0, MAX: 9},
            {ID: 'NAT', MIN: 0, MAX: 9},
            {ID: 'PER', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 2, LEVEL: [
                    {ID: 'GEI', MIN: 0, MAX: 1},
                ]},
            ]},
            {ID: 'ADR', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 9},
            ]},
            {ID: 'ATT', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'APP', MIN: 0, MAX: 1},
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'PCD', MIN: 0, MAX: 9},
            ]},
            {ID: 'PRV', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'APP', MIN: 0, MAX: 1},
                {ID: 'MOA', MIN: 0, MAX: 9},
                {ID: 'RTE', MIN: 0, MAX: 9},
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'QTY', MIN: 0, MAX: 9},
                {ID: 'ATT', MIN: 0, MAX: 99},
                {ID: 'BAS', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'APP', MIN: 0, MAX: 1},
                ]},
            ]},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

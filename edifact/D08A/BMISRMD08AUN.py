#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD08AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 1},
    {ID: 'RFF', MIN: 1, MAX: 9},
    {ID: 'LOC', MIN: 1, MAX: 9},
    {ID: 'FTX', MIN: 0, MAX: 99},
    {ID: 'PNA', MIN: 1, MAX: 9, LEVEL: [
        {ID: 'ADR', MIN: 0, MAX: 1},
        {ID: 'RFF', MIN: 0, MAX: 1},
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'DTM', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'STS', MIN: 0, MAX: 1},
        {ID: 'FTX', MIN: 0, MAX: 9},
    ]},
    {ID: 'LIN', MIN: 1, MAX: 999, LEVEL: [
        {ID: 'QTY', MIN: 0, MAX: 1},
        {ID: 'FTX', MIN: 0, MAX: 99},
        {ID: 'PNA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'ADR', MIN: 0, MAX: 1},
            {ID: 'RFF', MIN: 0, MAX: 1},
            {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'COM', MIN: 0, MAX: 9},
            ]},
        ]},
        {ID: 'TDT', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'EQD', MIN: 0, MAX: 1},
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'QTY', MIN: 0, MAX: 1},
            {ID: 'MEA', MIN: 0, MAX: 99},
            {ID: 'PCD', MIN: 0, MAX: 99},
            {ID: 'PSD', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'LOC', MIN: 0, MAX: 99},
                {ID: 'TEM', MIN: 0, MAX: 999, LEVEL: [
                    {ID: 'MEA', MIN: 0, MAX: 99},
                    {ID: 'PCD', MIN: 0, MAX: 99},
                    {ID: 'DTM', MIN: 0, MAX: 99},
                    {ID: 'FTX', MIN: 0, MAX: 99},
                ]},
            ]},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

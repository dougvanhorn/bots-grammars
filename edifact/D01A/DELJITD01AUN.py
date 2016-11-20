#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD01AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 10},
    {ID: 'FTX', MIN: 0, MAX: 5},
    {ID: 'RFF', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'NAD', MIN: 0, MAX: 20, LEVEL: [
        {ID: 'LOC', MIN: 0, MAX: 10},
        {ID: 'FTX', MIN: 0, MAX: 5},
        {ID: 'CTA', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'SEQ', MIN: 1, MAX: 9999, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 5},
        {ID: 'GIR', MIN: 0, MAX: 99},
        {ID: 'LOC', MIN: 0, MAX: 5},
        {ID: 'PAC', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'PCI', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'GIN', MIN: 0, MAX: 10},
            ]},
        ]},
        {ID: 'LIN', MIN: 0, MAX: 9999, LEVEL: [
            {ID: 'PIA', MIN: 0, MAX: 10},
            {ID: 'IMD', MIN: 0, MAX: 10},
            {ID: 'ALI', MIN: 0, MAX: 5},
            {ID: 'GIR', MIN: 0, MAX: 5},
            {ID: 'FTX', MIN: 0, MAX: 5},
            {ID: 'PAC', MIN: 0, MAX: 5},
            {ID: 'DTM', MIN: 0, MAX: 5},
            {ID: 'RFF', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 1},
            ]},
            {ID: 'TDT', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'TMD', MIN: 0, MAX: 1},
            ]},
            {ID: 'LOC', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'CTA', MIN: 0, MAX: 5, LEVEL: [
                    {ID: 'COM', MIN: 0, MAX: 5},
                ]},
            ]},
            {ID: 'QTY', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'SCC', MIN: 0, MAX: 1},
                {ID: 'DTM', MIN: 0, MAX: 2},
                {ID: 'RFF', MIN: 0, MAX: 5, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 1},
                ]},
            ]},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

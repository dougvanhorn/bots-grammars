#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD97BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 35},
    {ID: 'PAI', MIN: 0, MAX: 1},
    {ID: 'ALI', MIN: 0, MAX: 5},
    {ID: 'IMD', MIN: 0, MAX: 999},
    {ID: 'IRQ', MIN: 0, MAX: 10},
    {ID: 'FTX', MIN: 0, MAX: 99},
    {ID: 'RFF', MIN: 0, MAX: 9999, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 5},
    ]},
    {ID: 'AJT', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'FTX', MIN: 0, MAX: 5},
    ]},
    {ID: 'TAX', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'MOA', MIN: 0, MAX: 1},
        {ID: 'LOC', MIN: 0, MAX: 5},
    ]},
    {ID: 'CUX', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 5},
    ]},
    {ID: 'PAT', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 5},
        {ID: 'PCD', MIN: 0, MAX: 1},
        {ID: 'MOA', MIN: 0, MAX: 1},
    ]},
    {ID: 'TOD', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'LOC', MIN: 0, MAX: 2},
    ]},
    {ID: 'EQD', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'HAN', MIN: 0, MAX: 5},
        {ID: 'MEA', MIN: 0, MAX: 5},
        {ID: 'FTX', MIN: 0, MAX: 5},
    ]},
    {ID: 'RCS', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 5},
        {ID: 'DTM', MIN: 0, MAX: 5},
        {ID: 'FTX', MIN: 0, MAX: 99999},
    ]},
    {ID: 'APR', MIN: 0, MAX: 25, LEVEL: [
        {ID: 'PRI', MIN: 0, MAX: 1},
        {ID: 'QTY', MIN: 0, MAX: 2},
        {ID: 'DTM', MIN: 0, MAX: 1},
        {ID: 'MOA', MIN: 0, MAX: 2},
        {ID: 'RNG', MIN: 0, MAX: 2},
    ]},
    {ID: 'DLM', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'MOA', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'NAD', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'LOC', MIN: 0, MAX: 25},
        {ID: 'FII', MIN: 0, MAX: 5},
        {ID: 'RFF', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 5},
        ]},
        {ID: 'DOC', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
        ]},
        {ID: 'CTA', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'TDT', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'QTY', MIN: 0, MAX: 5},
        {ID: 'LOC', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'PAC', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'MEA', MIN: 0, MAX: 5},
        {ID: 'PCI', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'RFF', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 5},
            {ID: 'GIN', MIN: 0, MAX: 10},
        ]},
    ]},
    {ID: 'SCC', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'FTX', MIN: 0, MAX: 5},
        {ID: 'QTY', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'ALC', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'ALI', MIN: 0, MAX: 5},
        {ID: 'QTY', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'RNG', MIN: 0, MAX: 1},
        ]},
        {ID: 'PCD', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'RNG', MIN: 0, MAX: 1},
        ]},
        {ID: 'MOA', MIN: 0, MAX: 2, LEVEL: [
            {ID: 'RNG', MIN: 0, MAX: 1},
        ]},
        {ID: 'RTE', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'RNG', MIN: 0, MAX: 1},
        ]},
        {ID: 'TAX', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'MOA', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'LIN', MIN: 1, MAX: 200000, LEVEL: [
        {ID: 'PIA', MIN: 0, MAX: 25},
        {ID: 'IMD', MIN: 0, MAX: 99},
        {ID: 'MEA', MIN: 0, MAX: 5},
        {ID: 'QTY', MIN: 0, MAX: 99},
        {ID: 'PCD', MIN: 0, MAX: 1},
        {ID: 'ALI', MIN: 0, MAX: 5},
        {ID: 'DTM', MIN: 0, MAX: 35},
        {ID: 'GIN', MIN: 0, MAX: 1000},
        {ID: 'GIR', MIN: 0, MAX: 1000},
        {ID: 'QVR', MIN: 0, MAX: 1},
        {ID: 'FTX', MIN: 0, MAX: 99},
        {ID: 'PAI', MIN: 0, MAX: 1},
        {ID: 'DOC', MIN: 0, MAX: 99},
        {ID: 'CCI', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'CAV', MIN: 0, MAX: 10},
            {ID: 'MEA', MIN: 0, MAX: 10},
        ]},
        {ID: 'MOA', MIN: 0, MAX: 100, LEVEL: [
            {ID: 'QTY', MIN: 0, MAX: 2},
            {ID: 'IMD', MIN: 0, MAX: 1},
            {ID: 'CUX', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 2},
        ]},
        {ID: 'AJT', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 5},
        ]},
        {ID: 'PRI', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'APR', MIN: 0, MAX: 1},
            {ID: 'RNG', MIN: 0, MAX: 1},
            {ID: 'CUX', MIN: 0, MAX: 5},
            {ID: 'DTM', MIN: 0, MAX: 5},
        ]},
        {ID: 'RFF', MIN: 0, MAX: 9999, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 5},
        ]},
        {ID: 'LOC', MIN: 0, MAX: 100, LEVEL: [
            {ID: 'QTY', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 5},
        ]},
        {ID: 'TAX', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'MOA', MIN: 0, MAX: 1},
            {ID: 'LOC', MIN: 0, MAX: 5},
        ]},
        {ID: 'TOD', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'LOC', MIN: 0, MAX: 2},
        ]},
        {ID: 'EQD', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'HAN', MIN: 0, MAX: 5},
            {ID: 'MEA', MIN: 0, MAX: 5},
            {ID: 'FTX', MIN: 0, MAX: 5},
        ]},
        {ID: 'RCS', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'RFF', MIN: 0, MAX: 5},
            {ID: 'DTM', MIN: 0, MAX: 5},
            {ID: 'FTX', MIN: 0, MAX: 99999},
        ]},
        {ID: 'PAT', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 5},
            {ID: 'PCD', MIN: 0, MAX: 1},
            {ID: 'MOA', MIN: 0, MAX: 1},
        ]},
        {ID: 'PAC', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'MEA', MIN: 0, MAX: 5},
            {ID: 'QTY', MIN: 0, MAX: 5},
            {ID: 'DTM', MIN: 0, MAX: 5},
            {ID: 'RFF', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 5},
            ]},
            {ID: 'PCI', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'RFF', MIN: 0, MAX: 1},
                {ID: 'DTM', MIN: 0, MAX: 5},
                {ID: 'GIN', MIN: 0, MAX: 10},
            ]},
        ]},
        {ID: 'NAD', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'LOC', MIN: 0, MAX: 5},
            {ID: 'RFF', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 5},
            ]},
            {ID: 'DOC', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 5},
            ]},
            {ID: 'CTA', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'COM', MIN: 0, MAX: 5},
            ]},
        ]},
        {ID: 'ALC', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'ALI', MIN: 0, MAX: 5},
            {ID: 'QTY', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'RNG', MIN: 0, MAX: 1},
            ]},
            {ID: 'PCD', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'RNG', MIN: 0, MAX: 1},
            ]},
            {ID: 'MOA', MIN: 0, MAX: 2, LEVEL: [
                {ID: 'RNG', MIN: 0, MAX: 1},
            ]},
            {ID: 'RTE', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'RNG', MIN: 0, MAX: 1},
            ]},
            {ID: 'TAX', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'MOA', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'TDT', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'QTY', MIN: 0, MAX: 5},
            {ID: 'LOC', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 5},
            ]},
        ]},
        {ID: 'SCC', MIN: 0, MAX: 100, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 5},
            {ID: 'QTY', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 5},
            ]},
        ]},
    ]},
    {ID: 'UNS', MIN: 1, MAX: 1},
    {ID: 'MOA', MIN: 0, MAX: 15},
    {ID: 'CNT', MIN: 0, MAX: 10},
    {ID: 'ALC', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'MOA', MIN: 1, MAX: 1},
        {ID: 'ALI', MIN: 0, MAX: 1},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD98BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'CST', MIN: 0, MAX: 1},
    {ID: 'LOC', MIN: 0, MAX: 99},
    {ID: 'DTM', MIN: 0, MAX: 15},
    {ID: 'GIS', MIN: 0, MAX: 25},
    {ID: 'FII', MIN: 0, MAX: 1},
    {ID: 'MEA', MIN: 0, MAX: 5},
    {ID: 'EQD', MIN: 0, MAX: 999},
    {ID: 'SEL', MIN: 0, MAX: 999},
    {ID: 'FTX', MIN: 0, MAX: 99},
    {ID: 'RFF', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
        {ID: 'PAC', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'PCI', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'FTX', MIN: 0, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'TDT', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'TPL', MIN: 0, MAX: 1},
    ]},
    {ID: 'DOC', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 2},
        {ID: 'LOC', MIN: 0, MAX: 1},
    ]},
    {ID: 'NAD', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 10},
        {ID: 'CTA', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 5},
    ]},
    {ID: 'TOD', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'LOC', MIN: 0, MAX: 2},
        {ID: 'FTX', MIN: 0, MAX: 1},
    ]},
    {ID: 'MOA', MIN: 0, MAX: 25, LEVEL: [
        {ID: 'CUX', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'UNS', MIN: 1, MAX: 1},
    {ID: 'DMS', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
        {ID: 'MEA', MIN: 0, MAX: 5},
        {ID: 'MOA', MIN: 0, MAX: 25, LEVEL: [
            {ID: 'CUX', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'TOD', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'LOC', MIN: 0, MAX: 2},
            {ID: 'FTX', MIN: 0, MAX: 1},
        ]},
        {ID: 'NAD', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'DOC', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 2},
                {ID: 'LOC', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'PAC', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'PCI', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'FTX', MIN: 0, MAX: 1},
                {ID: 'RFF', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'PAT', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'MOA', MIN: 0, MAX: 1},
            {ID: 'PCD', MIN: 0, MAX: 1},
            {ID: 'FTX', MIN: 0, MAX: 1},
        ]},
        {ID: 'ALC', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'RTE', MIN: 0, MAX: 1},
            {ID: 'MOA', MIN: 0, MAX: 1},
            {ID: 'PCD', MIN: 0, MAX: 1},
            {ID: 'QTY', MIN: 0, MAX: 1},
            {ID: 'CUX', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'LIN', MIN: 0, MAX: 9999, LEVEL: [
            {ID: 'PIA', MIN: 0, MAX: 1},
            {ID: 'QTY', MIN: 0, MAX: 1},
            {ID: 'PRI', MIN: 0, MAX: 2},
            {ID: 'PCD', MIN: 0, MAX: 1},
            {ID: 'MEA', MIN: 0, MAX: 5},
            {ID: 'QVR', MIN: 0, MAX: 5},
            {ID: 'MOA', MIN: 0, MAX: 15},
            {ID: 'NAD', MIN: 0, MAX: 10},
            {ID: 'GIR', MIN: 0, MAX: 9999},
            {ID: 'DOC', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 2},
            ]},
            {ID: 'ALC', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'RTE', MIN: 0, MAX: 1},
                {ID: 'MOA', MIN: 0, MAX: 1},
                {ID: 'PCD', MIN: 0, MAX: 1},
                {ID: 'QTY', MIN: 0, MAX: 1},
                {ID: 'CUX', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 1},
                ]},
            ]},
            {ID: 'TOD', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'LOC', MIN: 0, MAX: 2},
            ]},
            {ID: 'PAT', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'MOA', MIN: 0, MAX: 1},
                {ID: 'PCD', MIN: 0, MAX: 1},
                {ID: 'FTX', MIN: 0, MAX: 1},
            ]},
            {ID: 'IMD', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'FTX', MIN: 0, MAX: 1},
            ]},
            {ID: 'PAC', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'PCI', MIN: 0, MAX: 999, LEVEL: [
                    {ID: 'FTX', MIN: 0, MAX: 1},
                    {ID: 'RFF', MIN: 0, MAX: 1},
                ]},
            ]},
        ]},
    ]},
    {ID: 'CST', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'LOC', MIN: 0, MAX: 25},
        {ID: 'DTM', MIN: 0, MAX: 5},
        {ID: 'MEA', MIN: 0, MAX: 20},
        {ID: 'NAD', MIN: 0, MAX: 5},
        {ID: 'TDT', MIN: 0, MAX: 9},
        {ID: 'PAC', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'PCI', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'FTX', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'MOA', MIN: 0, MAX: 25, LEVEL: [
            {ID: 'CUX', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'RFF', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
            {ID: 'GIN', MIN: 0, MAX: 99},
            {ID: 'MOA', MIN: 0, MAX: 1},
            {ID: 'IMD', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'FTX', MIN: 0, MAX: 5},
            ]},
        ]},
        {ID: 'DOC', MIN: 0, MAX: 25, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 2},
            {ID: 'LOC', MIN: 0, MAX: 1},
            {ID: 'NAD', MIN: 0, MAX: 5},
        ]},
        {ID: 'TOD', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'LOC', MIN: 0, MAX: 2},
            {ID: 'FTX', MIN: 0, MAX: 1},
        ]},
        {ID: 'GDS', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 1},
        ]},
        {ID: 'GIS', MIN: 0, MAX: 25, LEVEL: [
            {ID: 'PCD', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 1},
            {ID: 'RFF', MIN: 0, MAX: 1},
        ]},
        {ID: 'TAX', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'MOA', MIN: 0, MAX: 2},
            {ID: 'GIS', MIN: 0, MAX: 1},
        ]},
        {ID: 'QVR', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'QTY', MIN: 0, MAX: 1},
            {ID: 'RFF', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'GIR', MIN: 0, MAX: 50, LEVEL: [
            {ID: 'GIS', MIN: 0, MAX: 10},
            {ID: 'NAD', MIN: 0, MAX: 1},
            {ID: 'MEA', MIN: 0, MAX: 5},
            {ID: 'MOA', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'CUX', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 1},
                ]},
            ]},
            {ID: 'TAX', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'MOA', MIN: 0, MAX: 2},
                {ID: 'GIS', MIN: 0, MAX: 1},
            ]},
            {ID: 'DOC', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 2},
                {ID: 'LOC', MIN: 0, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'UNS', MIN: 1, MAX: 1},
    {ID: 'CNT', MIN: 0, MAX: 5},
    {ID: 'TAX', MIN: 0, MAX: 50, LEVEL: [
        {ID: 'MOA', MIN: 0, MAX: 2},
        {ID: 'GIS', MIN: 0, MAX: 1},
    ]},
    {ID: 'AUT', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

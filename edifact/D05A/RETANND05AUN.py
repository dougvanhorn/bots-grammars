#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD05AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 9},
    {ID: 'FTX', MIN: 0, MAX: 9},
    {ID: 'CUX', MIN: 0, MAX: 9},
    {ID: 'DOC', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'NAD', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'LOC', MIN: 0, MAX: 999},
        {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
        ]},
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'TOD', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'LOC', MIN: 0, MAX: 9},
    ]},
    {ID: 'TDT', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'LOC', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'EQD', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'MEA', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
    ]},
    {ID: 'ALC', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'ALI', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'MOA', MIN: 0, MAX: 9},
        {ID: 'TAX', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'MOA', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'LIN', MIN: 1, MAX: 9999, LEVEL: [
        {ID: 'PIA', MIN: 0, MAX: 9},
        {ID: 'IMD', MIN: 0, MAX: 9},
        {ID: 'MEA', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'PRI', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'LOC', MIN: 0, MAX: 9},
        {ID: 'MOA', MIN: 0, MAX: 9},
        {ID: 'TAX', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'MOA', MIN: 0, MAX: 9},
        ]},
        {ID: 'QTY', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'CDI', MIN: 0, MAX: 9},
        ]},
        {ID: 'DOC', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
        ]},
        {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
        ]},
        {ID: 'DGS', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'QTY', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 9},
        ]},
        {ID: 'HAN', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 9},
        ]},
        {ID: 'PAC', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'PCI', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'GIN', MIN: 0, MAX: 9},
            ]},
        ]},
        {ID: 'TDT', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'LOC', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9},
        ]},
        {ID: 'EQD', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'MEA', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 9},
        ]},
        {ID: 'ALC', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'ALI', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'MOA', MIN: 0, MAX: 9},
            {ID: 'PCD', MIN: 0, MAX: 9},
            {ID: 'TAX', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'MOA', MIN: 0, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'UNS', MIN: 1, MAX: 1},
    {ID: 'CNT', MIN: 0, MAX: 9},
    {ID: 'MOA', MIN: 0, MAX: 9},
    {ID: 'TAX', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'MOA', MIN: 0, MAX: 9},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

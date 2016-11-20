#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD11AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'RFF', MIN: 0, MAX: 9},
    {ID: 'SEQ', MIN: 0, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 9},
    {ID: 'EFI', MIN: 0, MAX: 9},
    {ID: 'ICD', MIN: 1, MAX: 1, LEVEL: [
        {ID: 'MOA', MIN: 0, MAX: 9},
        {ID: 'ATT', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'QRS', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
    ]},
    {ID: 'PNA', MIN: 1, MAX: 9, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 99},
        {ID: 'EMP', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'PCD', MIN: 0, MAX: 9},
        {ID: 'QRS', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 9},
        {ID: 'ATT', MIN: 0, MAX: 9},
        {ID: 'ADR', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
        {ID: 'ROD', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'MOA', MIN: 1, MAX: 1},
            {ID: 'FTX', MIN: 0, MAX: 1},
        ]},
        {ID: 'COD', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'ATT', MIN: 0, MAX: 9},
            {ID: 'IDE', MIN: 0, MAX: 1},
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'MOA', MIN: 0, MAX: 9},
            {ID: 'EQN', MIN: 0, MAX: 9},
            {ID: 'QRS', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'UNS', MIN: 1, MAX: 1},
    {ID: 'EVE', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'ADR', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'QRS', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'ATT', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'MOA', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'PYT', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'MOA', MIN: 1, MAX: 9},
        {ID: 'PNA', MIN: 0, MAX: 1},
        {ID: 'FII', MIN: 0, MAX: 1},
        {ID: 'ATT', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9},
    ]},
    {ID: 'COD', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'ATT', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'ADR', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'QRS', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'IMD', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'ATT', MIN: 0, MAX: 9},
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'MOA', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

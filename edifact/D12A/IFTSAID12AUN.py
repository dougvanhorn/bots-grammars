#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD12AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 9},
    {ID: 'FTX', MIN: 0, MAX: 99},
    {ID: 'GEI', MIN: 0, MAX: 1},
    {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'LOC', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'EQD', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'EQN', MIN: 0, MAX: 9},
        {ID: 'MEA', MIN: 0, MAX: 9},
        {ID: 'DIM', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'TPL', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'TDT', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'TSR', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'EQD', MIN: 0, MAX: 99},
        {ID: 'QTY', MIN: 0, MAX: 9},
        {ID: 'MEA', MIN: 0, MAX: 9},
        {ID: 'LOC', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'FTX', MIN: 0, MAX: 9},
            ]},
            {ID: 'EQD', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'EQN', MIN: 0, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'NAD', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'LOC', MIN: 0, MAX: 9},
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'GID', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'HAN', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'GDS', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 9},
        ]},
        {ID: 'MEA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'EQN', MIN: 0, MAX: 9},
        ]},
        {ID: 'DIM', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'EQN', MIN: 0, MAX: 9},
        ]},
        {ID: 'DGS', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

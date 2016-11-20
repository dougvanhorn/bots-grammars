#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD00AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'CTA', MIN: 0, MAX: 1},
    {ID: 'COM', MIN: 0, MAX: 9},
    {ID: 'DTM', MIN: 0, MAX: 9},
    {ID: 'TSR', MIN: 0, MAX: 9},
    {ID: 'FTX', MIN: 0, MAX: 99},
    {ID: 'CNT', MIN: 0, MAX: 9},
    {ID: 'GDS', MIN: 0, MAX: 9},
    {ID: 'LOC', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'RFF', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'GOR', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'DOC', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'TDT', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'TSR', MIN: 0, MAX: 9},
        {ID: 'LOC', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
        ]},
        {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'NAD', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'LOC', MIN: 0, MAX: 9},
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
        {ID: 'DOC', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
        ]},
        {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
        ]},
        {ID: 'CPI', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'RFF', MIN: 0, MAX: 99},
            {ID: 'CUX', MIN: 0, MAX: 1},
            {ID: 'LOC', MIN: 0, MAX: 9},
            {ID: 'MOA', MIN: 0, MAX: 9},
        ]},
        {ID: 'TSR', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'RFF', MIN: 0, MAX: 1},
            {ID: 'LOC', MIN: 0, MAX: 1},
            {ID: 'TPL', MIN: 0, MAX: 1},
            {ID: 'FTX', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'GID', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'HAN', MIN: 0, MAX: 1},
        {ID: 'TMP', MIN: 0, MAX: 1},
        {ID: 'RNG', MIN: 0, MAX: 1},
        {ID: 'TMD', MIN: 0, MAX: 1},
        {ID: 'LOC', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'NAD', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
        ]},
        {ID: 'GDS', MIN: 0, MAX: 9},
        {ID: 'MEA', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'EQN', MIN: 0, MAX: 1},
        ]},
        {ID: 'DIM', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'EQN', MIN: 0, MAX: 1},
        ]},
        {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
        ]},
        {ID: 'DOC', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
        ]},
        {ID: 'TPL', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'MEA', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'EQN', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'SGP', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'MEA', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'EQN', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'DGS', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 99},
            {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'COM', MIN: 0, MAX: 9},
            ]},
            {ID: 'MEA', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'EQN', MIN: 0, MAX: 1},
            ]},
            {ID: 'SGP', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'MEA', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'EQN', MIN: 0, MAX: 1},
                ]},
            ]},
        ]},
    ]},
    {ID: 'EQD', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'EQN', MIN: 0, MAX: 1},
        {ID: 'TMD', MIN: 0, MAX: 1},
        {ID: 'MEA', MIN: 0, MAX: 9},
        {ID: 'DIM', MIN: 0, MAX: 9},
        {ID: 'TPL', MIN: 0, MAX: 9},
        {ID: 'HAN', MIN: 0, MAX: 1},
        {ID: 'TMP', MIN: 0, MAX: 1},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'NAD', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
            {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'COM', MIN: 0, MAX: 9},
            ]},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

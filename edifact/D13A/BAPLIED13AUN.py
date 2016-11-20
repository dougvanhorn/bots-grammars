#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD13AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 9},
    {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'NAD', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'TDT', MIN: 1, MAX: 9, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'LOC', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'UNS', MIN: 1, MAX: 1},
    {ID: 'LOC', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'EQD', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'NAD', MIN: 0, MAX: 9},
            {ID: 'MEA', MIN: 0, MAX: 9},
            {ID: 'HAN', MIN: 0, MAX: 99},
            {ID: 'DIM', MIN: 0, MAX: 9},
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'GDS', MIN: 0, MAX: 99},
            {ID: 'FTX', MIN: 0, MAX: 9},
            {ID: 'LOC', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'TSR', MIN: 0, MAX: 1},
                {ID: 'TDT', MIN: 0, MAX: 1},
            ]},
            {ID: 'TMP', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'RNG', MIN: 0, MAX: 1},
                {ID: 'DTM', MIN: 0, MAX: 1},
            ]},
            {ID: 'EQA', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'NAD', MIN: 0, MAX: 1},
            ]},
            {ID: 'DGS', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'ATT', MIN: 0, MAX: 9},
                {ID: 'MEA', MIN: 0, MAX: 9},
                {ID: 'FTX', MIN: 0, MAX: 9},
                {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'COM', MIN: 0, MAX: 9},
                ]},
            ]},
        ]},
        {ID: 'CNT', MIN: 1, MAX: 1},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

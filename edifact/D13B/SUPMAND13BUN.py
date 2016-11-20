#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD13BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'RFF', MIN: 1, MAX: 6},
    {ID: 'CUX', MIN: 0, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 9},
    {ID: 'FTX', MIN: 0, MAX: 5},
    {ID: 'NAD', MIN: 0, MAX: 6, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'UNS', MIN: 1, MAX: 1},
    {ID: 'NAD', MIN: 1, MAX: 999999, LEVEL: [
        {ID: 'DTM', MIN: 1, MAX: 15},
        {ID: 'ATT', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'REL', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'NAD', MIN: 1, MAX: 1},
            {ID: 'PCD', MIN: 0, MAX: 1},
        ]},
        {ID: 'EMP', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'PCD', MIN: 0, MAX: 1},
            {ID: 'CUX', MIN: 0, MAX: 1},
            {ID: 'NAD', MIN: 0, MAX: 9},
            {ID: 'MOA', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'PYT', MIN: 0, MAX: 1},
                {ID: 'DTM', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'GEI', MIN: 1, MAX: 20, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
        ]},
        {ID: 'MEM', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'ATT', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'PCD', MIN: 0, MAX: 1},
            ]},
            {ID: 'COT', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'MOA', MIN: 0, MAX: 1},
                {ID: 'PCD', MIN: 0, MAX: 1},
                {ID: 'DTM', MIN: 0, MAX: 3},
                {ID: 'PYT', MIN: 0, MAX: 1},
                {ID: 'FTX', MIN: 0, MAX: 3},
            ]},
        ]},
    ]},
    {ID: 'CNT', MIN: 0, MAX: 9},
    {ID: 'AUT', MIN: 0, MAX: 1},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

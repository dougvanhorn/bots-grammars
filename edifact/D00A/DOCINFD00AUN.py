#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD00AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'RFF', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 3},
    {ID: 'BUS', MIN: 0, MAX: 1},
    {ID: 'INP', MIN: 0, MAX: 10},
    {ID: 'FCA', MIN: 0, MAX: 3},
    {ID: 'FTX', MIN: 0, MAX: 20},
    {ID: 'FII', MIN: 1, MAX: 9, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 2},
        {ID: 'CTA', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 5},
    ]},
    {ID: 'NAD', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 1},
        {ID: 'CTA', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 5},
    ]},
    {ID: 'DTM', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'LOC', MIN: 0, MAX: 1},
    ]},
    {ID: 'MOA', MIN: 1, MAX: 5, LEVEL: [
        {ID: 'ALC', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'PCD', MIN: 0, MAX: 2},
        ]},
    ]},
    {ID: 'LOC', MIN: 0, MAX: 3, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'PAI', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'FII', MIN: 0, MAX: 1},
        {ID: 'LOC', MIN: 0, MAX: 1},
    ]},
    {ID: 'PAT', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'FII', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 1},
        {ID: 'MOA', MIN: 0, MAX: 1},
        {ID: 'PCD', MIN: 0, MAX: 1},
        {ID: 'FTX', MIN: 0, MAX: 1},
    ]},
    {ID: 'TOD', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'LOC', MIN: 0, MAX: 1},
    ]},
    {ID: 'TSR', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'LOC', MIN: 0, MAX: 5},
    ]},
    {ID: 'INP', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'FTX', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 2},
    ]},
    {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
        {ID: 'FTX', MIN: 0, MAX: 2},
    ]},
    {ID: 'DOC', MIN: 0, MAX: 20, LEVEL: [
        {ID: 'MOA', MIN: 0, MAX: 1},
        {ID: 'PCD', MIN: 0, MAX: 1},
        {ID: 'LOC', MIN: 0, MAX: 1},
        {ID: 'FTX', MIN: 0, MAX: 1},
        {ID: 'ICD', MIN: 0, MAX: 20, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
            {ID: 'FTX', MIN: 0, MAX: 9},
        ]},
        {ID: 'ALI', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'NAD', MIN: 0, MAX: 3, LEVEL: [
                {ID: 'CTA', MIN: 0, MAX: 1},
                {ID: 'COM', MIN: 0, MAX: 5},
            ]},
        ]},
    ]},
    {ID: 'AUT', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

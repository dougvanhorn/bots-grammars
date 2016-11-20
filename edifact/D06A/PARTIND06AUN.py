#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD06AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 5},
    {ID: 'FII', MIN: 0, MAX: 10},
    {ID: 'FTX', MIN: 0, MAX: 5},
    {ID: 'RFF', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'NAD', MIN: 0, MAX: 2, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'UNS', MIN: 1, MAX: 1},
    {ID: 'NAD', MIN: 0, MAX: 200000, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 5},
        {ID: 'FII', MIN: 0, MAX: 10},
        {ID: 'IDE', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'TAX', MIN: 0, MAX: 9},
        {ID: 'HYN', MIN: 0, MAX: 9},
        {ID: 'LOC', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 2},
        ]},
        {ID: 'RFF', MIN: 0, MAX: 15, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
        ]},
        {ID: 'CTA', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 5},
        ]},
        {ID: 'SCC', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 2},
        ]},
        {ID: 'TOD', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'LOC', MIN: 0, MAX: 1},
        ]},
        {ID: 'PAI', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'PYT', MIN: 0, MAX: 1},
            {ID: 'CUX', MIN: 0, MAX: 2},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'PCD', MIN: 0, MAX: 9},
            {ID: 'MOA', MIN: 0, MAX: 9},
        ]},
        {ID: 'RCS', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'MOA', MIN: 0, MAX: 9},
            {ID: 'QTY', MIN: 0, MAX: 9},
        ]},
        {ID: 'CCI', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'MOA', MIN: 0, MAX: 9},
            {ID: 'QTY', MIN: 0, MAX: 9},
            {ID: 'CAV', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'MEA', MIN: 0, MAX: 9},
        ]},
        {ID: 'PRC', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'LIN', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'NAD', MIN: 1, MAX: 1},
                {ID: 'DOC', MIN: 1, MAX: 99, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 9},
                ]},
            ]},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

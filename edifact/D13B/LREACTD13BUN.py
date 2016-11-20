#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD13BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 1},
    {ID: 'CUX', MIN: 0, MAX: 1},
    {ID: 'CTA', MIN: 0, MAX: 9},
    {ID: 'FTX', MIN: 0, MAX: 1},
    {ID: 'GEI', MIN: 1, MAX: 999999, LEVEL: [
        {ID: 'RFF', MIN: 1, MAX: 9},
        {ID: 'ATT', MIN: 0, MAX: 99},
        {ID: 'DTM', MIN: 0, MAX: 99},
        {ID: 'FTX', MIN: 0, MAX: 1},
        {ID: 'IMD', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'LOC', MIN: 1, MAX: 9},
            {ID: 'SEQ', MIN: 0, MAX: 1},
            {ID: 'CUX', MIN: 0, MAX: 1},
            {ID: 'PNA', MIN: 0, MAX: 9},
        ]},
        {ID: 'PCD', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'PNA', MIN: 0, MAX: 1},
            {ID: 'LOC', MIN: 0, MAX: 1},
        ]},
        {ID: 'ICD', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'PCD', MIN: 1, MAX: 9},
            {ID: 'EMP', MIN: 0, MAX: 1},
            {ID: 'AGR', MIN: 0, MAX: 9},
            {ID: 'LOC', MIN: 0, MAX: 1},
            {ID: 'MOA', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'ARD', MIN: 1, MAX: 1},
            ]},
            {ID: 'RTE', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'ATT', MIN: 0, MAX: 1},
                {ID: 'DTM', MIN: 0, MAX: 1},
                {ID: 'MOA', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'ARD', MIN: 1, MAX: 1},
                ]},
            ]},
            {ID: 'PRC', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'ATT', MIN: 0, MAX: 9},
                {ID: 'PCD', MIN: 0, MAX: 1},
                {ID: 'MOA', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'ARD', MIN: 1, MAX: 1},
                ]},
            ]},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

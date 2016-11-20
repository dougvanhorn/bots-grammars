#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD05AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'ATT', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 9},
    {ID: 'PNA', MIN: 1, MAX: 9, LEVEL: [
        {ID: 'ADR', MIN: 0, MAX: 9},
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
            {ID: 'GEI', MIN: 0, MAX: 9},
            {ID: 'SEQ', MIN: 0, MAX: 1},
            {ID: 'ATT', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'ICD', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'MKS', MIN: 0, MAX: 9},
        {ID: 'PRC', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'GEI', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'ATT', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'MOA', MIN: 0, MAX: 1},
                {ID: 'PCD', MIN: 0, MAX: 1},
                {ID: 'RCS', MIN: 0, MAX: 9},
            ]},
            {ID: 'DOC', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'QRS', MIN: 0, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'RNG', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'GEI', MIN: 0, MAX: 9},
        {ID: 'MOA', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'MKS', MIN: 0, MAX: 9},
        {ID: 'ICD', MIN: 0, MAX: 9},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

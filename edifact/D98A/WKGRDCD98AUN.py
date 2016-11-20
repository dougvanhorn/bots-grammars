#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD98AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 2},
    {ID: 'PNA', MIN: 1, MAX: 3, LEVEL: [
        {ID: 'ADR', MIN: 0, MAX: 1},
        {ID: 'LOC', MIN: 0, MAX: 5},
        {ID: 'DTM', MIN: 0, MAX: 5},
        {ID: 'CTA', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'RFF', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 5},
    ]},
    {ID: 'GIS', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'FTX', MIN: 0, MAX: 1},
    ]},
    {ID: 'UNS', MIN: 1, MAX: 1},
    {ID: 'RFF', MIN: 1, MAX: 200, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 5},
        {ID: 'PNA', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'ADR', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 1},
            {ID: 'LOC', MIN: 0, MAX: 1},
            {ID: 'NAT', MIN: 0, MAX: 1},
            {ID: 'PDI', MIN: 0, MAX: 1},
            {ID: 'DOC', MIN: 0, MAX: 9},
        ]},
        {ID: 'FTX', MIN: 1, MAX: 99},
        {ID: 'GIS', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 1},
        ]},
        {ID: 'RFF', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 5},
        ]},
        {ID: 'RCS', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'RFF', MIN: 0, MAX: 5},
            {ID: 'DTM', MIN: 0, MAX: 5},
            {ID: 'FTX', MIN: 0, MAX: 5},
        ]},
        {ID: 'EMP', MIN: 1, MAX: 1, LEVEL: [
            {ID: 'LOC', MIN: 0, MAX: 10},
            {ID: 'ATT', MIN: 0, MAX: 20, LEVEL: [
                {ID: 'FTX', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'PNA', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'ADR', MIN: 0, MAX: 1},
            {ID: 'LOC', MIN: 0, MAX: 2},
            {ID: 'DTM', MIN: 0, MAX: 5},
            {ID: 'FTX', MIN: 0, MAX: 1},
            {ID: 'CTA', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'COM', MIN: 0, MAX: 5},
            ]},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

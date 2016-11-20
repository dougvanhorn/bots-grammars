#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD12AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 5},
    {ID: 'RFF', MIN: 0, MAX: 2},
    {ID: 'PNA', MIN: 1, MAX: 9, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'CTA', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 5},
        {ID: 'ADR', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'FTX', MIN: 1, MAX: 9},
        ]},
    ]},
    {ID: 'UNS', MIN: 1, MAX: 1},
    {ID: 'PNA', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'PDI', MIN: 0, MAX: 1},
        {ID: 'REL', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'NAT', MIN: 0, MAX: 1},
        {ID: 'LOC', MIN: 0, MAX: 1},
        {ID: 'FII', MIN: 0, MAX: 1},
        {ID: 'ATT', MIN: 0, MAX: 9},
        {ID: 'EMP', MIN: 0, MAX: 1},
        {ID: 'MOA', MIN: 0, MAX: 99},
        {ID: 'QTY', MIN: 0, MAX: 99},
        {ID: 'CTA', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 5},
        {ID: 'RFF', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
        ]},
        {ID: 'ADR', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 1},
        ]},
        {ID: 'PRC', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 99},
            {ID: 'ATT', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 99},
            {ID: 'EMP', MIN: 0, MAX: 9},
            {ID: 'ADR', MIN: 0, MAX: 9},
            {ID: 'DOC', MIN: 0, MAX: 9},
            {ID: 'IND', MIN: 0, MAX: 9},
            {ID: 'STS', MIN: 0, MAX: 9},
            {ID: 'LOC', MIN: 0, MAX: 9},
            {ID: 'QTY', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 1},
            ]},
            {ID: 'RFF', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 1},
                {ID: 'GEI', MIN: 0, MAX: 9},
            ]},
            {ID: 'MOA', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'RFF', MIN: 0, MAX: 9},
                {ID: 'DTM', MIN: 0, MAX: 9},
            ]},
            {ID: 'PCD', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'MOA', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 9},
                ]},
            ]},
        ]},
    ]},
    {ID: 'AUT', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

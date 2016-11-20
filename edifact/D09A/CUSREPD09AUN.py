#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD09AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 9},
    {ID: 'QTY', MIN: 0, MAX: 9},
    {ID: 'POC', MIN: 0, MAX: 99},
    {ID: 'FTX', MIN: 0, MAX: 9},
    {ID: 'MEA', MIN: 0, MAX: 9},
    {ID: 'GEI', MIN: 0, MAX: 9},
    {ID: 'GPO', MIN: 0, MAX: 1},
    {ID: 'STS', MIN: 0, MAX: 9},
    {ID: 'RFF', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'GDS', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'FTX', MIN: 0, MAX: 9},
    ]},
    {ID: 'LOC', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'DOC', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 1},
        {ID: 'LOC', MIN: 0, MAX: 1},
    ]},
    {ID: 'TAX', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'MOA', MIN: 0, MAX: 1},
        {ID: 'FII', MIN: 0, MAX: 1},
        {ID: 'LOC', MIN: 0, MAX: 1},
        {ID: 'RFF', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'GEI', MIN: 0, MAX: 1},
    ]},
    {ID: 'NAD', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 5},
        ]},
        {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'TDT', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'TPL', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 1},
        {ID: 'LOC', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'GPO', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'QTY', MIN: 0, MAX: 9},
            {ID: 'NAD', MIN: 0, MAX: 99},
            {ID: 'MEA', MIN: 0, MAX: 9},
            {ID: 'POC', MIN: 0, MAX: 9},
            {ID: 'STS', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'EQD', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'EQN', MIN: 0, MAX: 1},
    ]},
    {ID: 'AUT', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

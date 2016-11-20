#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD09AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 9},
    {ID: 'ALI', MIN: 0, MAX: 9},
    {ID: 'FTX', MIN: 0, MAX: 99},
    {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'NAD', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'FII', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 99},
        {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
        ]},
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'CUX', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'PYT', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'MOA', MIN: 0, MAX: 9},
        {ID: 'PCD', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'FII', MIN: 0, MAX: 1},
        {ID: 'PAI', MIN: 0, MAX: 9},
    ]},
    {ID: 'DOC', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'NAD', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'RFF', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 9},
            ]},
        ]},
        {ID: 'MOA', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'TAX', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'PAI', MIN: 0, MAX: 1},
            {ID: 'PYT', MIN: 0, MAX: 1},
            {ID: 'STS', MIN: 0, MAX: 9},
            {ID: 'AJT', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'MOA', MIN: 1, MAX: 1},
                {ID: 'RFF', MIN: 0, MAX: 1},
                {ID: 'FTX', MIN: 0, MAX: 9},
            ]},
        ]},
    ]},
    {ID: 'UNS', MIN: 1, MAX: 1},
    {ID: 'MOA', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'QTY', MIN: 0, MAX: 1},
        {ID: 'TAX', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'CNT', MIN: 0, MAX: 1},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

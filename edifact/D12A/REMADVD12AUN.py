#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD12AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 5},
    {ID: 'RFF', MIN: 0, MAX: 5},
    {ID: 'FII', MIN: 0, MAX: 5},
    {ID: 'PAI', MIN: 0, MAX: 1},
    {ID: 'FTX', MIN: 0, MAX: 99},
    {ID: 'GEI', MIN: 0, MAX: 5},
    {ID: 'NAD', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
        ]},
        {ID: 'CTA', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'CUX', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'DOC', MIN: 0, MAX: 999999, LEVEL: [
        {ID: 'MOA', MIN: 1, MAX: 5},
        {ID: 'DTM', MIN: 0, MAX: 5},
        {ID: 'RFF', MIN: 0, MAX: 5},
        {ID: 'NAD', MIN: 0, MAX: 2},
        {ID: 'CUX', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
        ]},
        {ID: 'AJT', MIN: 0, MAX: 100, LEVEL: [
            {ID: 'MOA', MIN: 0, MAX: 1},
            {ID: 'RFF', MIN: 0, MAX: 1},
            {ID: 'FTX', MIN: 0, MAX: 5},
            {ID: 'QTY', MIN: 0, MAX: 9},
            {ID: 'TAX', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'MOA', MIN: 0, MAX: 9},
            ]},
        ]},
        {ID: 'INP', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 5},
        ]},
        {ID: 'DLI', MIN: 0, MAX: 9999, LEVEL: [
            {ID: 'MOA', MIN: 0, MAX: 5},
            {ID: 'PIA', MIN: 0, MAX: 5},
            {ID: 'DTM', MIN: 0, MAX: 5},
            {ID: 'CUX', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 1},
            ]},
            {ID: 'AJT', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'MOA', MIN: 0, MAX: 1},
                {ID: 'RFF', MIN: 0, MAX: 1},
                {ID: 'FTX', MIN: 0, MAX: 5},
                {ID: 'TAX', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'MOA', MIN: 0, MAX: 9},
                ]},
            ]},
        ]},
    ]},
    {ID: 'UNS', MIN: 1, MAX: 1},
    {ID: 'MOA', MIN: 1, MAX: 99},
    {ID: 'ALC', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'MOA', MIN: 0, MAX: 9},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

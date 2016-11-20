#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD99AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'GIS', MIN: 1, MAX: 6},
    {ID: 'NAD', MIN: 1, MAX: 9, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 5},
        {ID: 'RFF', MIN: 0, MAX: 9},
    ]},
    {ID: 'DTM', MIN: 1, MAX: 6},
    {ID: 'FTX', MIN: 0, MAX: 6},
    {ID: 'ARD', MIN: 1, MAX: 999, LEVEL: [
        {ID: 'CUX', MIN: 1, MAX: 1},
        {ID: 'GIS', MIN: 0, MAX: 5},
        {ID: 'LOC', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 5},
        {ID: 'FTX', MIN: 0, MAX: 3},
        {ID: 'RFF', MIN: 1, MAX: 9},
        {ID: 'REL', MIN: 1, MAX: 999, LEVEL: [
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'GIS', MIN: 0, MAX: 7},
            {ID: 'LOC', MIN: 0, MAX: 9},
            {ID: 'NAD', MIN: 0, MAX: 7},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 6},
            {ID: 'PCD', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'NAD', MIN: 0, MAX: 1},
            ]},
            {ID: 'MOA', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'GIS', MIN: 0, MAX: 2},
                {ID: 'PCD', MIN: 0, MAX: 3},
                {ID: 'DTM', MIN: 0, MAX: 2},
                {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 3},
                    {ID: 'COM', MIN: 0, MAX: 1},
                ]},
                {ID: 'CUX', MIN: 0, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'UNS', MIN: 1, MAX: 1},
    {ID: 'MOA', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 3},
            {ID: 'COM', MIN: 0, MAX: 1},
        ]},
        {ID: 'PCD', MIN: 0, MAX: 3},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

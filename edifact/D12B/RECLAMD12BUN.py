#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD12BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'GEI', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'FTX', MIN: 0, MAX: 1},
    ]},
    {ID: 'NAD', MIN: 1, MAX: 999, LEVEL: [
        {ID: 'PCD', MIN: 0, MAX: 1},
        {ID: 'CTA', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 5},
        {ID: 'RFF', MIN: 0, MAX: 5},
        {ID: 'GEI', MIN: 0, MAX: 2},
        {ID: 'FTX', MIN: 0, MAX: 2},
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'UNS', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 8},
    {ID: 'FTX', MIN: 0, MAX: 999},
    {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 1},
        {ID: 'FTX', MIN: 0, MAX: 1},
    ]},
    {ID: 'LOC', MIN: 0, MAX: 1},
    {ID: 'MOA', MIN: 0, MAX: 1},
    {ID: 'PCD', MIN: 0, MAX: 1},
    {ID: 'GEI', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 8},
        {ID: 'LOC', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 1},
        {ID: 'FTX', MIN: 0, MAX: 3},
        {ID: 'PCD', MIN: 0, MAX: 2},
        {ID: 'CUX', MIN: 0, MAX: 3, LEVEL: [
            {ID: 'GEI', MIN: 0, MAX: 1},
            {ID: 'FTX', MIN: 0, MAX: 1},
            {ID: 'MOA', MIN: 1, MAX: 99, LEVEL: [
                {ID: 'GEI', MIN: 1, MAX: 3},
                {ID: 'CUX', MIN: 0, MAX: 1},
                {ID: 'FTX', MIN: 0, MAX: 2},
            ]},
            {ID: 'PCD', MIN: 1, MAX: 1},
        ]},
        {ID: 'NAD', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'PCD', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'UNS', MIN: 1, MAX: 1},
    {ID: 'CUX', MIN: 0, MAX: 3, LEVEL: [
        {ID: 'MOA', MIN: 1, MAX: 999, LEVEL: [
            {ID: 'PCD', MIN: 0, MAX: 2},
            {ID: 'CUX', MIN: 0, MAX: 1},
            {ID: 'FTX', MIN: 0, MAX: 10},
            {ID: 'RFF', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 1},
                {ID: 'COM', MIN: 0, MAX: 1},
                {ID: 'FTX', MIN: 0, MAX: 1},
            ]},
            {ID: 'GEI', MIN: 1, MAX: 99},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

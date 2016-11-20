#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD12BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 9},
    {ID: 'FTX', MIN: 0, MAX: 99},
    {ID: 'TDT', MIN: 0, MAX: 9},
    {ID: 'LOC', MIN: 0, MAX: 99},
    {ID: 'GEI', MIN: 0, MAX: 10},
    {ID: 'EQD', MIN: 0, MAX: 999},
    {ID: 'NAD', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'RFF', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'LOC', MIN: 0, MAX: 9},
    ]},
    {ID: 'ERP', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'ERC', MIN: 0, MAX: 99},
        {ID: 'FTX', MIN: 0, MAX: 99},
    ]},
    {ID: 'TAX', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'MOA', MIN: 0, MAX: 99},
        {ID: 'GEI', MIN: 0, MAX: 99},
    ]},
    {ID: 'DOC', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'PAC', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'PCI', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 99},
        {ID: 'TDT', MIN: 0, MAX: 9},
        {ID: 'LOC', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'GEI', MIN: 0, MAX: 99},
        {ID: 'MEA', MIN: 0, MAX: 99},
        {ID: 'EQD', MIN: 0, MAX: 999},
        {ID: 'NAD', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'COM', MIN: 0, MAX: 9},
            ]},
        ]},
        {ID: 'MOA', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'CUX', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'TAX', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'MOA', MIN: 0, MAX: 99},
            {ID: 'GEI', MIN: 0, MAX: 99},
        ]},
        {ID: 'CST', MIN: 0, MAX: 9999, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 9},
            {ID: 'TAX', MIN: 0, MAX: 999999, LEVEL: [
                {ID: 'MOA', MIN: 0, MAX: 99},
                {ID: 'GEI', MIN: 0, MAX: 99},
                {ID: 'MEA', MIN: 0, MAX: 9},
                {ID: 'RFF', MIN: 0, MAX: 9},
            ]},
        ]},
        {ID: 'ERP', MIN: 0, MAX: 9999, LEVEL: [
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'ERC', MIN: 0, MAX: 9999},
            {ID: 'FTX', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'CNT', MIN: 0, MAX: 9},
    {ID: 'AUT', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

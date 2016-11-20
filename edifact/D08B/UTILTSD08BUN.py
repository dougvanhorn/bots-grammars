#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD08BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 9},
    {ID: 'MKS', MIN: 0, MAX: 9},
    {ID: 'PRC', MIN: 0, MAX: 9},
    {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'NAD', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 1},
        {ID: 'ATT', MIN: 0, MAX: 9},
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'CUX', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'STS', MIN: 0, MAX: 9},
    ]},
    {ID: 'IDE', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'LOC', MIN: 0, MAX: 9},
        {ID: 'NAD', MIN: 0, MAX: 9},
        {ID: 'ALI', MIN: 0, MAX: 9},
        {ID: 'LIN', MIN: 0, MAX: 9},
        {ID: 'PIA', MIN: 0, MAX: 9},
        {ID: 'IMD', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'PRC', MIN: 0, MAX: 9},
        {ID: 'STS', MIN: 0, MAX: 9},
        {ID: 'AGR', MIN: 0, MAX: 9},
        {ID: 'MEA', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
        ]},
        {ID: 'CCI', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'CAV', MIN: 0, MAX: 99},
        ]},
        {ID: 'SEQ', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'MOA', MIN: 0, MAX: 9},
            {ID: 'PCD', MIN: 0, MAX: 9},
            {ID: 'GPO', MIN: 0, MAX: 9},
            {ID: 'CCI', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'CAV', MIN: 0, MAX: 99},
            ]},
            {ID: 'PRI', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'CUX', MIN: 0, MAX: 9},
            ]},
            {ID: 'QTY', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'STS', MIN: 0, MAX: 9},
                {ID: 'CCI', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'CAV', MIN: 0, MAX: 99},
                ]},
                {ID: 'PRI', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'CUX', MIN: 0, MAX: 9},
                ]},
            ]},
        ]},
    ]},
    {ID: 'CNT', MIN: 0, MAX: 9},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

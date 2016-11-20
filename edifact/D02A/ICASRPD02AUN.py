#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD02AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'ATT', MIN: 0, MAX: 9},
    {ID: 'CUX', MIN: 0, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 9},
    {ID: 'QRS', MIN: 0, MAX: 9},
    {ID: 'FTX', MIN: 0, MAX: 9},
    {ID: 'PNA', MIN: 1, MAX: 9, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'EVE', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'IDE', MIN: 0, MAX: 9},
        {ID: 'ATT', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'PCD', MIN: 0, MAX: 9},
        {ID: 'QRS', MIN: 0, MAX: 9},
        {ID: 'QTY', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'TCC', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'IDE', MIN: 0, MAX: 9},
            {ID: 'ATT', MIN: 0, MAX: 9},
            {ID: 'MOA', MIN: 0, MAX: 9},
            {ID: 'PCD', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 9},
            {ID: 'COT', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'IDE', MIN: 0, MAX: 9},
                {ID: 'ATT', MIN: 0, MAX: 9},
                {ID: 'MOA', MIN: 0, MAX: 9},
                {ID: 'PCD', MIN: 0, MAX: 9},
                {ID: 'RFF', MIN: 0, MAX: 9},
                {ID: 'FTX', MIN: 0, MAX: 9},
            ]},
        ]},
        {ID: 'COD', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'IDE', MIN: 0, MAX: 9},
            {ID: 'ADR', MIN: 0, MAX: 1},
            {ID: 'ATT', MIN: 0, MAX: 9},
            {ID: 'COM', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'MOA', MIN: 0, MAX: 9},
            {ID: 'PCD', MIN: 0, MAX: 9},
            {ID: 'QRS', MIN: 0, MAX: 9},
            {ID: 'QTY', MIN: 0, MAX: 9},
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 9},
            {ID: 'PCC', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'ATT', MIN: 0, MAX: 9},
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'MOA', MIN: 0, MAX: 9},
                {ID: 'PCD', MIN: 0, MAX: 9},
                {ID: 'QRS', MIN: 0, MAX: 9},
                {ID: 'QTY', MIN: 0, MAX: 9},
                {ID: 'FTX', MIN: 0, MAX: 9},
                {ID: 'TCC', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'IDE', MIN: 0, MAX: 9},
                    {ID: 'ATT', MIN: 0, MAX: 9},
                    {ID: 'MOA', MIN: 0, MAX: 9},
                    {ID: 'PCD', MIN: 0, MAX: 9},
                    {ID: 'FTX', MIN: 0, MAX: 9},
                    {ID: 'COT', MIN: 0, MAX: 99, LEVEL: [
                        {ID: 'IDE', MIN: 0, MAX: 9},
                        {ID: 'ATT', MIN: 0, MAX: 9},
                        {ID: 'MOA', MIN: 0, MAX: 9},
                        {ID: 'PCD', MIN: 0, MAX: 9},
                        {ID: 'RFF', MIN: 0, MAX: 9},
                        {ID: 'FTX', MIN: 0, MAX: 9},
                    ]},
                ]},
            ]},
        ]},
    ]},
    {ID: 'ICD', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'IDE', MIN: 0, MAX: 9},
        {ID: 'ATT', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'MOA', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'QRS', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
    ]},
    {ID: 'DOC', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'IDE', MIN: 0, MAX: 9},
        {ID: 'ATT', MIN: 0, MAX: 9},
        {ID: 'ADR', MIN: 0, MAX: 9},
        {ID: 'EFI', MIN: 0, MAX: 1},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'MOA', MIN: 0, MAX: 9},
        {ID: 'QRS', MIN: 0, MAX: 9},
        {ID: 'QTY', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
    ]},
    {ID: 'PNA', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'IDE', MIN: 0, MAX: 9},
        {ID: 'ATT', MIN: 0, MAX: 99},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'MEA', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'QRS', MIN: 0, MAX: 9},
        {ID: 'PCD', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'COD', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'IDE', MIN: 0, MAX: 9},
            {ID: 'ADR', MIN: 0, MAX: 1},
            {ID: 'FII', MIN: 0, MAX: 1},
            {ID: 'ATT', MIN: 0, MAX: 9},
            {ID: 'COM', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'EMP', MIN: 0, MAX: 9},
            {ID: 'MOA', MIN: 0, MAX: 9},
            {ID: 'QRS', MIN: 0, MAX: 9},
            {ID: 'QTY', MIN: 0, MAX: 9},
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'ROD', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'IDE', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'MOA', MIN: 0, MAX: 99},
        {ID: 'PCD', MIN: 0, MAX: 9},
        {ID: 'TAX', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 99},
        {ID: 'LOC', MIN: 0, MAX: 9},
        {ID: 'ATT', MIN: 0, MAX: 99},
        {ID: 'MEA', MIN: 0, MAX: 9},
        {ID: 'QTY', MIN: 0, MAX: 9},
        {ID: 'QRS', MIN: 0, MAX: 99},
        {ID: 'RTE', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'TCC', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'IDE', MIN: 0, MAX: 9},
            {ID: 'ATT', MIN: 0, MAX: 9},
            {ID: 'MOA', MIN: 0, MAX: 9},
            {ID: 'PCD', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 9},
            {ID: 'COT', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'IDE', MIN: 0, MAX: 9},
                {ID: 'ATT', MIN: 0, MAX: 9},
                {ID: 'MOA', MIN: 0, MAX: 9},
                {ID: 'PCD', MIN: 0, MAX: 9},
                {ID: 'RFF', MIN: 0, MAX: 9},
                {ID: 'FTX', MIN: 0, MAX: 9},
            ]},
        ]},
        {ID: 'COD', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'IDE', MIN: 0, MAX: 9},
            {ID: 'ADR', MIN: 0, MAX: 1},
            {ID: 'ATT', MIN: 0, MAX: 9},
            {ID: 'COM', MIN: 0, MAX: 9},
            {ID: 'DAM', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'MEA', MIN: 0, MAX: 9},
            {ID: 'MOA', MIN: 0, MAX: 9},
            {ID: 'PCD', MIN: 0, MAX: 9},
            {ID: 'QRS', MIN: 0, MAX: 9},
            {ID: 'QTY', MIN: 0, MAX: 9},
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 9},
            {ID: 'TCC', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'IDE', MIN: 0, MAX: 9},
                {ID: 'ATT', MIN: 0, MAX: 9},
                {ID: 'MOA', MIN: 0, MAX: 9},
                {ID: 'PCD', MIN: 0, MAX: 9},
                {ID: 'FTX', MIN: 0, MAX: 9},
                {ID: 'COT', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'IDE', MIN: 0, MAX: 9},
                    {ID: 'ATT', MIN: 0, MAX: 9},
                    {ID: 'MOA', MIN: 0, MAX: 9},
                    {ID: 'PCD', MIN: 0, MAX: 5},
                    {ID: 'RFF', MIN: 0, MAX: 9},
                    {ID: 'FTX', MIN: 0, MAX: 9},
                ]},
            ]},
            {ID: 'IMD', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'IDE', MIN: 0, MAX: 9},
                {ID: 'ATT', MIN: 0, MAX: 9},
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'MEA', MIN: 0, MAX: 9},
                {ID: 'PCD', MIN: 0, MAX: 9},
                {ID: 'QRS', MIN: 0, MAX: 9},
                {ID: 'QTY', MIN: 0, MAX: 9},
                {ID: 'RFF', MIN: 0, MAX: 9},
                {ID: 'FTX', MIN: 0, MAX: 9},
                {ID: 'TCC', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'IDE', MIN: 0, MAX: 9},
                    {ID: 'ATT', MIN: 0, MAX: 9},
                    {ID: 'MOA', MIN: 0, MAX: 9},
                    {ID: 'PCD', MIN: 0, MAX: 9},
                    {ID: 'FTX', MIN: 0, MAX: 9},
                    {ID: 'COT', MIN: 0, MAX: 99, LEVEL: [
                        {ID: 'IDE', MIN: 0, MAX: 9},
                        {ID: 'ATT', MIN: 0, MAX: 9},
                        {ID: 'MOA', MIN: 0, MAX: 9},
                        {ID: 'PCD', MIN: 0, MAX: 9},
                        {ID: 'RFF', MIN: 0, MAX: 9},
                        {ID: 'FTX', MIN: 0, MAX: 9},
                    ]},
                ]},
            ]},
        ]},
    ]},
    {ID: 'PRC', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'IDE', MIN: 0, MAX: 9},
        {ID: 'ATT', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 99},
        {ID: 'MOA', MIN: 0, MAX: 9},
        {ID: 'QRS', MIN: 0, MAX: 99},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
    ]},
    {ID: 'SEQ', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'IDE', MIN: 0, MAX: 9},
        {ID: 'ATT', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'COD', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'IDE', MIN: 0, MAX: 9},
            {ID: 'ATT', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'MOA', MIN: 0, MAX: 9},
            {ID: 'QRS', MIN: 0, MAX: 9},
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD00BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'GIS', MIN: 0, MAX: 1},
    {ID: 'ATT', MIN: 0, MAX: 9},
    {ID: 'CTA', MIN: 0, MAX: 1},
    {ID: 'RFF', MIN: 0, MAX: 99},
    {ID: 'QTY', MIN: 0, MAX: 1},
    {ID: 'SEQ', MIN: 0, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 9},
    {ID: 'PNA', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'QRS', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'ICD', MIN: 1, MAX: 9, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 99},
        {ID: 'ATT', MIN: 0, MAX: 9},
        {ID: 'PCD', MIN: 0, MAX: 9},
        {ID: 'MOA', MIN: 0, MAX: 9},
        {ID: 'QRS', MIN: 0, MAX: 99},
        {ID: 'QTY', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 99},
        {ID: 'DOC', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'ATT', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 1},
            {ID: 'PCC', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'GIS', MIN: 0, MAX: 1},
                {ID: 'MOA', MIN: 0, MAX: 9},
                {ID: 'PCD', MIN: 0, MAX: 9},
                {ID: 'QTY', MIN: 0, MAX: 9},
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'FTX', MIN: 0, MAX: 99},
                {ID: 'ATT', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'PCD', MIN: 0, MAX: 1},
                    {ID: 'MOA', MIN: 0, MAX: 9},
                    {ID: 'FTX', MIN: 0, MAX: 9},
                ]},
            ]},
        ]},
    ]},
    {ID: 'PNA', MIN: 1, MAX: 999, LEVEL: [
        {ID: 'GIS', MIN: 0, MAX: 1},
        {ID: 'ATT', MIN: 0, MAX: 9},
        {ID: 'PCD', MIN: 0, MAX: 1},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'EMP', MIN: 0, MAX: 99},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'MEM', MIN: 0, MAX: 9},
        {ID: 'QTY', MIN: 0, MAX: 9},
        {ID: 'REL', MIN: 0, MAX: 1},
        {ID: 'LOC', MIN: 0, MAX: 1},
        {ID: 'QRS', MIN: 0, MAX: 99},
        {ID: 'FTX', MIN: 0, MAX: 99},
        {ID: 'ADR', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
        ]},
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
        {ID: 'EVT', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'GIS', MIN: 0, MAX: 1},
            {ID: 'QRS', MIN: 0, MAX: 9},
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'ATT', MIN: 0, MAX: 9},
            {ID: 'ICD', MIN: 0, MAX: 9},
            {ID: 'MOA', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'QTY', MIN: 0, MAX: 9},
            {ID: 'PCD', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 99},
            {ID: 'PNA', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'ADR', MIN: 0, MAX: 1},
                {ID: 'RFF', MIN: 0, MAX: 9},
                {ID: 'CTA', MIN: 0, MAX: 1},
                {ID: 'COM', MIN: 0, MAX: 9},
            ]},
        ]},
        {ID: 'DOC', MIN: 1, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'ATT', MIN: 0, MAX: 9},
            {ID: 'LOC', MIN: 0, MAX: 1},
            {ID: 'FTX', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'PAT', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'ATT', MIN: 0, MAX: 9},
        {ID: 'FII', MIN: 0, MAX: 1},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'PCD', MIN: 0, MAX: 9},
        {ID: 'PNA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'ADR', MIN: 0, MAX: 1},
        ]},
        {ID: 'MOA', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 99},
            {ID: 'ATT', MIN: 0, MAX: 1},
            {ID: 'TAX', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'MOA', MIN: 0, MAX: 9},
                {ID: 'LOC', MIN: 0, MAX: 1},
                {ID: 'PCD', MIN: 1, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'ROD', MIN: 0, MAX: 9999, LEVEL: [
        {ID: 'GIS', MIN: 0, MAX: 1},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'ATT', MIN: 0, MAX: 99},
        {ID: 'QTY', MIN: 0, MAX: 99},
        {ID: 'MOA', MIN: 0, MAX: 9},
        {ID: 'MEA', MIN: 0, MAX: 9},
        {ID: 'ADR', MIN: 0, MAX: 99},
        {ID: 'PCD', MIN: 0, MAX: 9},
        {ID: 'QRS', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 99},
        {ID: 'PNA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'GIS', MIN: 0, MAX: 1},
            {ID: 'ADR', MIN: 0, MAX: 1},
            {ID: 'FTX', MIN: 0, MAX: 9},
        ]},
        {ID: 'EQD', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'GIS', MIN: 0, MAX: 1},
            {ID: 'ATT', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 1},
            {ID: 'PNA', MIN: 0, MAX: 9},
            {ID: 'QRS', MIN: 0, MAX: 9},
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 9},
        ]},
        {ID: 'DOC', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'ATT', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 99},
            {ID: 'PCD', MIN: 0, MAX: 1},
            {ID: 'FTX', MIN: 0, MAX: 9},
        ]},
        {ID: 'EVT', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'GIS', MIN: 0, MAX: 1},
            {ID: 'QRS', MIN: 0, MAX: 9},
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'ATT', MIN: 0, MAX: 9},
            {ID: 'ICD', MIN: 0, MAX: 1},
            {ID: 'MOA', MIN: 1, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'QTY', MIN: 0, MAX: 9},
            {ID: 'PCD', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 99},
            {ID: 'PNA', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'ADR', MIN: 0, MAX: 1},
                {ID: 'RFF', MIN: 0, MAX: 9},
                {ID: 'CTA', MIN: 0, MAX: 1},
                {ID: 'COM', MIN: 0, MAX: 9},
            ]},
        ]},
        {ID: 'ICD', MIN: 1, MAX: 99, LEVEL: [
            {ID: 'GIS', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'ATT', MIN: 0, MAX: 9},
            {ID: 'QRS', MIN: 0, MAX: 9},
            {ID: 'QTY', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 9},
            {ID: 'MOA', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'PCD', MIN: 0, MAX: 1},
                {ID: 'LOC', MIN: 0, MAX: 1},
            ]},
            {ID: 'ROD', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'GIS', MIN: 0, MAX: 1},
                {ID: 'MOA', MIN: 0, MAX: 9},
            ]},
            {ID: 'COD', MIN: 1, MAX: 1, LEVEL: [
                {ID: 'GIS', MIN: 0, MAX: 1},
                {ID: 'PCC', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'GIS', MIN: 0, MAX: 1},
                    {ID: 'MOA', MIN: 0, MAX: 9},
                    {ID: 'PCD', MIN: 0, MAX: 9},
                    {ID: 'QRS', MIN: 0, MAX: 9},
                    {ID: 'QTY', MIN: 0, MAX: 9},
                    {ID: 'DTM', MIN: 0, MAX: 9},
                    {ID: 'FTX', MIN: 0, MAX: 9},
                    {ID: 'PNA', MIN: 0, MAX: 99, LEVEL: [
                        {ID: 'ICD', MIN: 0, MAX: 9},
                    ]},
                    {ID: 'ATT', MIN: 1, MAX: 9, LEVEL: [
                        {ID: 'PCD', MIN: 0, MAX: 1},
                        {ID: 'MOA', MIN: 0, MAX: 9},
                        {ID: 'FTX', MIN: 0, MAX: 9},
                    ]},
                ]},
            ]},
            {ID: 'PNA', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'GIS', MIN: 0, MAX: 1},
                {ID: 'RFF', MIN: 0, MAX: 9},
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'MOA', MIN: 0, MAX: 9},
                {ID: 'PCD', MIN: 0, MAX: 9},
                {ID: 'QTY', MIN: 0, MAX: 9},
                {ID: 'QRS', MIN: 0, MAX: 9},
                {ID: 'REL', MIN: 0, MAX: 1},
            ]},
            {ID: 'EVT', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'GIS', MIN: 0, MAX: 1},
                {ID: 'ATT', MIN: 0, MAX: 9},
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'MOA', MIN: 0, MAX: 9},
                {ID: 'PCD', MIN: 0, MAX: 9},
                {ID: 'QRS', MIN: 0, MAX: 9},
                {ID: 'QTY', MIN: 0, MAX: 9},
                {ID: 'RFF', MIN: 0, MAX: 9},
                {ID: 'PCC', MIN: 0, MAX: 9},
                {ID: 'LOC', MIN: 0, MAX: 9},
                {ID: 'FTX', MIN: 0, MAX: 9},
                {ID: 'PNA', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'ADR', MIN: 0, MAX: 1},
                    {ID: 'RFF', MIN: 0, MAX: 9},
                    {ID: 'CTA', MIN: 0, MAX: 1},
                    {ID: 'COM', MIN: 0, MAX: 9},
                ]},
            ]},
        ]},
    ]},
    {ID: 'UNS', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'QRS', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'PNA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'ADR', MIN: 0, MAX: 1},
            {ID: 'CTA', MIN: 0, MAX: 1},
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
        {ID: 'GIS', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 1, MAX: 9},
            {ID: 'QTY', MIN: 1, MAX: 9},
            {ID: 'MOA', MIN: 0, MAX: 9},
            {ID: 'ICD', MIN: 1, MAX: 99, LEVEL: [
                {ID: 'ATT', MIN: 0, MAX: 9},
                {ID: 'MOA', MIN: 1, MAX: 9},
                {ID: 'QTY', MIN: 0, MAX: 9},
                {ID: 'FTX', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'EVT', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'GIS', MIN: 0, MAX: 1},
            {ID: 'ATT', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'ICD', MIN: 1, MAX: 1},
            {ID: 'MOA', MIN: 0, MAX: 9},
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'QRS', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD03BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'ATT', MIN: 0, MAX: 9},
    {ID: 'RFF', MIN: 0, MAX: 9},
    {ID: 'DTM', MIN: 0, MAX: 9},
    {ID: 'QTY', MIN: 0, MAX: 9},
    {ID: 'SEQ', MIN: 0, MAX: 1},
    {ID: 'PNA', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'ICD', MIN: 1, MAX: 999, LEVEL: [
        {ID: 'IDE', MIN: 1, MAX: 9},
        {ID: 'GEI', MIN: 0, MAX: 1},
        {ID: 'ATT', MIN: 0, MAX: 99},
        {ID: 'CUX', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 99},
        {ID: 'MOA', MIN: 0, MAX: 9},
        {ID: 'PCD', MIN: 0, MAX: 9},
        {ID: 'QTY', MIN: 0, MAX: 9},
        {ID: 'QRS', MIN: 0, MAX: 99},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 99},
        {ID: 'COD', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'IDE', MIN: 0, MAX: 99},
            {ID: 'GEI', MIN: 0, MAX: 1},
            {ID: 'ATT', MIN: 0, MAX: 99},
            {ID: 'COM', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 99},
            {ID: 'EFI', MIN: 0, MAX: 1},
            {ID: 'MOA', MIN: 0, MAX: 9},
            {ID: 'PCD', MIN: 0, MAX: 9},
            {ID: 'QRS', MIN: 0, MAX: 99},
            {ID: 'QTY', MIN: 0, MAX: 9},
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 9},
            {ID: 'PCC', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'IDE', MIN: 0, MAX: 9},
                {ID: 'ADR', MIN: 0, MAX: 99},
                {ID: 'ATT', MIN: 0, MAX: 9},
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'MOA', MIN: 0, MAX: 9},
                {ID: 'PCD', MIN: 0, MAX: 9},
                {ID: 'QRS', MIN: 0, MAX: 9},
                {ID: 'QTY', MIN: 0, MAX: 9},
                {ID: 'FTX', MIN: 0, MAX: 9},
            ]},
        ]},
    ]},
    {ID: 'PNA', MIN: 0, MAX: 9999, LEVEL: [
        {ID: 'IDE', MIN: 0, MAX: 99},
        {ID: 'GEI', MIN: 0, MAX: 1},
        {ID: 'ATT', MIN: 0, MAX: 99},
        {ID: 'COM', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'LOC', MIN: 0, MAX: 9},
        {ID: 'MOA', MIN: 0, MAX: 9},
        {ID: 'PCD', MIN: 0, MAX: 9},
        {ID: 'QRS', MIN: 0, MAX: 99},
        {ID: 'QTY', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 99},
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
        {ID: 'COD', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'IDE', MIN: 0, MAX: 9},
            {ID: 'GEI', MIN: 0, MAX: 1},
            {ID: 'ADR', MIN: 0, MAX: 9},
            {ID: 'ATT', MIN: 0, MAX: 9},
            {ID: 'COM', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'EFI', MIN: 0, MAX: 1},
            {ID: 'EMP', MIN: 0, MAX: 1},
            {ID: 'FII', MIN: 0, MAX: 1},
            {ID: 'IMD', MIN: 0, MAX: 9},
            {ID: 'MOA', MIN: 0, MAX: 9},
            {ID: 'PCD', MIN: 0, MAX: 9},
            {ID: 'QRS', MIN: 0, MAX: 99},
            {ID: 'QTY', MIN: 0, MAX: 9},
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 9},
            {ID: 'PCC', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'IDE', MIN: 0, MAX: 9},
                {ID: 'ADR', MIN: 0, MAX: 99},
                {ID: 'ATT', MIN: 0, MAX: 9},
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'MOA', MIN: 0, MAX: 9},
                {ID: 'PCD', MIN: 0, MAX: 9},
                {ID: 'QRS', MIN: 0, MAX: 9},
                {ID: 'QTY', MIN: 0, MAX: 9},
                {ID: 'FTX', MIN: 0, MAX: 9},
            ]},
        ]},
    ]},
    {ID: 'ROD', MIN: 0, MAX: 9999, LEVEL: [
        {ID: 'IDE', MIN: 0, MAX: 99},
        {ID: 'GEI', MIN: 0, MAX: 1},
        {ID: 'ATT', MIN: 0, MAX: 99},
        {ID: 'COM', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 99},
        {ID: 'MEA', MIN: 0, MAX: 99},
        {ID: 'MOA', MIN: 0, MAX: 9},
        {ID: 'PCD', MIN: 0, MAX: 9},
        {ID: 'QRS', MIN: 0, MAX: 99},
        {ID: 'QTY', MIN: 0, MAX: 99},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 99},
        {ID: 'COD', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'IDE', MIN: 0, MAX: 9},
            {ID: 'GEI', MIN: 0, MAX: 1},
            {ID: 'ADR', MIN: 0, MAX: 9},
            {ID: 'ATT', MIN: 0, MAX: 99},
            {ID: 'COM', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'EFI', MIN: 0, MAX: 1},
            {ID: 'EMP', MIN: 0, MAX: 9},
            {ID: 'IMD', MIN: 0, MAX: 9},
            {ID: 'MOA', MIN: 0, MAX: 9},
            {ID: 'MEA', MIN: 0, MAX: 9},
            {ID: 'PCD', MIN: 0, MAX: 9},
            {ID: 'QRS', MIN: 0, MAX: 99},
            {ID: 'QTY', MIN: 0, MAX: 9},
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 99},
            {ID: 'PCC', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'IDE', MIN: 0, MAX: 9},
                {ID: 'ADR', MIN: 0, MAX: 99},
                {ID: 'ATT', MIN: 0, MAX: 9},
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'MOA', MIN: 0, MAX: 9},
                {ID: 'PCD', MIN: 0, MAX: 9},
                {ID: 'QRS', MIN: 0, MAX: 9},
                {ID: 'QTY', MIN: 0, MAX: 9},
                {ID: 'FTX', MIN: 0, MAX: 9},
            ]},
        ]},
    ]},
    {ID: 'EVE', MIN: 0, MAX: 9999, LEVEL: [
        {ID: 'IDE', MIN: 0, MAX: 99},
        {ID: 'GEI', MIN: 0, MAX: 1},
        {ID: 'ATT', MIN: 0, MAX: 99},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'MEA', MIN: 0, MAX: 9},
        {ID: 'MOA', MIN: 0, MAX: 9},
        {ID: 'PCD', MIN: 0, MAX: 9},
        {ID: 'QRS', MIN: 0, MAX: 99},
        {ID: 'QTY', MIN: 0, MAX: 99},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 99},
        {ID: 'COD', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'IDE', MIN: 0, MAX: 99},
            {ID: 'GEI', MIN: 0, MAX: 1},
            {ID: 'ADR', MIN: 0, MAX: 9},
            {ID: 'ATT', MIN: 0, MAX: 99},
            {ID: 'COM', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'EFI', MIN: 0, MAX: 1},
            {ID: 'EMP', MIN: 0, MAX: 9},
            {ID: 'MOA', MIN: 0, MAX: 9},
            {ID: 'PCD', MIN: 0, MAX: 9},
            {ID: 'QRS', MIN: 0, MAX: 99},
            {ID: 'QTY', MIN: 0, MAX: 9},
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 99},
            {ID: 'PCC', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'IDE', MIN: 0, MAX: 9},
                {ID: 'ADR', MIN: 0, MAX: 99},
                {ID: 'ATT', MIN: 0, MAX: 9},
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'MOA', MIN: 0, MAX: 9},
                {ID: 'PCD', MIN: 0, MAX: 9},
                {ID: 'QRS', MIN: 0, MAX: 9},
                {ID: 'QTY', MIN: 0, MAX: 9},
                {ID: 'FTX', MIN: 0, MAX: 9},
            ]},
        ]},
    ]},
    {ID: 'SEQ', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'IDE', MIN: 0, MAX: 9},
        {ID: 'GEI', MIN: 0, MAX: 9},
        {ID: 'ATT', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'MOA', MIN: 0, MAX: 9},
        {ID: 'PCD', MIN: 0, MAX: 9},
        {ID: 'PNA', MIN: 0, MAX: 9},
        {ID: 'QRS', MIN: 0, MAX: 9},
        {ID: 'QTY', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'COD', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'IDE', MIN: 0, MAX: 99},
            {ID: 'GEI', MIN: 0, MAX: 9},
            {ID: 'ATT', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'MOA', MIN: 0, MAX: 9},
            {ID: 'PCD', MIN: 0, MAX: 9},
            {ID: 'PNA', MIN: 0, MAX: 9},
            {ID: 'QRS', MIN: 0, MAX: 9},
            {ID: 'QTY', MIN: 0, MAX: 9},
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 9},
            {ID: 'IMD', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'IDE', MIN: 0, MAX: 9},
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'PNA', MIN: 0, MAX: 9},
                {ID: 'QRS', MIN: 0, MAX: 9},
                {ID: 'RFF', MIN: 0, MAX: 9},
            ]},
        ]},
    ]},
    {ID: 'PYT', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'IDE', MIN: 0, MAX: 9},
        {ID: 'GEI', MIN: 0, MAX: 1},
        {ID: 'ATT', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'MOA', MIN: 0, MAX: 9},
        {ID: 'PCD', MIN: 0, MAX: 9},
        {ID: 'QRS', MIN: 0, MAX: 9},
        {ID: 'QTY', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'PCC', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'IDE', MIN: 0, MAX: 9},
            {ID: 'ADR', MIN: 0, MAX: 1},
            {ID: 'ATT', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'MOA', MIN: 1, MAX: 9},
            {ID: 'PCD', MIN: 0, MAX: 9},
            {ID: 'QRS', MIN: 0, MAX: 9},
            {ID: 'QTY', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

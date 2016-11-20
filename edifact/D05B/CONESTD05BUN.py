#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD05BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'RFF', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 1},
    {ID: 'AUT', MIN: 0, MAX: 2},
    {ID: 'AGR', MIN: 0, MAX: 2},
    {ID: 'IND', MIN: 0, MAX: 1000, LEVEL: [
        {ID: 'RCS', MIN: 1, MAX: 1},
        {ID: 'GEI', MIN: 1, MAX: 1, LEVEL: [
            {ID: 'BII', MIN: 1, MAX: 1, LEVEL: [
                {ID: 'IMD', MIN: 1, MAX: 9},
            ]},
        ]},
    ]},
    {ID: 'BII', MIN: 0, MAX: 1000, LEVEL: [
        {ID: 'RCS', MIN: 1, MAX: 1},
        {ID: 'GEI', MIN: 1, MAX: 10},
        {ID: 'NAD', MIN: 0, MAX: 1},
        {ID: 'LOC', MIN: 0, MAX: 1},
        {ID: 'APR', MIN: 0, MAX: 1},
        {ID: 'ALI', MIN: 0, MAX: 2},
        {ID: 'QTY', MIN: 0, MAX: 5},
        {ID: 'DTM', MIN: 0, MAX: 10},
        {ID: 'RTE', MIN: 0, MAX: 9},
        {ID: 'AGR', MIN: 0, MAX: 99},
        {ID: 'RFF', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 2},
            {ID: 'GEI', MIN: 0, MAX: 5},
            {ID: 'FTX', MIN: 0, MAX: 5},
        ]},
        {ID: 'CUX', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 5},
            {ID: 'FTX', MIN: 0, MAX: 1},
        ]},
        {ID: 'ALC', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'RFF', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 1},
            {ID: 'RNG', MIN: 0, MAX: 1},
            {ID: 'FTX', MIN: 0, MAX: 10},
            {ID: 'PCD', MIN: 0, MAX: 20, LEVEL: [
                {ID: 'RFF', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'RCS', MIN: 0, MAX: 100, LEVEL: [
            {ID: 'BII', MIN: 1, MAX: 1},
            {ID: 'FTX', MIN: 0, MAX: 9},
        ]},
        {ID: 'ARD', MIN: 1, MAX: 100, LEVEL: [
            {ID: 'MOA', MIN: 1, MAX: 6},
            {ID: 'FTX', MIN: 0, MAX: 10},
            {ID: 'TAX', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'MOA', MIN: 0, MAX: 1},
                {ID: 'LOC', MIN: 0, MAX: 5},
            ]},
            {ID: 'ALC', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'ALI', MIN: 0, MAX: 5},
                {ID: 'RFF', MIN: 0, MAX: 9},
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'FTX', MIN: 0, MAX: 9},
                {ID: 'QTY', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'RNG', MIN: 0, MAX: 1},
                ]},
                {ID: 'PCD', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'RNG', MIN: 0, MAX: 1},
                ]},
                {ID: 'MOA', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'RNG', MIN: 0, MAX: 1},
                ]},
                {ID: 'RTE', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'RNG', MIN: 0, MAX: 1},
                ]},
                {ID: 'TAX', MIN: 0, MAX: 5, LEVEL: [
                    {ID: 'MOA', MIN: 0, MAX: 1},
                ]},
            ]},
        ]},
        {ID: 'NAD', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'LOC', MIN: 0, MAX: 25},
            {ID: 'FII', MIN: 0, MAX: 9},
            {ID: 'MOA', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 5},
            {ID: 'RFF', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 5},
            ]},
            {ID: 'DOC', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 5},
            ]},
            {ID: 'CTA', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'COM', MIN: 0, MAX: 5},
            ]},
        ]},
    ]},
    {ID: 'UNS', MIN: 1, MAX: 1},
    {ID: 'BII', MIN: 0, MAX: 9999, LEVEL: [
        {ID: 'RCS', MIN: 1, MAX: 1},
        {ID: 'GEI', MIN: 1, MAX: 10},
        {ID: 'RFF', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
        ]},
        {ID: 'DIM', MIN: 0, MAX: 100, LEVEL: [
            {ID: 'APR', MIN: 0, MAX: 1},
            {ID: 'FTX', MIN: 0, MAX: 1},
        ]},
        {ID: 'LIN', MIN: 0, MAX: 100, LEVEL: [
            {ID: 'IMD', MIN: 0, MAX: 1000, LEVEL: [
                {ID: 'RFF', MIN: 0, MAX: 5},
                {ID: 'GEI', MIN: 0, MAX: 5},
            ]},
        ]},
        {ID: 'QTY', MIN: 1, MAX: 1000, LEVEL: [
            {ID: 'GEI', MIN: 0, MAX: 3},
            {ID: 'APR', MIN: 0, MAX: 1},
            {ID: 'PRI', MIN: 0, MAX: 3, LEVEL: [
                {ID: 'GEI', MIN: 1, MAX: 3},
                {ID: 'ARD', MIN: 0, MAX: 2, LEVEL: [
                    {ID: 'MOA', MIN: 0, MAX: 1},
                ]},
            ]},
        ]},
        {ID: 'TAX', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'MOA', MIN: 0, MAX: 1},
            {ID: 'LOC', MIN: 0, MAX: 5},
        ]},
        {ID: 'RCS', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'BII', MIN: 1, MAX: 1},
            {ID: 'GEI', MIN: 1, MAX: 1},
        ]},
        {ID: 'ALC', MIN: 0, MAX: 2, LEVEL: [
            {ID: 'RFF', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 1},
            {ID: 'RNG', MIN: 0, MAX: 1},
            {ID: 'FTX', MIN: 0, MAX: 10},
            {ID: 'PCD', MIN: 0, MAX: 20, LEVEL: [
                {ID: 'RFF', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'IMD', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'QTY', MIN: 0, MAX: 1},
            {ID: 'MOA', MIN: 0, MAX: 1},
            {ID: 'PRI', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'CNT', MIN: 0, MAX: 10},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

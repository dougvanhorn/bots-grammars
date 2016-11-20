#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD01AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'CST', MIN: 0, MAX: 1},
    {ID: 'LOC', MIN: 0, MAX: 99},
    {ID: 'DTM', MIN: 0, MAX: 99},
    {ID: 'GIS', MIN: 0, MAX: 99},
    {ID: 'FII', MIN: 0, MAX: 1},
    {ID: 'RFF', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'NAD', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 9},
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
        {ID: 'MOA', MIN: 0, MAX: 9},
        {ID: 'GIS', MIN: 0, MAX: 9},
    ]},
    {ID: 'CNT', MIN: 0, MAX: 9},
    {ID: 'DMS', MIN: 0, MAX: 9999, LEVEL: [
        {ID: 'CNT', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'GIS', MIN: 0, MAX: 99},
        {ID: 'LOC', MIN: 0, MAX: 99},
        {ID: 'EQD', MIN: 0, MAX: 999},
        {ID: 'PAC', MIN: 0, MAX: 9},
        {ID: 'TDT', MIN: 0, MAX: 9},
        {ID: 'NAD', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'COM', MIN: 0, MAX: 9},
            ]},
        ]},
        {ID: 'DOC', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'LOC', MIN: 0, MAX: 1},
            {ID: 'NAD', MIN: 0, MAX: 1},
        ]},
        {ID: 'TOD', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'LOC', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 9},
        ]},
        {ID: 'MOA', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'CUX', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'TAX', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'MOA', MIN: 0, MAX: 9},
            {ID: 'GIS', MIN: 0, MAX: 9},
        ]},
        {ID: 'CST', MIN: 0, MAX: 9999, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 9},
            {ID: 'LOC', MIN: 0, MAX: 99},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'MEA', MIN: 0, MAX: 99},
            {ID: 'NAD', MIN: 0, MAX: 9},
            {ID: 'TDT', MIN: 0, MAX: 9},
            {ID: 'PAC', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'PCI', MIN: 0, MAX: 999, LEVEL: [
                    {ID: 'FTX', MIN: 0, MAX: 1},
                ]},
            ]},
            {ID: 'MOA', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'CUX', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 1},
                ]},
            ]},
            {ID: 'DOC', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'LOC', MIN: 0, MAX: 1},
                {ID: 'NAD', MIN: 0, MAX: 1},
                {ID: 'GIN', MIN: 0, MAX: 99},
                {ID: 'MOA', MIN: 0, MAX: 1},
                {ID: 'IMD', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'FTX', MIN: 0, MAX: 9},
                ]},
            ]},
            {ID: 'RFF', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 1},
            ]},
            {ID: 'TOD', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'LOC', MIN: 0, MAX: 9},
                {ID: 'FTX', MIN: 0, MAX: 1},
            ]},
            {ID: 'GDS', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'FTX', MIN: 0, MAX: 1},
            ]},
            {ID: 'GIS', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'PCD', MIN: 0, MAX: 1},
                {ID: 'DTM', MIN: 0, MAX: 1},
                {ID: 'RFF', MIN: 0, MAX: 1},
            ]},
            {ID: 'TAX', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'MOA', MIN: 0, MAX: 9},
                {ID: 'GIS', MIN: 0, MAX: 1},
            ]},
            {ID: 'QVR', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'QTY', MIN: 0, MAX: 1},
                {ID: 'RFF', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 1},
                ]},
            ]},
            {ID: 'GIR', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'GIS', MIN: 0, MAX: 9},
                {ID: 'NAD', MIN: 0, MAX: 1},
                {ID: 'MEA', MIN: 0, MAX: 9},
                {ID: 'MOA', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'CUX', MIN: 0, MAX: 1, LEVEL: [
                        {ID: 'DTM', MIN: 0, MAX: 1},
                    ]},
                ]},
                {ID: 'TAX', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'MOA', MIN: 0, MAX: 9},
                    {ID: 'GIS', MIN: 0, MAX: 1},
                ]},
                {ID: 'DOC', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 9},
                    {ID: 'LOC', MIN: 0, MAX: 1},
                    {ID: 'NAD', MIN: 0, MAX: 1},
                ]},
            ]},
        ]},
    ]},
    {ID: 'AUT', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD09AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 5},
    {ID: 'LOC', MIN: 0, MAX: 5},
    {ID: 'CNT', MIN: 0, MAX: 9},
    {ID: 'NAD', MIN: 1, MAX: 1, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'TDT', MIN: 1, MAX: 1, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
        {ID: 'LOC', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'EQD', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'SEL', MIN: 0, MAX: 9},
    ]},
    {ID: 'RFF', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'NAD', MIN: 0, MAX: 2},
        {ID: 'CNT', MIN: 0, MAX: 1},
        {ID: 'CNI', MIN: 1, MAX: 9999, LEVEL: [
            {ID: 'SGP', MIN: 0, MAX: 9},
            {ID: 'CNT', MIN: 0, MAX: 9},
            {ID: 'MEA', MIN: 0, MAX: 1},
            {ID: 'LOC', MIN: 0, MAX: 2},
            {ID: 'NAD', MIN: 0, MAX: 5},
            {ID: 'GDS', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'FTX', MIN: 0, MAX: 1},
            ]},
            {ID: 'PAC', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'PCI', MIN: 0, MAX: 1},
            ]},
            {ID: 'TOD', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'LOC', MIN: 0, MAX: 1},
                {ID: 'FTX', MIN: 0, MAX: 1},
            ]},
            {ID: 'MOA', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'CUX', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 1},
                ]},
            ]},
            {ID: 'TAX', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'MOA', MIN: 0, MAX: 1},
                {ID: 'GEI', MIN: 0, MAX: 1},
            ]},
            {ID: 'DOC', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 1},
                {ID: 'LOC', MIN: 0, MAX: 1},
            ]},
            {ID: 'CST', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'FTX', MIN: 0, MAX: 1},
                {ID: 'LOC', MIN: 1, MAX: 1},
                {ID: 'MEA', MIN: 0, MAX: 9},
                {ID: 'TAX', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'MOA', MIN: 0, MAX: 1},
                    {ID: 'GEI', MIN: 0, MAX: 1},
                ]},
            ]},
        ]},
    ]},
    {ID: 'AUT', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

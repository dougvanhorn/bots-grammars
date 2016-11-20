#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD05BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 9},
    {ID: 'TSR', MIN: 0, MAX: 1},
    {ID: 'NAD', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'LOC', MIN: 0, MAX: 9},
    {ID: 'FTX', MIN: 0, MAX: 9},
    {ID: 'CNT', MIN: 0, MAX: 9},
    {ID: 'CNI', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'LOC', MIN: 0, MAX: 9},
        {ID: 'CNT', MIN: 0, MAX: 9},
        {ID: 'STS', MIN: 1, MAX: 99, LEVEL: [
            {ID: 'RFF', MIN: 0, MAX: 999},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'DOC', MIN: 0, MAX: 1},
            {ID: 'FTX', MIN: 0, MAX: 9},
            {ID: 'NAD', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'COM', MIN: 0, MAX: 9},
                ]},
            ]},
            {ID: 'LOC', MIN: 0, MAX: 1},
            {ID: 'PCI', MIN: 0, MAX: 99},
            {ID: 'TDT', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'RFF', MIN: 0, MAX: 9},
                {ID: 'LOC', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 9},
                ]},
            ]},
            {ID: 'EQD', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'MEA', MIN: 0, MAX: 9},
                {ID: 'DIM', MIN: 0, MAX: 9},
                {ID: 'SEL', MIN: 0, MAX: 9},
                {ID: 'RFF', MIN: 0, MAX: 9},
                {ID: 'TPL', MIN: 0, MAX: 9},
                {ID: 'TMD', MIN: 0, MAX: 1},
                {ID: 'LOC', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 9},
                ]},
                {ID: 'EQA', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'SEL', MIN: 0, MAX: 9},
                    {ID: 'LOC', MIN: 0, MAX: 9, LEVEL: [
                        {ID: 'DTM', MIN: 0, MAX: 9},
                    ]},
                ]},
            ]},
            {ID: 'GID', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'HAN', MIN: 0, MAX: 9},
                {ID: 'SGP', MIN: 0, MAX: 99},
                {ID: 'DGS', MIN: 0, MAX: 9},
                {ID: 'FTX', MIN: 0, MAX: 9},
                {ID: 'GDS', MIN: 0, MAX: 9},
                {ID: 'LOC', MIN: 0, MAX: 9},
                {ID: 'QTY', MIN: 0, MAX: 9},
                {ID: 'MEA', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'EQN', MIN: 0, MAX: 1},
                ]},
                {ID: 'DIM', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'EQN', MIN: 0, MAX: 1},
                ]},
                {ID: 'PCI', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'GIN', MIN: 0, MAX: 9999},
                ]},
                {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 9},
                ]},
            ]},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

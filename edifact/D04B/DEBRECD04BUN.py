#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD04BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 5},
    {ID: 'PNA', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'ADR', MIN: 0, MAX: 1},
        {ID: 'RFF', MIN: 0, MAX: 5},
        {ID: 'EMP', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 9},
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
            {ID: 'COM', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 9},
            ]},
        ]},
        {ID: 'AUT', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'GIR', MIN: 0, MAX: 9999, LEVEL: [
        {ID: 'ATT', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 3},
        ]},
        {ID: 'EVE', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'IRQ', MIN: 0, MAX: 99},
            {ID: 'FTX', MIN: 0, MAX: 99},
            {ID: 'ATT', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 3},
            ]},
            {ID: 'PNA', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'RFF', MIN: 0, MAX: 9},
                {ID: 'ATT', MIN: 0, MAX: 9},
                {ID: 'EMP', MIN: 0, MAX: 1},
                {ID: 'PDI', MIN: 0, MAX: 1},
                {ID: 'FII', MIN: 0, MAX: 9},
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'MOA', MIN: 0, MAX: 5},
                {ID: 'QTY', MIN: 0, MAX: 9},
                {ID: 'PCD', MIN: 0, MAX: 1},
                {ID: 'COM', MIN: 0, MAX: 1},
                {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 1},
                    {ID: 'FTX', MIN: 0, MAX: 9},
                    {ID: 'COM', MIN: 0, MAX: 5, LEVEL: [
                        {ID: 'DTM', MIN: 0, MAX: 9},
                    ]},
                ]},
                {ID: 'ADR', MIN: 0, MAX: 5, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 1},
                    {ID: 'COM', MIN: 0, MAX: 1, LEVEL: [
                        {ID: 'DTM', MIN: 0, MAX: 9},
                    ]},
                ]},
                {ID: 'REL', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'RFF', MIN: 0, MAX: 1},
                ]},
            ]},
            {ID: 'DOC', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'FTX', MIN: 0, MAX: 99},
                {ID: 'ATT', MIN: 0, MAX: 9},
                {ID: 'MOA', MIN: 0, MAX: 9},
                {ID: 'PNA', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'RFF', MIN: 0, MAX: 9},
                    {ID: 'ADR', MIN: 0, MAX: 5},
                ]},
            ]},
            {ID: 'IMD', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'STS', MIN: 0, MAX: 1},
                {ID: 'FTX', MIN: 0, MAX: 9},
                {ID: 'ATT', MIN: 0, MAX: 1},
                {ID: 'RFF', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'PIA', MIN: 0, MAX: 1},
                    {ID: 'LOC', MIN: 0, MAX: 2},
                    {ID: 'DTM', MIN: 0, MAX: 9},
                    {ID: 'MEA', MIN: 0, MAX: 9},
                    {ID: 'ATT', MIN: 0, MAX: 99},
                    {ID: 'FTX', MIN: 0, MAX: 1},
                ]},
                {ID: 'ADR', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
                        {ID: 'FTX', MIN: 0, MAX: 9},
                        {ID: 'MEA', MIN: 0, MAX: 1},
                    ]},
                ]},
                {ID: 'DOC', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 9},
                    {ID: 'FTX', MIN: 0, MAX: 9},
                ]},
            ]},
            {ID: 'GEI', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 3},
                {ID: 'FTX', MIN: 0, MAX: 9},
                {ID: 'DOC', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 9},
                    {ID: 'FTX', MIN: 0, MAX: 9},
                ]},
                {ID: 'ARD', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'MOA', MIN: 0, MAX: 2},
                    {ID: 'DTM', MIN: 0, MAX: 5},
                    {ID: 'TAX', MIN: 0, MAX: 9},
                    {ID: 'FTX', MIN: 0, MAX: 9},
                    {ID: 'ATT', MIN: 0, MAX: 9},
                    {ID: 'PCD', MIN: 0, MAX: 9, LEVEL: [
                        {ID: 'DTM', MIN: 0, MAX: 1},
                    ]},
                    {ID: 'PAI', MIN: 0, MAX: 9, LEVEL: [
                        {ID: 'RFF', MIN: 0, MAX: 9},
                    ]},
                ]},
            ]},
        ]},
    ]},
    {ID: 'CNT', MIN: 0, MAX: 99},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

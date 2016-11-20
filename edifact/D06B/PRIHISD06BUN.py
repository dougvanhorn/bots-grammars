#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD06BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 1},
    {ID: 'RFF', MIN: 0, MAX: 9},
    {ID: 'CUX', MIN: 0, MAX: 9},
    {ID: 'NAD', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'LOC', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
        ]},
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'LIN', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'PIA', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'IMD', MIN: 0, MAX: 9},
        {ID: 'MEA', MIN: 0, MAX: 9},
        {ID: 'PCD', MIN: 0, MAX: 9},
        {ID: 'ALI', MIN: 0, MAX: 9},
        {ID: 'GIR', MIN: 0, MAX: 9},
        {ID: 'NAD', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'LOC', MIN: 0, MAX: 9},
            {ID: 'STS', MIN: 0, MAX: 9},
            {ID: 'PIA', MIN: 0, MAX: 9},
            {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'COM', MIN: 0, MAX: 9},
            ]},
            {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'AGR', MIN: 0, MAX: 9},
                {ID: 'QTY', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 9},
                    {ID: 'TAX', MIN: 0, MAX: 9},
                    {ID: 'FTX', MIN: 0, MAX: 9},
                    {ID: 'PYT', MIN: 0, MAX: 9, LEVEL: [
                        {ID: 'DTM', MIN: 0, MAX: 9},
                        {ID: 'PCD', MIN: 0, MAX: 9},
                        {ID: 'MOA', MIN: 0, MAX: 9},
                    ]},
                    {ID: 'TOD', MIN: 0, MAX: 9, LEVEL: [
                        {ID: 'LOC', MIN: 0, MAX: 9},
                    ]},
                    {ID: 'ALC', MIN: 0, MAX: 99, LEVEL: [
                        {ID: 'ALI', MIN: 0, MAX: 9},
                        {ID: 'DTM', MIN: 0, MAX: 9},
                        {ID: 'QTY', MIN: 0, MAX: 9, LEVEL: [
                            {ID: 'RNG', MIN: 0, MAX: 1},
                        ]},
                        {ID: 'PCD', MIN: 0, MAX: 9, LEVEL: [
                            {ID: 'RNG', MIN: 0, MAX: 1},
                        ]},
                        {ID: 'MOA', MIN: 0, MAX: 9, LEVEL: [
                            {ID: 'RNG', MIN: 0, MAX: 1},
                        ]},
                        {ID: 'RTE', MIN: 0, MAX: 9, LEVEL: [
                            {ID: 'RNG', MIN: 0, MAX: 1},
                        ]},
                        {ID: 'TAX', MIN: 0, MAX: 9, LEVEL: [
                            {ID: 'MOA', MIN: 0, MAX: 1},
                        ]},
                    ]},
                    {ID: 'PRI', MIN: 1, MAX: 9, LEVEL: [
                        {ID: 'DTM', MIN: 0, MAX: 9},
                        {ID: 'CUX', MIN: 0, MAX: 9},
                        {ID: 'RNG', MIN: 0, MAX: 9},
                    ]},
                ]},
            ]},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

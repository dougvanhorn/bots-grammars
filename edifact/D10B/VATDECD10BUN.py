#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD10BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 1},
    {ID: 'LOC', MIN: 0, MAX: 1},
    {ID: 'NAD', MIN: 1, MAX: 9999, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
        {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 9},
        ]},
        {ID: 'FII', MIN: 0, MAX: 9},
        {ID: 'PAI', MIN: 0, MAX: 9},
        {ID: 'GEI', MIN: 0, MAX: 9},
        {ID: 'LOC', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'GEI', MIN: 0, MAX: 9},
            {ID: 'MEA', MIN: 0, MAX: 9},
            {ID: 'DMS', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'MOA', MIN: 0, MAX: 1},
                {ID: 'MEA', MIN: 0, MAX: 1},
                {ID: 'PCD', MIN: 0, MAX: 1},
                {ID: 'GEI', MIN: 0, MAX: 1},
            ]},
            {ID: 'LIN', MIN: 1, MAX: 9999, LEVEL: [
                {ID: 'NAD', MIN: 0, MAX: 9999, LEVEL: [
                    {ID: 'CTA', MIN: 0, MAX: 9999, LEVEL: [
                        {ID: 'COM', MIN: 0, MAX: 9},
                    ]},
                    {ID: 'RFF', MIN: 0, MAX: 9},
                    {ID: 'FII', MIN: 0, MAX: 1},
                ]},
                {ID: 'GEI', MIN: 0, MAX: 9},
                {ID: 'MOA', MIN: 1, MAX: 9999, LEVEL: [
                    {ID: 'ARD', MIN: 0, MAX: 1},
                    {ID: 'PCD', MIN: 0, MAX: 1},
                    {ID: 'GEI', MIN: 0, MAX: 9},
                    {ID: 'DMS', MIN: 0, MAX: 9, LEVEL: [
                        {ID: 'MOA', MIN: 0, MAX: 1},
                        {ID: 'MEA', MIN: 0, MAX: 1},
                        {ID: 'PCD', MIN: 0, MAX: 1},
                        {ID: 'GEI', MIN: 1, MAX: 1},
                    ]},
                ]},
            ]},
            {ID: 'CNT', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'MOA', MIN: 1, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'AUT', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
        {ID: 'RFF', MIN: 0, MAX: 1},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

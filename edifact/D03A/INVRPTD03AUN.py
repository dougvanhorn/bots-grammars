#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD03AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'FTX', MIN: 0, MAX: 99},
    {ID: 'DTM', MIN: 1, MAX: 10},
    {ID: 'RFF', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'NAD', MIN: 0, MAX: 20, LEVEL: [
        {ID: 'LOC', MIN: 0, MAX: 5},
        {ID: 'RFF', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
        ]},
        {ID: 'CTA', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'CUX', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'CPS', MIN: 0, MAX: 9999, LEVEL: [
        {ID: 'PAC', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'PCI', MIN: 0, MAX: 1000},
            {ID: 'QTY', MIN: 0, MAX: 9999, LEVEL: [
                {ID: 'GIN', MIN: 0, MAX: 9999},
                {ID: 'DTM', MIN: 0, MAX: 5},
            ]},
        ]},
    ]},
    {ID: 'LIN', MIN: 0, MAX: 9999999, LEVEL: [
        {ID: 'PIA', MIN: 0, MAX: 10},
        {ID: 'IMD', MIN: 0, MAX: 10},
        {ID: 'NAD', MIN: 0, MAX: 1},
        {ID: 'MEA', MIN: 0, MAX: 10},
        {ID: 'ALI', MIN: 0, MAX: 10},
        {ID: 'LOC', MIN: 0, MAX: 5},
        {ID: 'DTM', MIN: 0, MAX: 5},
        {ID: 'FTX', MIN: 0, MAX: 99},
        {ID: 'RFF', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
        ]},
        {ID: 'INV', MIN: 0, MAX: 9999, LEVEL: [
            {ID: 'QTY', MIN: 1, MAX: 1},
            {ID: 'GIN', MIN: 0, MAX: 9999},
            {ID: 'LOC', MIN: 0, MAX: 5},
            {ID: 'DTM', MIN: 0, MAX: 5},
            {ID: 'STS', MIN: 0, MAX: 9},
            {ID: 'NAD', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'LOC', MIN: 0, MAX: 1},
            ]},
            {ID: 'PRI', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'CUX', MIN: 0, MAX: 1},
                {ID: 'DTM', MIN: 0, MAX: 1},
            ]},
            {ID: 'RFF', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 1},
            ]},
            {ID: 'CPS', MIN: 0, MAX: 9999, LEVEL: [
                {ID: 'PAC', MIN: 0, MAX: 9999, LEVEL: [
                    {ID: 'MEA', MIN: 0, MAX: 10},
                    {ID: 'QTY', MIN: 0, MAX: 10},
                    {ID: 'PCI', MIN: 0, MAX: 9999, LEVEL: [
                        {ID: 'RFF', MIN: 0, MAX: 1},
                        {ID: 'DTM', MIN: 0, MAX: 5},
                        {ID: 'GIN', MIN: 0, MAX: 9999},
                        {ID: 'GIR', MIN: 0, MAX: 99, LEVEL: [
                            {ID: 'DTM', MIN: 0, MAX: 5},
                        ]},
                    ]},
                ]},
            ]},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

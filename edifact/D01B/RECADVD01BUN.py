#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD01BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 10},
    {ID: 'ALI', MIN: 0, MAX: 5},
    {ID: 'CUX', MIN: 0, MAX: 9},
    {ID: 'FTX', MIN: 0, MAX: 99},
    {ID: 'RFF', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
        {ID: 'GEI', MIN: 0, MAX: 99},
        {ID: 'MOA', MIN: 0, MAX: 99},
        {ID: 'ALC', MIN: 0, MAX: 1},
    ]},
    {ID: 'DOC', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'CDI', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'INP', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'NAD', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'LOC', MIN: 0, MAX: 10},
        {ID: 'RFF', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
        ]},
        {ID: 'CTA', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'TOD', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'CDI', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'INP', MIN: 0, MAX: 5},
        ]},
        {ID: 'LOC', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'CDI', MIN: 0, MAX: 10},
        ]},
    ]},
    {ID: 'TDT', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 10},
        {ID: 'CDI', MIN: 0, MAX: 20},
    ]},
    {ID: 'EQD', MIN: 0, MAX: 9999, LEVEL: [
        {ID: 'CDI', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'INP', MIN: 0, MAX: 5},
        ]},
        {ID: 'SEL', MIN: 0, MAX: 25, LEVEL: [
            {ID: 'CDI', MIN: 1, MAX: 10},
        ]},
        {ID: 'EQA', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'CDI', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'INP', MIN: 0, MAX: 5},
            ]},
        ]},
    ]},
    {ID: 'CPS', MIN: 0, MAX: 9999, LEVEL: [
        {ID: 'PAC', MIN: 0, MAX: 9999, LEVEL: [
            {ID: 'QVR', MIN: 0, MAX: 1},
            {ID: 'PCI', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'RFF', MIN: 0, MAX: 1},
                {ID: 'CDI', MIN: 0, MAX: 10, LEVEL: [
                    {ID: 'INP', MIN: 0, MAX: 5},
                ]},
                {ID: 'GIN', MIN: 0, MAX: 999, LEVEL: [
                    {ID: 'CDI', MIN: 0, MAX: 10, LEVEL: [
                        {ID: 'INP', MIN: 0, MAX: 5},
                    ]},
                ]},
            ]},
        ]},
        {ID: 'LIN', MIN: 0, MAX: 9999, LEVEL: [
            {ID: 'PIA', MIN: 0, MAX: 10},
            {ID: 'IMD', MIN: 0, MAX: 25},
            {ID: 'QTY', MIN: 0, MAX: 10},
            {ID: 'QVR', MIN: 0, MAX: 10},
            {ID: 'DTM', MIN: 0, MAX: 5},
            {ID: 'PRI', MIN: 0, MAX: 1},
            {ID: 'FTX', MIN: 0, MAX: 99},
            {ID: 'NAD', MIN: 0, MAX: 99},
            {ID: 'CDI', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'INP', MIN: 0, MAX: 5},
            ]},
            {ID: 'DOC', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'CDI', MIN: 0, MAX: 10, LEVEL: [
                    {ID: 'INP', MIN: 0, MAX: 5},
                ]},
            ]},
            {ID: 'GIN', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'CDI', MIN: 0, MAX: 10, LEVEL: [
                    {ID: 'INP', MIN: 0, MAX: 5},
                ]},
            ]},
            {ID: 'RFF', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 1},
                {ID: 'GEI', MIN: 0, MAX: 99},
                {ID: 'MOA', MIN: 0, MAX: 99},
                {ID: 'ALC', MIN: 0, MAX: 1},
            ]},
            {ID: 'PCI', MIN: 0, MAX: 9999, LEVEL: [
                {ID: 'QTY', MIN: 0, MAX: 1},
                {ID: 'QVR', MIN: 0, MAX: 1},
                {ID: 'CDI', MIN: 0, MAX: 10, LEVEL: [
                    {ID: 'INP', MIN: 0, MAX: 5},
                ]},
                {ID: 'GIN', MIN: 0, MAX: 10, LEVEL: [
                    {ID: 'CDI', MIN: 0, MAX: 10, LEVEL: [
                        {ID: 'INP', MIN: 0, MAX: 5},
                    ]},
                ]},
            ]},
        ]},
    ]},
    {ID: 'CNT', MIN: 0, MAX: 1},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

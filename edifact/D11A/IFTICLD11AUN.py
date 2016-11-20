#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD11AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 9},
    {ID: 'FTX', MIN: 0, MAX: 99},
    {ID: 'LOC', MIN: 0, MAX: 99},
    {ID: 'DOC', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'EFI', MIN: 0, MAX: 1},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'NAD', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'COM', MIN: 0, MAX: 9},
            ]},
        ]},
    ]},
    {ID: 'RFF', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'TDT', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'MEA', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'NAD', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'COM', MIN: 0, MAX: 9},
            ]},
        ]},
        {ID: 'LOC', MIN: 1, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
        ]},
        {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'NAD', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'STS', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'ICD', MIN: 0, MAX: 9},
        {ID: 'LOC', MIN: 0, MAX: 9},
        {ID: 'MEA', MIN: 0, MAX: 9},
        {ID: 'QRS', MIN: 0, MAX: 99},
        {ID: 'FTX', MIN: 0, MAX: 99},
        {ID: 'MOA', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'CUX', MIN: 0, MAX: 1},
        ]},
        {ID: 'DOC', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'EFI', MIN: 0, MAX: 1},
            {ID: 'FTX', MIN: 0, MAX: 9},
            {ID: 'NAD', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'COM', MIN: 0, MAX: 9},
                ]},
            ]},
        ]},
    ]},
    {ID: 'GID', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'PIA', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'PCI', MIN: 0, MAX: 9},
        {ID: 'SGP', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'MEA', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'EQN', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'DGS', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 99},
        ]},
        {ID: 'STS', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'ICD', MIN: 0, MAX: 9},
            {ID: 'LOC', MIN: 0, MAX: 9},
            {ID: 'MEA', MIN: 0, MAX: 9},
            {ID: 'QRS', MIN: 0, MAX: 99},
            {ID: 'FTX', MIN: 0, MAX: 99},
            {ID: 'MOA', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'CUX', MIN: 0, MAX: 1},
            ]},
            {ID: 'DOC', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'EFI', MIN: 0, MAX: 1},
                {ID: 'FTX', MIN: 0, MAX: 9},
                {ID: 'NAD', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
                        {ID: 'COM', MIN: 0, MAX: 9},
                    ]},
                ]},
            ]},
        ]},
    ]},
    {ID: 'EQD', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'EQN', MIN: 0, MAX: 1},
        {ID: 'TMD', MIN: 0, MAX: 1},
        {ID: 'MEA', MIN: 0, MAX: 9},
        {ID: 'DIM', MIN: 0, MAX: 9},
        {ID: 'SEL', MIN: 0, MAX: 99},
        {ID: 'LOC', MIN: 0, MAX: 1},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'NAD', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'COM', MIN: 0, MAX: 9},
            ]},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

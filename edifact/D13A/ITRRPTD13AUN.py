#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD13AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 10},
    {ID: 'MEA', MIN: 0, MAX: 5},
    {ID: 'CUX', MIN: 0, MAX: 9},
    {ID: 'RFF', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 5},
    ]},
    {ID: 'NAD', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'LOC', MIN: 0, MAX: 10},
        {ID: 'RFF', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 5},
        ]},
        {ID: 'CTA', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'TDT', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'PCD', MIN: 0, MAX: 5},
        {ID: 'LOC', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 10},
        ]},
    ]},
    {ID: 'EQD', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'MEA', MIN: 0, MAX: 5},
        {ID: 'SEL', MIN: 0, MAX: 99},
        {ID: 'EQA', MIN: 0, MAX: 5},
        {ID: 'PCD', MIN: 0, MAX: 5},
        {ID: 'HAN', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 10},
        ]},
    ]},
    {ID: 'GEI', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'CDI', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 10},
        {ID: 'ALI', MIN: 0, MAX: 5},
        {ID: 'MEA', MIN: 0, MAX: 5},
        {ID: 'MOA', MIN: 0, MAX: 5},
        {ID: 'RFF', MIN: 1, MAX: 10, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
        ]},
        {ID: 'NAD', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'LOC', MIN: 0, MAX: 10},
            {ID: 'RFF', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 1},
            ]},
            {ID: 'CTA', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'COM', MIN: 0, MAX: 5},
            ]},
        ]},
        {ID: 'TOD', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'LOC', MIN: 0, MAX: 5},
            {ID: 'FTX', MIN: 0, MAX: 5},
        ]},
        {ID: 'CPS', MIN: 0, MAX: 9999, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 5},
            {ID: 'PAC', MIN: 0, MAX: 9999, LEVEL: [
                {ID: 'MEA', MIN: 0, MAX: 10},
                {ID: 'QTY', MIN: 0, MAX: 10},
                {ID: 'HAN', MIN: 0, MAX: 10, LEVEL: [
                    {ID: 'FTX', MIN: 0, MAX: 10},
                ]},
                {ID: 'PCI', MIN: 0, MAX: 9999, LEVEL: [
                    {ID: 'RFF', MIN: 0, MAX: 1},
                    {ID: 'CDI', MIN: 0, MAX: 1},
                    {ID: 'DTM', MIN: 0, MAX: 5},
                    {ID: 'GIN', MIN: 0, MAX: 99, LEVEL: [
                        {ID: 'CDI', MIN: 0, MAX: 1},
                        {ID: 'DLM', MIN: 0, MAX: 999},
                    ]},
                ]},
            ]},
            {ID: 'LIN', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'PIA', MIN: 0, MAX: 10},
                {ID: 'IMD', MIN: 0, MAX: 99},
                {ID: 'MEA', MIN: 0, MAX: 10},
                {ID: 'CDI', MIN: 0, MAX: 1},
                {ID: 'QTY', MIN: 0, MAX: 10},
                {ID: 'ALI', MIN: 0, MAX: 10},
                {ID: 'GIN', MIN: 0, MAX: 999},
                {ID: 'GIR', MIN: 0, MAX: 999},
                {ID: 'DTM', MIN: 0, MAX: 5},
                {ID: 'MOA', MIN: 0, MAX: 1},
                {ID: 'FTX', MIN: 0, MAX: 5},
                {ID: 'RFF', MIN: 0, MAX: 10, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 1},
                ]},
                {ID: 'DGS', MIN: 0, MAX: 10, LEVEL: [
                    {ID: 'QTY', MIN: 0, MAX: 1},
                    {ID: 'FTX', MIN: 0, MAX: 5},
                ]},
                {ID: 'PCI', MIN: 0, MAX: 9999, LEVEL: [
                    {ID: 'CDI', MIN: 0, MAX: 1},
                    {ID: 'DTM', MIN: 0, MAX: 5},
                    {ID: 'QTY', MIN: 0, MAX: 1},
                    {ID: 'MEA', MIN: 0, MAX: 10},
                    {ID: 'GIN', MIN: 0, MAX: 10, LEVEL: [
                        {ID: 'CDI', MIN: 0, MAX: 1},
                        {ID: 'DLM', MIN: 0, MAX: 999},
                    ]},
                    {ID: 'HAN', MIN: 0, MAX: 10, LEVEL: [
                        {ID: 'FTX', MIN: 0, MAX: 5},
                        {ID: 'GIN', MIN: 0, MAX: 9999},
                    ]},
                ]},
            ]},
        ]},
    ]},
    {ID: 'CNT', MIN: 0, MAX: 1},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

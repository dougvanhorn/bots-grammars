#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD01AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'CUX', MIN: 0, MAX: 1},
    {ID: 'PNA', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'ATT', MIN: 0, MAX: 9},
        {ID: 'ADR', MIN: 0, MAX: 9},
        {ID: 'COM', MIN: 0, MAX: 9},
    ]},
    {ID: 'DOC', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'ATT', MIN: 0, MAX: 9},
        {ID: 'ADR', MIN: 0, MAX: 9},
        {ID: 'LOC', MIN: 0, MAX: 9},
        {ID: 'COM', MIN: 0, MAX: 9},
        {ID: 'GEI', MIN: 0, MAX: 1},
        {ID: 'FTX', MIN: 0, MAX: 99},
    ]},
    {ID: 'MOA', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'PAI', MIN: 0, MAX: 1},
        {ID: 'FII', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'EVE', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'ATT', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
    ]},
    {ID: 'DSI', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'PNA', MIN: 0, MAX: 9},
        {ID: 'REL', MIN: 0, MAX: 1},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'EVE', MIN: 1, MAX: 999, LEVEL: [
            {ID: 'ATT', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 99},
            {ID: 'REL', MIN: 1, MAX: 9999, LEVEL: [
                {ID: 'PNA', MIN: 0, MAX: 9},
                {ID: 'RFF', MIN: 0, MAX: 999},
                {ID: 'NAT', MIN: 0, MAX: 2},
                {ID: 'PDI', MIN: 0, MAX: 1},
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'ADR', MIN: 0, MAX: 9},
                {ID: 'LOC', MIN: 0, MAX: 9},
                {ID: 'COM', MIN: 0, MAX: 9},
                {ID: 'QTY', MIN: 0, MAX: 99},
                {ID: 'FTX', MIN: 0, MAX: 999},
                {ID: 'ATT', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'GEI', MIN: 0, MAX: 1},
                    {ID: 'DTM', MIN: 0, MAX: 9},
                    {ID: 'MEA', MIN: 0, MAX: 1},
                    {ID: 'FTX', MIN: 0, MAX: 99},
                ]},
                {ID: 'MOA', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'ATT', MIN: 0, MAX: 9},
                    {ID: 'DTM', MIN: 0, MAX: 9},
                    {ID: 'QTY', MIN: 0, MAX: 9},
                    {ID: 'FTX', MIN: 0, MAX: 99},
                ]},
                {ID: 'DOC', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'ATT', MIN: 0, MAX: 9},
                    {ID: 'LOC', MIN: 0, MAX: 9},
                    {ID: 'DTM', MIN: 0, MAX: 9},
                ]},
                {ID: 'TAX', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'ATT', MIN: 0, MAX: 9},
                    {ID: 'LOC', MIN: 0, MAX: 9},
                    {ID: 'FTX', MIN: 0, MAX: 9},
                ]},
                {ID: 'EMP', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'ATT', MIN: 0, MAX: 9},
                    {ID: 'LOC', MIN: 0, MAX: 9},
                    {ID: 'DTM', MIN: 0, MAX: 9},
                ]},
                {ID: 'ICD', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'PNA', MIN: 0, MAX: 9, LEVEL: [
                        {ID: 'ADR', MIN: 0, MAX: 9},
                        {ID: 'LOC', MIN: 0, MAX: 9},
                    ]},
                ]},
            ]},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

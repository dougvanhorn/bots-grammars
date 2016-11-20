#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD08BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 9},
    {ID: 'RFF', MIN: 0, MAX: 99},
    {ID: 'PNA', MIN: 1, MAX: 9, LEVEL: [
        {ID: 'ADR', MIN: 0, MAX: 1},
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'LIN', MIN: 0, MAX: 999999, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 99},
        {ID: 'PNA', MIN: 0, MAX: 9},
        {ID: 'CUX', MIN: 0, MAX: 1},
        {ID: 'LAN', MIN: 0, MAX: 1},
        {ID: 'IFD', MIN: 0, MAX: 99},
        {ID: 'FTX', MIN: 0, MAX: 99},
        {ID: 'HYN', MIN: 0, MAX: 999999, LEVEL: [
            {ID: 'IRQ', MIN: 0, MAX: 99},
            {ID: 'IFD', MIN: 0, MAX: 99},
            {ID: 'PCD', MIN: 0, MAX: 99},
            {ID: 'DTM', MIN: 0, MAX: 99},
            {ID: 'RFF', MIN: 0, MAX: 99},
            {ID: 'MEA', MIN: 0, MAX: 99},
            {ID: 'CUX', MIN: 0, MAX: 1},
            {ID: 'FTX', MIN: 0, MAX: 99},
            {ID: 'MOA', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'ARD', MIN: 0, MAX: 9},
                {ID: 'PCD', MIN: 0, MAX: 9},
                {ID: 'FTX', MIN: 0, MAX: 1},
            ]},
            {ID: 'ATT', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'MEA', MIN: 0, MAX: 9},
                {ID: 'PCD', MIN: 0, MAX: 1},
            ]},
            {ID: 'RSL', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'CAV', MIN: 0, MAX: 99},
                {ID: 'FTX', MIN: 0, MAX: 99},
            ]},
            {ID: 'RCS', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'IFD', MIN: 0, MAX: 99},
                {ID: 'MEA', MIN: 0, MAX: 9},
                {ID: 'ATT', MIN: 0, MAX: 99},
                {ID: 'MOA', MIN: 0, MAX: 999, LEVEL: [
                    {ID: 'ARD', MIN: 0, MAX: 9},
                    {ID: 'FTX', MIN: 0, MAX: 1},
                ]},
            ]},
            {ID: 'QTY', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'FTX', MIN: 0, MAX: 1},
            ]},
            {ID: 'BUS', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'PYT', MIN: 0, MAX: 9},
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'RNG', MIN: 0, MAX: 9},
                {ID: 'PCD', MIN: 0, MAX: 1},
            ]},
            {ID: 'GEI', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'IMD', MIN: 0, MAX: 99},
                {ID: 'CAV', MIN: 0, MAX: 99},
                {ID: 'PCD', MIN: 0, MAX: 1},
                {ID: 'EQN', MIN: 0, MAX: 1},
                {ID: 'RFF', MIN: 0, MAX: 99},
                {ID: 'MOA', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'ARD', MIN: 0, MAX: 9},
                    {ID: 'FTX', MIN: 0, MAX: 1},
                ]},
            ]},
            {ID: 'REL', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'ATT', MIN: 0, MAX: 99},
            ]},
            {ID: 'STS', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'ATT', MIN: 0, MAX: 99},
            ]},
            {ID: 'PNA', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'REL', MIN: 0, MAX: 9},
                {ID: 'ADR', MIN: 0, MAX: 99},
                {ID: 'FII', MIN: 0, MAX: 9},
                {ID: 'ATT', MIN: 0, MAX: 99},
                {ID: 'PDI', MIN: 0, MAX: 1},
                {ID: 'EMP', MIN: 0, MAX: 9},
                {ID: 'NAT', MIN: 0, MAX: 9},
                {ID: 'RFF', MIN: 0, MAX: 9},
                {ID: 'LAN', MIN: 0, MAX: 9},
                {ID: 'DTM', MIN: 0, MAX: 99},
                {ID: 'IFD', MIN: 0, MAX: 99},
                {ID: 'PCD', MIN: 0, MAX: 9},
                {ID: 'COM', MIN: 0, MAX: 9},
                {ID: 'QTY', MIN: 0, MAX: 99},
                {ID: 'FTX', MIN: 0, MAX: 99},
                {ID: 'MOA', MIN: 0, MAX: 999, LEVEL: [
                    {ID: 'ARD', MIN: 0, MAX: 9},
                    {ID: 'FTX', MIN: 0, MAX: 1},
                ]},
            ]},
            {ID: 'EVE', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 99},
                {ID: 'IFD', MIN: 0, MAX: 99},
                {ID: 'FTX', MIN: 0, MAX: 99},
            ]},
            {ID: 'LOC', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'REL', MIN: 0, MAX: 9},
                {ID: 'ADR', MIN: 0, MAX: 9},
                {ID: 'DTM', MIN: 0, MAX: 99},
                {ID: 'COM', MIN: 0, MAX: 99},
                {ID: 'IFD', MIN: 0, MAX: 99},
                {ID: 'FTX', MIN: 0, MAX: 99},
                {ID: 'PNA', MIN: 0, MAX: 999, LEVEL: [
                    {ID: 'REL', MIN: 0, MAX: 99},
                ]},
                {ID: 'MOA', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'ARD', MIN: 0, MAX: 9},
                    {ID: 'FTX', MIN: 0, MAX: 1},
                ]},
            ]},
            {ID: 'APR', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'LOC', MIN: 0, MAX: 99},
                {ID: 'PCD', MIN: 0, MAX: 1},
                {ID: 'FTX', MIN: 0, MAX: 99},
            ]},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

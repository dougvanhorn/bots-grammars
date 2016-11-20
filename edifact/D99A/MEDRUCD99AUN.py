#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD99AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 9},
    {ID: 'RFF', MIN: 0, MAX: 9},
    {ID: 'FTX', MIN: 0, MAX: 9},
    {ID: 'CNT', MIN: 0, MAX: 9},
    {ID: 'MOA', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'TAX', MIN: 0, MAX: 1},
    ]},
    {ID: 'PNA', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'SEQ', MIN: 0, MAX: 1},
        {ID: 'ADR', MIN: 0, MAX: 9},
        {ID: 'CTA', MIN: 0, MAX: 9},
        {ID: 'COM', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 99},
        {ID: 'LAN', MIN: 0, MAX: 9},
        {ID: 'SPR', MIN: 0, MAX: 1},
        {ID: 'EMP', MIN: 0, MAX: 9},
        {ID: 'QUA', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 99},
        {ID: 'RCS', MIN: 0, MAX: 99},
        {ID: 'FII', MIN: 0, MAX: 9},
    ]},
    {ID: 'AGR', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'SEQ', MIN: 0, MAX: 1},
        {ID: 'RFF', MIN: 0, MAX: 99},
        {ID: 'DTM', MIN: 0, MAX: 99},
        {ID: 'ICD', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'FCA', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'GIS', MIN: 0, MAX: 1},
        {ID: 'RFF', MIN: 0, MAX: 99},
        {ID: 'DTM', MIN: 0, MAX: 99},
        {ID: 'FTX', MIN: 0, MAX: 99},
        {ID: 'AGR', MIN: 0, MAX: 99},
        {ID: 'RCS', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 9},
        ]},
        {ID: 'PNA', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'RFF', MIN: 0, MAX: 99},
            {ID: 'ADR', MIN: 0, MAX: 9},
            {ID: 'COM', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 99},
            {ID: 'PDI', MIN: 0, MAX: 1},
            {ID: 'NAT', MIN: 0, MAX: 9},
            {ID: 'LAN', MIN: 0, MAX: 9},
            {ID: 'HAN', MIN: 0, MAX: 9},
            {ID: 'REL', MIN: 0, MAX: 1},
        ]},
        {ID: 'PRC', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'GIS', MIN: 0, MAX: 1},
            {ID: 'IMD', MIN: 0, MAX: 9},
            {ID: 'CIN', MIN: 0, MAX: 99},
            {ID: 'PNA', MIN: 0, MAX: 99},
            {ID: 'DTM', MIN: 0, MAX: 99},
            {ID: 'RFF', MIN: 0, MAX: 99},
            {ID: 'FTX', MIN: 0, MAX: 99},
            {ID: 'QTY', MIN: 0, MAX: 99},
            {ID: 'PCD', MIN: 0, MAX: 99},
            {ID: 'PAS', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'LOC', MIN: 0, MAX: 9},
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'RFF', MIN: 0, MAX: 9},
            ]},
            {ID: 'MOA', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'TAX', MIN: 0, MAX: 1},
            ]},
            {ID: 'RCS', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'FTX', MIN: 0, MAX: 9},
            ]},
            {ID: 'CLI', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'GIS', MIN: 0, MAX: 1},
                {ID: 'IMD', MIN: 0, MAX: 9},
                {ID: 'CIN', MIN: 0, MAX: 99},
                {ID: 'PNA', MIN: 0, MAX: 99},
                {ID: 'DTM', MIN: 0, MAX: 99},
                {ID: 'RFF', MIN: 0, MAX: 99},
                {ID: 'FTX', MIN: 0, MAX: 99},
                {ID: 'QTY', MIN: 0, MAX: 99},
                {ID: 'PCD', MIN: 0, MAX: 99},
                {ID: 'PAC', MIN: 0, MAX: 9},
                {ID: 'MOA', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'TAX', MIN: 0, MAX: 1},
                ]},
                {ID: 'RCS', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'FTX', MIN: 0, MAX: 9},
                ]},
                {ID: 'EQD', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'SEQ', MIN: 0, MAX: 1},
                ]},
            ]},
        ]},
    ]},
    {ID: 'TMD', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'SEQ', MIN: 0, MAX: 1},
        {ID: 'GIS', MIN: 0, MAX: 1},
        {ID: 'FTX', MIN: 0, MAX: 99},
        {ID: 'TDT', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'GIS', MIN: 0, MAX: 1},
            {ID: 'IMD', MIN: 0, MAX: 9},
            {ID: 'PNA', MIN: 0, MAX: 99},
            {ID: 'RFF', MIN: 0, MAX: 99},
            {ID: 'FTX', MIN: 0, MAX: 99},
            {ID: 'CIN', MIN: 0, MAX: 99},
            {ID: 'QTY', MIN: 0, MAX: 99},
            {ID: 'ADR', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 9},
            ]},
            {ID: 'TSR', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'FTX', MIN: 0, MAX: 9},
            ]},
            {ID: 'TCC', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'GIS', MIN: 0, MAX: 1},
                {ID: 'IMD', MIN: 0, MAX: 9},
                {ID: 'DTM', MIN: 0, MAX: 99},
                {ID: 'RFF', MIN: 0, MAX: 99},
                {ID: 'FTX', MIN: 0, MAX: 99},
                {ID: 'QTY', MIN: 0, MAX: 99},
                {ID: 'PCD', MIN: 0, MAX: 99},
                {ID: 'MOA', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'TAX', MIN: 0, MAX: 1},
                ]},
                {ID: 'TSR', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'FTX', MIN: 0, MAX: 9},
                ]},
            ]},
        ]},
    ]},
    {ID: 'AUT', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

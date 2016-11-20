#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD03AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 99},
    {ID: 'STS', MIN: 0, MAX: 99},
    {ID: 'LOC', MIN: 0, MAX: 99},
    {ID: 'RFF', MIN: 0, MAX: 99},
    {ID: 'FTX', MIN: 0, MAX: 99},
    {ID: 'MEA', MIN: 0, MAX: 99},
    {ID: 'MOA', MIN: 0, MAX: 99},
    {ID: 'GEI', MIN: 0, MAX: 99},
    {ID: 'CST', MIN: 0, MAX: 1},
    {ID: 'DOC', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'LOC', MIN: 0, MAX: 9},
    ]},
    {ID: 'PNA', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'ADR', MIN: 0, MAX: 9},
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'TDT', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'LOC', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9},
    ]},
    {ID: 'PAC', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'PCI', MIN: 0, MAX: 9},
        {ID: 'MEA', MIN: 0, MAX: 9},
    ]},
    {ID: 'EQD', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'TMP', MIN: 0, MAX: 9},
        {ID: 'SEL', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'LOC', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'PRC', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'IMD', MIN: 0, MAX: 9},
        {ID: 'MEA', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'LOC', MIN: 0, MAX: 9},
        {ID: 'DOC', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'TMP', MIN: 0, MAX: 9},
        {ID: 'GEI', MIN: 0, MAX: 99},
        {ID: 'FTX', MIN: 0, MAX: 99},
        {ID: 'PNA', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'ADR', MIN: 0, MAX: 9},
            {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'COM', MIN: 0, MAX: 9},
            ]},
        ]},
    ]},
    {ID: 'LIN', MIN: 0, MAX: 9999, LEVEL: [
        {ID: 'CST', MIN: 0, MAX: 9},
        {ID: 'MEA', MIN: 0, MAX: 9},
        {ID: 'PIA', MIN: 0, MAX: 9},
        {ID: 'IMD', MIN: 0, MAX: 9},
        {ID: 'GIN', MIN: 0, MAX: 9999},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'ATT', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'LOC', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'QTY', MIN: 0, MAX: 9},
        {ID: 'MOA', MIN: 0, MAX: 9},
        {ID: 'DOC', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'LOC', MIN: 0, MAX: 9},
        ]},
        {ID: 'PNA', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'ADR', MIN: 0, MAX: 9},
            {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'COM', MIN: 0, MAX: 9},
            ]},
        ]},
        {ID: 'PAC', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'PCI', MIN: 0, MAX: 9},
            {ID: 'MEA', MIN: 0, MAX: 9},
        ]},
        {ID: 'EQD', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'TMP', MIN: 0, MAX: 9},
            {ID: 'SEL', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'LOC', MIN: 0, MAX: 9},
            ]},
        ]},
        {ID: 'PRC', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'IMD', MIN: 0, MAX: 9},
            {ID: 'MEA', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'LOC', MIN: 0, MAX: 9},
            {ID: 'DOC', MIN: 0, MAX: 9},
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'TMP', MIN: 0, MAX: 9},
            {ID: 'GEI', MIN: 0, MAX: 99},
            {ID: 'FTX', MIN: 0, MAX: 99},
            {ID: 'PNA', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'ADR', MIN: 0, MAX: 9},
                {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'COM', MIN: 0, MAX: 9},
                ]},
            ]},
        ]},
    ]},
    {ID: 'CNT', MIN: 0, MAX: 9},
    {ID: 'AUT', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

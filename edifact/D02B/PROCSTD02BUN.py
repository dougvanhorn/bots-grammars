#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD02BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'PRI', MIN: 0, MAX: 1},
    {ID: 'CUX', MIN: 0, MAX: 1},
    {ID: 'ATT', MIN: 0, MAX: 99},
    {ID: 'MOA', MIN: 0, MAX: 99},
    {ID: 'PCD', MIN: 0, MAX: 99},
    {ID: 'DTM', MIN: 0, MAX: 99},
    {ID: 'RFF', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'IMD', MIN: 0, MAX: 9},
    ]},
    {ID: 'QTY', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'IMD', MIN: 0, MAX: 1},
        {ID: 'CCI', MIN: 0, MAX: 1},
        {ID: 'ATT', MIN: 0, MAX: 9},
    ]},
    {ID: 'PNA', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'ADR', MIN: 0, MAX: 1},
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'EFI', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'CED', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'LIN', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'ATT', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'QTY', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 1},
            {ID: 'IMD', MIN: 0, MAX: 1},
        ]},
        {ID: 'IDE', MIN: 0, MAX: 9999, LEVEL: [
            {ID: 'REL', MIN: 0, MAX: 1},
            {ID: 'IMD', MIN: 0, MAX: 1},
            {ID: 'RCS', MIN: 0, MAX: 9},
            {ID: 'CCI', MIN: 0, MAX: 9},
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'STA', MIN: 0, MAX: 99},
            {ID: 'FTX', MIN: 0, MAX: 99},
            {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'COM', MIN: 0, MAX: 9},
            ]},
            {ID: 'MOA', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 9},
            ]},
            {ID: 'QTY', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 9},
            ]},
            {ID: 'PCD', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 9},
            ]},
            {ID: 'CAV', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'PRC', MIN: 0, MAX: 1},
                {ID: 'IMD', MIN: 0, MAX: 1},
                {ID: 'RFF', MIN: 0, MAX: 9},
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'STA', MIN: 0, MAX: 99},
                {ID: 'MOA', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 9},
                ]},
                {ID: 'QTY', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 9},
                ]},
                {ID: 'PCD', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 9},
                ]},
            ]},
        ]},
    ]},
    {ID: 'CNT', MIN: 0, MAX: 9},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

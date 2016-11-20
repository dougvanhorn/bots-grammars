#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD05AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DII', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 9},
    {ID: 'FTX', MIN: 1, MAX: 99},
    {ID: 'RFF', MIN: 0, MAX: 999},
    {ID: 'EFI', MIN: 0, MAX: 9},
    {ID: 'PNA', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'ADR', MIN: 0, MAX: 1},
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'MSG', MIN: 1, MAX: 1, LEVEL: [
        {ID: 'ATT', MIN: 0, MAX: 99},
        {ID: 'FTX', MIN: 0, MAX: 999},
        {ID: 'SGU', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'ATT', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 99},
            {ID: 'GRU', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'ATT', MIN: 0, MAX: 9},
                {ID: 'FTX', MIN: 0, MAX: 99},
            ]},
        ]},
        {ID: 'FNT', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'REL', MIN: 0, MAX: 1},
            {ID: 'GIR', MIN: 0, MAX: 9},
            {ID: 'ATT', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'SEG', MIN: 0, MAX: 9999, LEVEL: [
        {ID: 'ATT', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'ELU', MIN: 0, MAX: 99},
        {ID: 'FNT', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'REL', MIN: 0, MAX: 1},
            {ID: 'GIR', MIN: 0, MAX: 9},
            {ID: 'ATT', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'CMP', MIN: 0, MAX: 9999, LEVEL: [
        {ID: 'ATT', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'ELU', MIN: 0, MAX: 99},
        {ID: 'FNT', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'REL', MIN: 0, MAX: 1},
            {ID: 'GIR', MIN: 0, MAX: 9},
            {ID: 'ATT', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'ELM', MIN: 0, MAX: 9999, LEVEL: [
        {ID: 'ATT', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
    ]},
    {ID: 'CDS', MIN: 0, MAX: 9999, LEVEL: [
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'CDV', MIN: 0, MAX: 9999, LEVEL: [
            {ID: 'ATT', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

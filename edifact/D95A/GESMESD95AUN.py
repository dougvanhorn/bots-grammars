#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD95AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 0, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 9},
    {ID: 'FNT', MIN: 0, MAX: 9999, LEVEL: [
        {ID: 'FTX', MIN: 0, MAX: 9999},
    ]},
    {ID: 'NAD', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'IDE', MIN: 0, MAX: 1},
        {ID: 'CTA', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'VLI', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9999},
        {ID: 'FTX', MIN: 0, MAX: 9999},
        {ID: 'IDE', MIN: 0, MAX: 9},
        {ID: 'GIR', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 2},
        ]},
        {ID: 'CDV', MIN: 0, MAX: 9999, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 999},
            {ID: 'IDE', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'STC', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'FTX', MIN: 0, MAX: 5},
        {ID: 'IDE', MIN: 0, MAX: 5},
    ]},
    {ID: 'ASI', MIN: 0, MAX: 9999, LEVEL: [
        {ID: 'GIS', MIN: 0, MAX: 5},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'IDE', MIN: 0, MAX: 5},
        {ID: 'SCD', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'ATT', MIN: 0, MAX: 99},
            {ID: 'IDE', MIN: 0, MAX: 9999, LEVEL: [
                {ID: 'ATT', MIN: 0, MAX: 99},
                {ID: 'DTM', MIN: 0, MAX: 2},
            ]},
        ]},
    ]},
    {ID: 'DSI', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'STS', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 5},
        {ID: 'FTX', MIN: 0, MAX: 5},
        {ID: 'GIR', MIN: 0, MAX: 2},
        {ID: 'ARR', MIN: 0, MAX: 9999},
        {ID: 'IDE', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'GIS', MIN: 0, MAX: 5},
            {ID: 'DTM', MIN: 0, MAX: 5},
            {ID: 'CDV', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'FTX', MIN: 0, MAX: 99},
            ]},
            {ID: 'SCD', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'ATT', MIN: 0, MAX: 9},
                {ID: 'DTM', MIN: 0, MAX: 9999},
                {ID: 'CDV', MIN: 0, MAX: 9999, LEVEL: [
                    {ID: 'FTX', MIN: 0, MAX: 99},
                ]},
            ]},
        ]},
        {ID: 'NAD', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'IDE', MIN: 0, MAX: 1},
            {ID: 'CTA', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'COM', MIN: 0, MAX: 5},
            ]},
        ]},
        {ID: 'FNS', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'REL', MIN: 0, MAX: 9999, LEVEL: [
                {ID: 'ARR', MIN: 0, MAX: 1},
                {ID: 'IDE', MIN: 0, MAX: 99},
            ]},
        ]},
        {ID: 'FNT', MIN: 0, MAX: 9999, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 9999},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

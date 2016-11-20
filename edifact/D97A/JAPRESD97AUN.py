#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD97AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 2},
    {ID: 'PNA', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'ADR', MIN: 0, MAX: 1},
        {ID: 'LOC', MIN: 0, MAX: 5},
        {ID: 'DTM', MIN: 0, MAX: 5},
        {ID: 'CTA', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'RFF', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 5},
    ]},
    {ID: 'GIS', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'FTX', MIN: 0, MAX: 1},
    ]},
    {ID: 'UNS', MIN: 1, MAX: 1},
    {ID: 'RFF', MIN: 1, MAX: 999, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 5},
        {ID: 'FTX', MIN: 0, MAX: 5},
        {ID: 'PNA', MIN: 1, MAX: 1, LEVEL: [
            {ID: 'ADR', MIN: 0, MAX: 5},
            {ID: 'DTM', MIN: 0, MAX: 1},
            {ID: 'LOC', MIN: 0, MAX: 5},
            {ID: 'NAT', MIN: 0, MAX: 9},
            {ID: 'PDI', MIN: 0, MAX: 1},
            {ID: 'DOC', MIN: 0, MAX: 9},
        ]},
        {ID: 'RFF', MIN: 1, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 5},
        ]},
        {ID: 'GIS', MIN: 1, MAX: 5, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 1},
        ]},
        {ID: 'EMP', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'LOC', MIN: 0, MAX: 1},
            {ID: 'GIS', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'FTX', MIN: 0, MAX: 1},
            ]},
            {ID: 'ATT', MIN: 0, MAX: 20, LEVEL: [
                {ID: 'FTX', MIN: 0, MAX: 1},
                {ID: 'PTY', MIN: 0, MAX: 1},
            ]},
            {ID: 'LAN', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'GIS', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'SAL', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 2},
            {ID: 'ATT', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'FTX', MIN: 0, MAX: 1},
            ]},
            {ID: 'GIS', MIN: 0, MAX: 2, LEVEL: [
                {ID: 'FTX', MIN: 0, MAX: 1},
            ]},
            {ID: 'MOA', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'RNG', MIN: 0, MAX: 1},
                {ID: 'FTX', MIN: 0, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

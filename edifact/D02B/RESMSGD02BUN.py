#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD02BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'LAN', MIN: 0, MAX: 1},
    {ID: 'PCD', MIN: 0, MAX: 1},
    {ID: 'PAI', MIN: 0, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 5},
    {ID: 'FTX', MIN: 0, MAX: 5},
    {ID: 'LOC', MIN: 0, MAX: 2},
    {ID: 'MOA', MIN: 0, MAX: 5},
    {ID: 'PYT', MIN: 0, MAX: 10},
    {ID: 'FII', MIN: 0, MAX: 5},
    {ID: 'RFF', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'NAD', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 5},
        {ID: 'COM', MIN: 0, MAX: 5},
        {ID: 'LAN', MIN: 0, MAX: 1},
        {ID: 'CTA', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 5},
            {ID: 'LAN', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'SEQ', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'IMD', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'QTY', MIN: 0, MAX: 1},
            {ID: 'LAN', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 20},
            {ID: 'NAD', MIN: 0, MAX: 1},
            {ID: 'RFF', MIN: 0, MAX: 99},
            {ID: 'PCD', MIN: 0, MAX: 1},
            {ID: 'PAI', MIN: 0, MAX: 1},
            {ID: 'PYT', MIN: 0, MAX: 5},
            {ID: 'FII', MIN: 0, MAX: 5},
            {ID: 'DIM', MIN: 0, MAX: 2},
            {ID: 'FTX', MIN: 0, MAX: 5},
            {ID: 'LOC', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'NAD', MIN: 0, MAX: 1},
                {ID: 'DTM', MIN: 0, MAX: 10},
            ]},
            {ID: 'MOA', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'QTY', MIN: 0, MAX: 1},
            ]},
            {ID: 'RCS', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'FII', MIN: 0, MAX: 5},
                {ID: 'MOA', MIN: 0, MAX: 2},
                {ID: 'RFF', MIN: 0, MAX: 1},
                {ID: 'FTX', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'MEM', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'NAD', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'ATT', MIN: 0, MAX: 99},
                {ID: 'RFF', MIN: 0, MAX: 99},
                {ID: 'LAN', MIN: 0, MAX: 1},
                {ID: 'FTX', MIN: 0, MAX: 5},
                {ID: 'COM', MIN: 0, MAX: 5},
                {ID: 'CTA', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'COM', MIN: 0, MAX: 5},
                ]},
                {ID: 'DOC', MIN: 0, MAX: 5, LEVEL: [
                    {ID: 'LOC', MIN: 0, MAX: 1},
                    {ID: 'DTM', MIN: 0, MAX: 10},
                ]},
                {ID: 'PAI', MIN: 0, MAX: 10, LEVEL: [
                    {ID: 'PYT', MIN: 0, MAX: 1},
                    {ID: 'FII', MIN: 0, MAX: 1},
                    {ID: 'MOA', MIN: 0, MAX: 1},
                    {ID: 'RFF', MIN: 0, MAX: 9},
                ]},
                {ID: 'RCS', MIN: 0, MAX: 10, LEVEL: [
                    {ID: 'MOA', MIN: 0, MAX: 2},
                    {ID: 'RFF', MIN: 0, MAX: 2},
                    {ID: 'FTX', MIN: 0, MAX: 1},
                ]},
            ]},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

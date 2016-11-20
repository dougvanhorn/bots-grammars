#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD01CUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 9},
    {ID: 'LOC', MIN: 0, MAX: 9},
    {ID: 'QTY', MIN: 0, MAX: 9},
    {ID: 'RFF', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'NAD', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'FTX', MIN: 0, MAX: 9},
    {ID: 'TDT', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'LOC', MIN: 0, MAX: 99},
        {ID: 'DTM', MIN: 0, MAX: 99},
    ]},
    {ID: 'GIS', MIN: 0, MAX: 9},
    {ID: 'EQD', MIN: 0, MAX: 9999, LEVEL: [
        {ID: 'TSR', MIN: 0, MAX: 9},
        {ID: 'MEA', MIN: 0, MAX: 9},
        {ID: 'DIM', MIN: 0, MAX: 9},
        {ID: 'SEL', MIN: 0, MAX: 9},
        {ID: 'NAD', MIN: 0, MAX: 9},
        {ID: 'GIS', MIN: 0, MAX: 9},
        {ID: 'LOC', MIN: 0, MAX: 1},
        {ID: 'TMP', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'RNG', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'CNT', MIN: 0, MAX: 9},
    {ID: 'CNI', MIN: 0, MAX: 9999, LEVEL: [
        {ID: 'CNT', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9999, LEVEL: [
            {ID: 'CNT', MIN: 0, MAX: 9},
            {ID: 'MOA', MIN: 0, MAX: 9},
            {ID: 'LOC', MIN: 0, MAX: 99},
            {ID: 'GIS', MIN: 0, MAX: 9},
            {ID: 'CUX', MIN: 0, MAX: 9},
            {ID: 'CPI', MIN: 0, MAX: 9},
            {ID: 'TDT', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'LOC', MIN: 0, MAX: 9},
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'MEA', MIN: 0, MAX: 9},
                {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'TSR', MIN: 0, MAX: 9},
                ]},
            ]},
            {ID: 'NAD', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'RFF', MIN: 0, MAX: 9},
                {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'COM', MIN: 0, MAX: 9},
                ]},
            ]},
            {ID: 'QTY', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'FTX', MIN: 0, MAX: 9},
            ]},
            {ID: 'GID', MIN: 1, MAX: 9999, LEVEL: [
                {ID: 'PAC', MIN: 0, MAX: 9},
                {ID: 'HAN', MIN: 0, MAX: 9},
                {ID: 'FTX', MIN: 0, MAX: 99},
                {ID: 'MEA', MIN: 0, MAX: 99},
                {ID: 'MOA', MIN: 0, MAX: 9},
                {ID: 'SGP', MIN: 0, MAX: 9999},
                {ID: 'DGS', MIN: 0, MAX: 9},
                {ID: 'PCI', MIN: 0, MAX: 9},
                {ID: 'CST', MIN: 0, MAX: 1},
                {ID: 'LOC', MIN: 0, MAX: 9},
                {ID: 'TMD', MIN: 0, MAX: 9},
                {ID: 'GIS', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 9},
                    {ID: 'DOC', MIN: 0, MAX: 9},
                    {ID: 'PAC', MIN: 0, MAX: 9},
                    {ID: 'MEA', MIN: 0, MAX: 9},
                ]},
                {ID: 'QTY', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'FTX', MIN: 0, MAX: 1},
                ]},
            ]},
        ]},
    ]},
    {ID: 'AUT', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

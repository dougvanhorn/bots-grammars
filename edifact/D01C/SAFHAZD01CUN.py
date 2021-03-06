#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD01CUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'RFF', MIN: 0, MAX: 10},
    {ID: 'DTM', MIN: 0, MAX: 10},
    {ID: 'FTX', MIN: 0, MAX: 99},
    {ID: 'NAD', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 10},
        {ID: 'CTA', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'DOC', MIN: 1, MAX: 1000, LEVEL: [
        {ID: 'IMD', MIN: 0, MAX: 999},
        {ID: 'PIA', MIN: 0, MAX: 10},
        {ID: 'MEA', MIN: 0, MAX: 10},
        {ID: 'RCS', MIN: 0, MAX: 10},
        {ID: 'RFF', MIN: 0, MAX: 10},
        {ID: 'DTM', MIN: 0, MAX: 10},
        {ID: 'FTX', MIN: 0, MAX: 99},
        {ID: 'NAD', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'RFF', MIN: 0, MAX: 10},
            {ID: 'CTA', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'COM', MIN: 0, MAX: 5},
            ]},
        ]},
        {ID: 'SFI', MIN: 0, MAX: 20, LEVEL: [
            {ID: 'PIA', MIN: 0, MAX: 10},
            {ID: 'EQD', MIN: 0, MAX: 99},
            {ID: 'FTX', MIN: 0, MAX: 99},
            {ID: 'NAD', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'RFF', MIN: 0, MAX: 10},
                {ID: 'CTA', MIN: 0, MAX: 10, LEVEL: [
                    {ID: 'COM', MIN: 0, MAX: 5},
                ]},
            ]},
            {ID: 'HAN', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'FTX', MIN: 0, MAX: 99},
            ]},
            {ID: 'IMD', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'MEA', MIN: 0, MAX: 10},
                {ID: 'PCD', MIN: 0, MAX: 10},
                {ID: 'RFF', MIN: 0, MAX: 10},
                {ID: 'FTX', MIN: 0, MAX: 99},
            ]},
            {ID: 'DGS', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'RFF', MIN: 0, MAX: 10},
                {ID: 'FTX', MIN: 0, MAX: 99},
                {ID: 'PAC', MIN: 0, MAX: 10, LEVEL: [
                    {ID: 'PCI', MIN: 0, MAX: 10},
                ]},
            ]},
            {ID: 'CCI', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'IMD', MIN: 0, MAX: 10},
                {ID: 'FTX', MIN: 0, MAX: 99},
                {ID: 'CAV', MIN: 0, MAX: 10},
                {ID: 'RFF', MIN: 0, MAX: 10, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 10},
                ]},
                {ID: 'MEA', MIN: 0, MAX: 10, LEVEL: [
                    {ID: 'TEM', MIN: 0, MAX: 10},
                    {ID: 'DTM', MIN: 0, MAX: 10},
                    {ID: 'RFF', MIN: 0, MAX: 10},
                    {ID: 'FTX', MIN: 0, MAX: 99},
                ]},
            ]},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

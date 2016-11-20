#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD97AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 5},
    {ID: 'RFF', MIN: 0, MAX: 1},
    {ID: 'FTX', MIN: 0, MAX: 99},
    {ID: 'NAD', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'DOC', MIN: 1, MAX: 999, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 5},
        {ID: 'STS', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 5},
            {ID: 'PCD', MIN: 0, MAX: 1},
            {ID: 'QTY', MIN: 0, MAX: 1},
            {ID: 'NAD', MIN: 0, MAX: 1},
        ]},
        {ID: 'LIN', MIN: 0, MAX: 999999, LEVEL: [
            {ID: 'PIA', MIN: 0, MAX: 99},
            {ID: 'IMD', MIN: 0, MAX: 99},
            {ID: 'MEA', MIN: 0, MAX: 5},
            {ID: 'GIN', MIN: 0, MAX: 99},
            {ID: 'RCS', MIN: 0, MAX: 5},
            {ID: 'FTX', MIN: 0, MAX: 99},
            {ID: 'RFF', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 1},
            ]},
            {ID: 'STS', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 5},
                {ID: 'PCD', MIN: 0, MAX: 1},
                {ID: 'QTY', MIN: 0, MAX: 1},
                {ID: 'NAD', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'RFF', MIN: 0, MAX: 5},
                    {ID: 'CTA', MIN: 0, MAX: 5, LEVEL: [
                        {ID: 'COM', MIN: 0, MAX: 5},
                    ]},
                ]},
                {ID: 'TDT', MIN: 0, MAX: 5, LEVEL: [
                    {ID: 'LOC', MIN: 0, MAX: 1},
                ]},
                {ID: 'TOD', MIN: 0, MAX: 5, LEVEL: [
                    {ID: 'LOC', MIN: 0, MAX: 1},
                ]},
                {ID: 'EQD', MIN: 0, MAX: 5, LEVEL: [
                    {ID: 'HAN', MIN: 0, MAX: 5},
                ]},
                {ID: 'PAC', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'QTY', MIN: 0, MAX: 1},
                    {ID: 'PCI', MIN: 0, MAX: 10, LEVEL: [
                        {ID: 'RFF', MIN: 0, MAX: 99},
                    ]},
                ]},
            ]},
            {ID: 'SCC', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'LOC', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 5},
                    {ID: 'QTY', MIN: 0, MAX: 1},
                    {ID: 'STS', MIN: 0, MAX: 99, LEVEL: [
                        {ID: 'DTM', MIN: 0, MAX: 5},
                        {ID: 'PCD', MIN: 0, MAX: 1},
                        {ID: 'QTY', MIN: 0, MAX: 1},
                        {ID: 'NAD', MIN: 0, MAX: 1},
                    ]},
                ]},
            ]},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

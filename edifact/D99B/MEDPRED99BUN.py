#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD99BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 9},
    {ID: 'FTX', MIN: 0, MAX: 9},
    {ID: 'SEQ', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'PNA', MIN: 0, MAX: 9},
        {ID: 'IDE', MIN: 0, MAX: 9},
        {ID: 'SPR', MIN: 0, MAX: 9},
        {ID: 'QUA', MIN: 0, MAX: 9},
        {ID: 'EMP', MIN: 0, MAX: 1},
        {ID: 'ADR', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 1},
        {ID: 'DOC', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'ATT', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'PNA', MIN: 0, MAX: 9},
        {ID: 'PDI', MIN: 0, MAX: 1},
        {ID: 'IDE', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 2},
        {ID: 'NAT', MIN: 0, MAX: 1},
        {ID: 'AGR', MIN: 0, MAX: 9},
        {ID: 'CCI', MIN: 0, MAX: 2},
        {ID: 'STS', MIN: 0, MAX: 1},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'LAN', MIN: 0, MAX: 1},
        {ID: 'CAV', MIN: 0, MAX: 1},
        {ID: 'HAN', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 2},
        ]},
        {ID: 'ADR', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
        {ID: 'REL', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'PNA', MIN: 1, MAX: 9},
            {ID: 'PDI', MIN: 0, MAX: 1},
            {ID: 'ADR', MIN: 0, MAX: 1},
            {ID: 'COM', MIN: 0, MAX: 9},
            {ID: 'LAN', MIN: 0, MAX: 1},
            {ID: 'CAV', MIN: 0, MAX: 1},
        ]},
        {ID: 'LIN', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'CIN', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'PNA', MIN: 0, MAX: 9},
            {ID: 'LAN', MIN: 0, MAX: 1},
            {ID: 'FTX', MIN: 0, MAX: 99},
            {ID: 'RSL', MIN: 0, MAX: 1},
            {ID: 'CLI', MIN: 0, MAX: 9},
            {ID: 'CCI', MIN: 0, MAX: 9},
            {ID: 'IMD', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'STS', MIN: 1, MAX: 1},
                {ID: 'DSG', MIN: 0, MAX: 9},
                {ID: 'INP', MIN: 0, MAX: 9},
                {ID: 'FTX', MIN: 0, MAX: 9},
                {ID: 'SCC', MIN: 0, MAX: 9},
                {ID: 'QTY', MIN: 0, MAX: 9},
            ]},
        ]},
    ]},
    {ID: 'GIS', MIN: 1, MAX: 1, LEVEL: [
        {ID: 'IDE', MIN: 1, MAX: 9},
        {ID: 'DTM', MIN: 1, MAX: 9},
        {ID: 'PTY', MIN: 0, MAX: 1},
        {ID: 'AGR', MIN: 0, MAX: 1},
        {ID: 'LAN', MIN: 0, MAX: 1},
        {ID: 'STS', MIN: 0, MAX: 1},
        {ID: 'FTX', MIN: 0, MAX: 99},
        {ID: 'DOC', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'IDE', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 1},
        ]},
        {ID: 'TOD', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'TDT', MIN: 0, MAX: 1},
            {ID: 'FTX', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'ADR', MIN: 0, MAX: 1},
            {ID: 'COM', MIN: 0, MAX: 9},
            {ID: 'PNA', MIN: 0, MAX: 9},
            {ID: 'PTY', MIN: 0, MAX: 1},
            {ID: 'PAC', MIN: 0, MAX: 1},
        ]},
        {ID: 'FCA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'PNA', MIN: 0, MAX: 9},
            {ID: 'IDE', MIN: 0, MAX: 9},
            {ID: 'RCS', MIN: 0, MAX: 9},
            {ID: 'ICD', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'ALC', MIN: 0, MAX: 9},
                {ID: 'PCD', MIN: 0, MAX: 1},
                {ID: 'MOA', MIN: 0, MAX: 9},
                {ID: 'IDE', MIN: 0, MAX: 9},
                {ID: 'DTM', MIN: 0, MAX: 9},
            ]},
        ]},
        {ID: 'LIN', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DSG', MIN: 0, MAX: 9},
            {ID: 'IMD', MIN: 1, MAX: 1},
            {ID: 'QTY', MIN: 0, MAX: 9},
            {ID: 'PGI', MIN: 0, MAX: 9},
            {ID: 'PNA', MIN: 0, MAX: 9},
            {ID: 'PAC', MIN: 0, MAX: 1},
            {ID: 'IDE', MIN: 0, MAX: 9},
            {ID: 'DLM', MIN: 0, MAX: 9},
            {ID: 'EQN', MIN: 0, MAX: 1},
            {ID: 'PRC', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'STS', MIN: 0, MAX: 1},
            {ID: 'CIN', MIN: 0, MAX: 99},
            {ID: 'FTX', MIN: 0, MAX: 99},
            {ID: 'CAV', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'IMD', MIN: 1, MAX: 1},
                {ID: 'QTY', MIN: 0, MAX: 9},
                {ID: 'FTX', MIN: 0, MAX: 99},
            ]},
            {ID: 'SEQ', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'DSG', MIN: 0, MAX: 9},
                {ID: 'QTY', MIN: 0, MAX: 9},
                {ID: 'INP', MIN: 0, MAX: 9},
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'FTX', MIN: 0, MAX: 9},
                {ID: 'SCC', MIN: 0, MAX: 9},
                {ID: 'CIN', MIN: 0, MAX: 9},
                {ID: 'PCI', MIN: 0, MAX: 9},
                {ID: 'LAN', MIN: 0, MAX: 1},
                {ID: 'EQA', MIN: 0, MAX: 9},
            ]},
            {ID: 'FCA', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'PNA', MIN: 0, MAX: 9},
                {ID: 'IDE', MIN: 0, MAX: 9},
                {ID: 'RCS', MIN: 0, MAX: 9},
                {ID: 'ICD', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'ALC', MIN: 0, MAX: 9},
                    {ID: 'PCD', MIN: 0, MAX: 1},
                    {ID: 'MOA', MIN: 0, MAX: 9},
                    {ID: 'IDE', MIN: 0, MAX: 9},
                    {ID: 'DTM', MIN: 0, MAX: 9},
                ]},
            ]},
        ]},
    ]},
    {ID: 'CNT', MIN: 0, MAX: 1},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

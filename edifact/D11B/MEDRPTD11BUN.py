#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD11BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 9},
    {ID: 'FTX', MIN: 0, MAX: 9},
    {ID: 'PNA', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'ADR', MIN: 0, MAX: 9},
        {ID: 'COM', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'SEQ', MIN: 0, MAX: 1},
        {ID: 'LAN', MIN: 0, MAX: 9},
        {ID: 'SPR', MIN: 0, MAX: 1},
        {ID: 'QUA', MIN: 0, MAX: 9},
        {ID: 'EMP', MIN: 0, MAX: 9},
    ]},
    {ID: 'IRQ', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'GEI', MIN: 1, MAX: 1},
        {ID: 'RFF', MIN: 1, MAX: 9},
        {ID: 'DTM', MIN: 1, MAX: 1},
        {ID: 'STS', MIN: 0, MAX: 1},
        {ID: 'PTY', MIN: 0, MAX: 1},
        {ID: 'LAN', MIN: 0, MAX: 1},
        {ID: 'FTX', MIN: 0, MAX: 99},
        {ID: 'TEM', MIN: 0, MAX: 1},
        {ID: 'RFF', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
        ]},
        {ID: 'FCA', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'RFF', MIN: 1, MAX: 9},
            {ID: 'GEI', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'PTY', MIN: 0, MAX: 1},
            {ID: 'CIN', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 9},
            {ID: 'TEM', MIN: 0, MAX: 9},
            {ID: 'DOC', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'RFF', MIN: 1, MAX: 9},
                {ID: 'DTM', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'ATT', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'ADR', MIN: 0, MAX: 9},
            {ID: 'COM', MIN: 0, MAX: 9},
            {ID: 'REL', MIN: 0, MAX: 1},
            {ID: 'IMD', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 9},
            {ID: 'PNA', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'PDI', MIN: 0, MAX: 1},
            {ID: 'NAT', MIN: 0, MAX: 9},
            {ID: 'LAN', MIN: 0, MAX: 9},
            {ID: 'HAN', MIN: 0, MAX: 9},
            {ID: 'CCI', MIN: 0, MAX: 9},
            {ID: 'PAS', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'LOC', MIN: 0, MAX: 9},
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'RFF', MIN: 0, MAX: 1},
            ]},
            {ID: 'CAV', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'CIN', MIN: 0, MAX: 9},
                {ID: 'LAN', MIN: 0, MAX: 9},
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'FTX', MIN: 0, MAX: 99},
                {ID: 'RFF', MIN: 0, MAX: 9},
                {ID: 'STS', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'SEQ', MIN: 0, MAX: 1},
                    {ID: 'GEI', MIN: 0, MAX: 1},
                    {ID: 'RSL', MIN: 0, MAX: 1},
                    {ID: 'CCI', MIN: 1, MAX: 9},
                    {ID: 'CIN', MIN: 0, MAX: 9},
                    {ID: 'DTM', MIN: 0, MAX: 99},
                    {ID: 'FTX', MIN: 0, MAX: 99},
                    {ID: 'RFF', MIN: 0, MAX: 99},
                    {ID: 'RSL', MIN: 0, MAX: 99, LEVEL: [
                        {ID: 'FTX', MIN: 0, MAX: 9},
                        {ID: 'CCI', MIN: 0, MAX: 9},
                    ]},
                    {ID: 'REL', MIN: 0, MAX: 99, LEVEL: [
                        {ID: 'RFF', MIN: 0, MAX: 99},
                    ]},
                ]},
                {ID: 'CLI', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'IMD', MIN: 0, MAX: 99, LEVEL: [
                        {ID: 'DSG', MIN: 0, MAX: 9},
                        {ID: 'FTX', MIN: 0, MAX: 9},
                        {ID: 'INP', MIN: 0, MAX: 9},
                    ]},
                ]},
            ]},
            {ID: 'SEQ', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'IMD', MIN: 1, MAX: 9},
                {ID: 'PRC', MIN: 0, MAX: 9},
                {ID: 'RFF', MIN: 0, MAX: 9},
                {ID: 'QTY', MIN: 0, MAX: 1},
                {ID: 'DTM', MIN: 0, MAX: 99},
                {ID: 'PAC', MIN: 0, MAX: 1},
                {ID: 'FTX', MIN: 0, MAX: 9},
                {ID: 'TDT', MIN: 0, MAX: 9},
                {ID: 'HAN', MIN: 0, MAX: 9},
                {ID: 'LOC', MIN: 0, MAX: 9},
                {ID: 'ADR', MIN: 0, MAX: 9},
                {ID: 'CLI', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'IMD', MIN: 0, MAX: 1},
                    {ID: 'DSG', MIN: 0, MAX: 1},
                    {ID: 'DTM', MIN: 0, MAX: 9},
                    {ID: 'FTX', MIN: 0, MAX: 9},
                    {ID: 'QTY', MIN: 0, MAX: 1},
                    {ID: 'INP', MIN: 0, MAX: 9},
                ]},
            ]},
            {ID: 'LIN', MIN: 1, MAX: 99, LEVEL: [
                {ID: 'GEI', MIN: 1, MAX: 1},
                {ID: 'RSL', MIN: 0, MAX: 1},
                {ID: 'CCI', MIN: 1, MAX: 99},
                {ID: 'CIN', MIN: 0, MAX: 9},
                {ID: 'SEQ', MIN: 0, MAX: 1},
                {ID: 'STS', MIN: 0, MAX: 1},
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'FTX', MIN: 0, MAX: 99},
                {ID: 'MOA', MIN: 0, MAX: 9},
                {ID: 'RFF', MIN: 0, MAX: 99},
                {ID: 'EQD', MIN: 0, MAX: 9},
                {ID: 'REL', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'RFF', MIN: 0, MAX: 99},
                ]},
                {ID: 'RSL', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'FTX', MIN: 0, MAX: 9},
                    {ID: 'CCI', MIN: 0, MAX: 9},
                ]},
            ]},
        ]},
    ]},
    {ID: 'AUT', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

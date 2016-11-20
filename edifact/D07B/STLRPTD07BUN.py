#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD07BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 2},
    {ID: 'NAD', MIN: 1, MAX: 1},
    {ID: 'CUX', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'EQN', MIN: 1, MAX: 1},
        {ID: 'MOA', MIN: 1, MAX: 6},
    ]},
    {ID: 'DTM', MIN: 1, MAX: 9, LEVEL: [
        {ID: 'GEI', MIN: 0, MAX: 1},
        {ID: 'CUX', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'EQN', MIN: 1, MAX: 1},
            {ID: 'MOA', MIN: 1, MAX: 6},
            {ID: 'QVR', MIN: 0, MAX: 1},
        ]},
        {ID: 'RFF', MIN: 1, MAX: 999999, LEVEL: [
            {ID: 'LOC', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 1},
            {ID: 'FTX', MIN: 0, MAX: 9},
            {ID: 'CUX', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'MOA', MIN: 1, MAX: 9},
                {ID: 'QVR', MIN: 0, MAX: 1},
            ]},
            {ID: 'BUS', MIN: 1, MAX: 99, LEVEL: [
                {ID: 'CUX', MIN: 0, MAX: 999, LEVEL: [
                    {ID: 'MOA', MIN: 1, MAX: 9},
                    {ID: 'QVR', MIN: 0, MAX: 1},
                ]},
                {ID: 'LIN', MIN: 1, MAX: 99999, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 1},
                    {ID: 'RFF', MIN: 0, MAX: 9},
                    {ID: 'NAD', MIN: 0, MAX: 9},
                    {ID: 'LOC', MIN: 0, MAX: 1},
                    {ID: 'CUX', MIN: 0, MAX: 1},
                    {ID: 'GEI', MIN: 0, MAX: 2},
                    {ID: 'IMD', MIN: 0, MAX: 9},
                    {ID: 'MOA', MIN: 0, MAX: 9},
                    {ID: 'ALC', MIN: 0, MAX: 9},
                    {ID: 'FTX', MIN: 0, MAX: 99},
                    {ID: 'TAX', MIN: 0, MAX: 999},
                    {ID: 'DOC', MIN: 0, MAX: 99, LEVEL: [
                        {ID: 'DTM', MIN: 1, MAX: 1},
                        {ID: 'FTX', MIN: 0, MAX: 1},
                        {ID: 'PIA', MIN: 0, MAX: 1},
                        {ID: 'SEQ', MIN: 0, MAX: 1},
                    ]},
                    {ID: 'PYT', MIN: 0, MAX: 9999, LEVEL: [
                        {ID: 'MOA', MIN: 0, MAX: 9},
                        {ID: 'RFF', MIN: 0, MAX: 9},
                        {ID: 'DTM', MIN: 0, MAX: 2},
                        {ID: 'AGR', MIN: 0, MAX: 1},
                        {ID: 'GEI', MIN: 0, MAX: 2},
                        {ID: 'NAD', MIN: 0, MAX: 1},
                        {ID: 'FTX', MIN: 0, MAX: 9},
                        {ID: 'IMD', MIN: 0, MAX: 2},
                    ]},
                    {ID: 'GIR', MIN: 0, MAX: 999, LEVEL: [
                        {ID: 'IMD', MIN: 0, MAX: 2},
                        {ID: 'GIN', MIN: 0, MAX: 2},
                        {ID: 'SEQ', MIN: 0, MAX: 99, LEVEL: [
                            {ID: 'FTX', MIN: 0, MAX: 99},
                            {ID: 'ALC', MIN: 0, MAX: 1},
                            {ID: 'GIN', MIN: 0, MAX: 1},
                            {ID: 'RFF', MIN: 0, MAX: 2},
                            {ID: 'IMD', MIN: 0, MAX: 9},
                            {ID: 'NAD', MIN: 0, MAX: 1},
                            {ID: 'TDT', MIN: 0, MAX: 1},
                            {ID: 'DTM', MIN: 0, MAX: 9},
                            {ID: 'LOC', MIN: 0, MAX: 9},
                        ]},
                    ]},
                ]},
            ]},
            {ID: 'CNT', MIN: 1, MAX: 1},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

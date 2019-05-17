from bots.botsconfig import *
from records006020 import recorddefs

syntax = {
    'version': '00602',
    'functionalgroup': 'AD',
    }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'DTP', MIN: 0, MAX: 99999},
    {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'N3', MIN: 0, MAX: 3},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 9},
        {ID: 'PER', MIN: 0, MAX: 3},
    ]},
    {ID: 'N1', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 3},
        {ID: 'N3', MIN: 0, MAX: 3},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'N9', MIN: 0, MAX: 99999},
        {ID: 'DTM', MIN: 0, MAX: 99999},
        {ID: 'ACT', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'ASI', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 99999},
            {ID: 'C3', MIN: 0, MAX: 1},
            {ID: 'LUI', MIN: 0, MAX: 99999},
            {ID: 'DTP', MIN: 0, MAX: 99999},
            {ID: 'BLI', MIN: 0, MAX: 1},
            {ID: 'LIN', MIN: 0, MAX: 99999},
            {ID: 'PDL', MIN: 0, MAX: 99999},
            {ID: 'AM1', MIN: 0, MAX: 99999},
            {ID: 'AMT', MIN: 0, MAX: 99999},
            {ID: 'QTY', MIN: 0, MAX: 99999},
            {ID: 'YNQ', MIN: 0, MAX: 99999},
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'LQ', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N4', MIN: 0, MAX: 99999},
                {ID: 'LUI', MIN: 0, MAX: 99999},
            ]},
            {ID: 'SI', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'AMT', MIN: 0, MAX: 99999},
                {ID: 'DTP', MIN: 0, MAX: 99999},
                {ID: 'REF', MIN: 0, MAX: 99999},
                {ID: 'NM1', MIN: 0, MAX: 1},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'MSG', MIN: 0, MAX: 99999},
            ]},
            {ID: 'PID', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'BLI', MIN: 0, MAX: 1},
                {ID: 'SPA', MIN: 0, MAX: 1},
                {ID: 'UD', MIN: 0, MAX: 1},
                {ID: 'AMT', MIN: 0, MAX: 99999},
                {ID: 'AM1', MIN: 0, MAX: 99999},
                {ID: 'PDL', MIN: 0, MAX: 99999},
                {ID: 'QTY', MIN: 0, MAX: 99999},
                {ID: 'DTP', MIN: 0, MAX: 99999},
                {ID: 'MSG', MIN: 0, MAX: 99999},
                {ID: 'INV', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'AM1', MIN: 0, MAX: 99999},
                    {ID: 'DTP', MIN: 0, MAX: 99999},
                    {ID: 'QTY', MIN: 0, MAX: 99999},
                    {ID: 'LIN', MIN: 0, MAX: 2},
                    {ID: 'RPA', MIN: 0, MAX: 99999},
                ]},
                {ID: 'BEN', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'NM1', MIN: 0, MAX: 1},
                    {ID: 'N2', MIN: 0, MAX: 3},
                    {ID: 'N3', MIN: 0, MAX: 3},
                    {ID: 'N4', MIN: 0, MAX: 1},
                    {ID: 'REF', MIN: 0, MAX: 99999},
                    {ID: 'DTP', MIN: 0, MAX: 99999},
                    {ID: 'III', MIN: 0, MAX: 99999},
                    {ID: 'QTY', MIN: 0, MAX: 99999},
                    {ID: 'AMT', MIN: 0, MAX: 99999},
                    {ID: 'LUI', MIN: 0, MAX: 1},
                    {ID: 'MSG', MIN: 0, MAX: 99999},
                ]},
            ]},
            {ID: 'ENT', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'NX1', MIN: 0, MAX: 2},
                {ID: 'REF', MIN: 0, MAX: 99999},
                {ID: 'LIN', MIN: 0, MAX: 9},
                {ID: 'DMG', MIN: 0, MAX: 1},
                {ID: 'DMA', MIN: 0, MAX: 1},
                {ID: 'IND', MIN: 0, MAX: 1},
                {ID: 'LUI', MIN: 0, MAX: 1},
                {ID: 'ERI', MIN: 0, MAX: 1},
                {ID: 'DTP', MIN: 0, MAX: 99999},
                {ID: 'AMT', MIN: 0, MAX: 99999},
                {ID: 'AM1', MIN: 0, MAX: 99999},
                {ID: 'RPA', MIN: 0, MAX: 99999},
                {ID: 'YNQ', MIN: 0, MAX: 99999},
                {ID: 'QTY', MIN: 0, MAX: 99999},
                {ID: 'MSG', MIN: 0, MAX: 99999},
                {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'N2', MIN: 0, MAX: 3},
                    {ID: 'REF', MIN: 0, MAX: 99999},
                    {ID: 'AM1', MIN: 0, MAX: 99999},
                    {ID: 'N3', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'N4', MIN: 0, MAX: 1},
                        {ID: 'COM', MIN: 0, MAX: 9},
                        {ID: 'DTP', MIN: 0, MAX: 99999},
                        {ID: 'QTY', MIN: 0, MAX: 1},
                    ]},
                ]},
                {ID: 'LQ', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'SPA', MIN: 0, MAX: 1},
                    {ID: 'DTP', MIN: 0, MAX: 99999},
                    {ID: 'MSG', MIN: 0, MAX: 99999},
                    {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'N3', MIN: 0, MAX: 3},
                        {ID: 'N4', MIN: 0, MAX: 1},
                        {ID: 'REF', MIN: 0, MAX: 99999},
                        {ID: 'COM', MIN: 0, MAX: 3},
                        {ID: 'LUI', MIN: 0, MAX: 1},
                        {ID: 'DTP', MIN: 0, MAX: 99999},
                        {ID: 'MSG', MIN: 0, MAX: 99999},
                    ]},
                ]},
                {ID: 'BEN', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'NM1', MIN: 0, MAX: 1},
                    {ID: 'N2', MIN: 0, MAX: 3},
                    {ID: 'N3', MIN: 0, MAX: 3},
                    {ID: 'N4', MIN: 0, MAX: 1},
                    {ID: 'REF', MIN: 0, MAX: 99999},
                    {ID: 'DTP', MIN: 0, MAX: 99999},
                    {ID: 'III', MIN: 0, MAX: 99999},
                    {ID: 'QTY', MIN: 0, MAX: 99999},
                    {ID: 'AMT', MIN: 0, MAX: 99999},
                    {ID: 'LUI', MIN: 0, MAX: 1},
                    {ID: 'MSG', MIN: 0, MAX: 99999},
                ]},
                {ID: 'PID', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'BLI', MIN: 0, MAX: 9},
                    {ID: 'SPA', MIN: 0, MAX: 1},
                    {ID: 'AMT', MIN: 0, MAX: 99999},
                    {ID: 'QTY', MIN: 0, MAX: 99999},
                    {ID: 'DTP', MIN: 0, MAX: 99999},
                    {ID: 'YNQ', MIN: 0, MAX: 99999},
                    {ID: 'MSG', MIN: 0, MAX: 99999},
                    {ID: 'PDL', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'REF', MIN: 0, MAX: 99999},
                    ]},
                    {ID: 'INV', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'AM1', MIN: 0, MAX: 99999},
                        {ID: 'DTP', MIN: 0, MAX: 99999},
                        {ID: 'RPA', MIN: 0, MAX: 99999},
                    ]},
                    {ID: 'BEN', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'NM1', MIN: 0, MAX: 1},
                        {ID: 'N2', MIN: 0, MAX: 3},
                        {ID: 'N3', MIN: 0, MAX: 3},
                        {ID: 'N4', MIN: 0, MAX: 1},
                        {ID: 'REF', MIN: 0, MAX: 99999},
                        {ID: 'DTP', MIN: 0, MAX: 99999},
                        {ID: 'III', MIN: 0, MAX: 99999},
                        {ID: 'QTY', MIN: 0, MAX: 99999},
                        {ID: 'AMT', MIN: 0, MAX: 99999},
                        {ID: 'LUI', MIN: 0, MAX: 1},
                        {ID: 'MSG', MIN: 0, MAX: 99999},
                    ]},
                ]},
                {ID: 'UC', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'HL', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'UQS', MIN: 0, MAX: 1},
                        {ID: 'YNQ', MIN: 0, MAX: 99999},
                        {ID: 'NM1', MIN: 0, MAX: 1},
                        {ID: 'N3', MIN: 0, MAX: 3},
                        {ID: 'N4', MIN: 0, MAX: 1},
                        {ID: 'COM', MIN: 0, MAX: 9},
                        {ID: 'DTP', MIN: 0, MAX: 99999},
                        {ID: 'QTY', MIN: 0, MAX: 99999},
                        {ID: 'MSG', MIN: 0, MAX: 99999},
                        {ID: 'AM1', MIN: 0, MAX: 99999},
                        {ID: 'AMT', MIN: 0, MAX: 99999},
                        {ID: 'III', MIN: 0, MAX: 99999},
                        {ID: 'EC', MIN: 0, MAX: 1},
                        {ID: 'EMS', MIN: 0, MAX: 1},
                        {ID: 'EMP', MIN: 0, MAX: 1},
                        {ID: 'PCT', MIN: 0, MAX: 99999},
                        {ID: 'SOI', MIN: 0, MAX: 99999},
                        {ID: 'LIN', MIN: 0, MAX: 2},
                        {ID: 'REF', MIN: 0, MAX: 99999},
                        {ID: 'ASL', MIN: 0, MAX: 99999},
                        {ID: 'TOA', MIN: 0, MAX: 99999},
                        {ID: 'TOV', MIN: 0, MAX: 99999},
                        {ID: 'VEH', MIN: 0, MAX: 99999},
                        {ID: 'CDS', MIN: 0, MAX: 99999},
                        {ID: 'CED', MIN: 0, MAX: 99999},
                        {ID: 'SIN', MIN: 0, MAX: 99999},
                        {ID: 'UCS', MIN: 0, MAX: 99999},
                        {ID: 'FH', MIN: 0, MAX: 99999},
                        {ID: 'SPA', MIN: 0, MAX: 1},
                        {ID: 'MPI', MIN: 0, MAX: 1},
                    ]},
                ]},
            ]},
            {ID: 'PWK', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'NM1', MIN: 0, MAX: 1},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'REF', MIN: 0, MAX: 99999},
                {ID: 'DTP', MIN: 0, MAX: 99999},
                {ID: 'SPA', MIN: 0, MAX: 1},
                {ID: 'EFI', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'BIN', MIN: 1, MAX: 1},
                ]},
            ]},
            {ID: 'LX', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'PDL', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'REF', MIN: 0, MAX: 99999},
                    {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
                        {ID: 'AMT', MIN: 1, MAX: 99999, LEVEL: [
                            {ID: 'N1', MIN: 0, MAX: 1},
                            {ID: 'N3', MIN: 0, MAX: 2},
                            {ID: 'N4', MIN: 0, MAX: 1},
                            {ID: 'LIN', MIN: 0, MAX: 2},
                            {ID: 'DTP', MIN: 0, MAX: 99999},
                            {ID: 'QTY', MIN: 0, MAX: 99999},
                            {ID: 'MSG', MIN: 0, MAX: 99999},
                            {ID: 'AM1', MIN: 0, MAX: 99999, LEVEL: [
                                {ID: 'INV', MIN: 0, MAX: 99999, LEVEL: [
                                    {ID: 'QTY', MIN: 0, MAX: 99999},
                                    {ID: 'DTP', MIN: 0, MAX: 99999},
                                    {ID: 'RPA', MIN: 0, MAX: 99999},
                                ]},
                            ]},
                        ]},
                        {ID: 'LE', MIN: 1, MAX: 1},
                    ]},
                ]},
            ]},
            {ID: 'K2', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'DTP', MIN: 0, MAX: 1},
                {ID: 'NM1', MIN: 0, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]

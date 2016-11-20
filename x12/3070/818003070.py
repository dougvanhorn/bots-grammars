from bots.botsconfig import *
from records003070 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'RP',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BSC', MIN: 1, MAX: 1},
    {ID: 'CUR', MIN: 0, MAX: 1},
    {ID: 'N11', MIN: 1, MAX: 999, LEVEL: [
        {ID: 'REF', MIN: 0, MAX: 5},
        {ID: 'AMT', MIN: 0, MAX: 5},
        {ID: 'LIN', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'PID', MIN: 0, MAX: 5},
            {ID: 'AMT', MIN: 0, MAX: 5},
        ]},
        {ID: 'N1', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'SCD', MIN: 0, MAX: 1},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'SAL', MIN: 0, MAX: 4},
            {ID: 'AMT', MIN: 0, MAX: 10},
            {ID: 'LIN', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'PID', MIN: 0, MAX: 5},
                {ID: 'AMT', MIN: 0, MAX: 5},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]

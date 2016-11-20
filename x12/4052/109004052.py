from bots.botsconfig import *
from records004052 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'VE',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'B4', MIN: 1, MAX: 1},
    {ID: 'N9', MIN: 0, MAX: 30},
    {ID: 'Q2', MIN: 0, MAX: 1},
    {ID: 'V9', MIN: 0, MAX: 10},
    {ID: 'R4', MIN: 1, MAX: 20, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 15},
        {ID: 'V9', MIN: 0, MAX: 10},
        {ID: 'N9', MIN: 0, MAX: 9999, LEVEL: [
            {ID: 'SG', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]

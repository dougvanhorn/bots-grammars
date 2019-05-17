from bots.botsconfig import *
from records006020 import recorddefs

syntax = {
    'version': '00602',
    'functionalgroup': 'RH',
    }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 10},
    {ID: 'SMS', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 2, LEVEL: [
        {ID: 'PI', MIN: 0, MAX: 1},
        {ID: 'CD', MIN: 0, MAX: 50},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]

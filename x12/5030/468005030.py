from bots.botsconfig import *
from records005030 import recorddefs

syntax = {
    'version': '00503',
    'functionalgroup': 'TP',
    }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'DK', MIN: 1, MAX: 1},
    {ID: 'JL', MIN: 1, MAX: 7, LEVEL: [
        {ID: 'K1', MIN: 1, MAX: 100},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]

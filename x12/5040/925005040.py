from bots.botsconfig import *
from records005040 import recorddefs

syntax = {
    'version': '00504',
    'functionalgroup': 'GC',
    }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'F10', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'F02', MIN: 0, MAX: 1},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]

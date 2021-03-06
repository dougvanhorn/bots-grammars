from bots.botsconfig import *
from records006020 import recorddefs

syntax = {
    'version': '00602',
    'functionalgroup': 'WT',
    }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'ZT', MIN: 1, MAX: 255, LEVEL: [
        {ID: 'F9', MIN: 0, MAX: 1},
        {ID: 'D9', MIN: 0, MAX: 1},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]

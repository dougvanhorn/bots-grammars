from bots.botsconfig import *
from records006020 import recorddefs

syntax = {
    'version': '00602',
    'functionalgroup': 'VH',
    }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'VR', MIN: 1, MAX: 1},
    {ID: 'G62', MIN: 1, MAX: 3},
    {ID: 'RT', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'RT1', MIN: 1, MAX: 99},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]

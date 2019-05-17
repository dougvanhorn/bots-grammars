from bots.botsconfig import *
from records005030 import recorddefs

syntax = {
    'version': '00503',
    'functionalgroup': 'GC',
    }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'F11', MIN: 1, MAX: 500, LEVEL: [
        {ID: 'F14', MIN: 0, MAX: 99},
        {ID: 'TRN', MIN: 0, MAX: 1},
        {ID: 'F13', MIN: 0, MAX: 1},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]

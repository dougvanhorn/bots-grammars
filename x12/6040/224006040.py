from bots.botsconfig import *
from records006040 import recorddefs

syntax = {
    'version': '00604',
    'functionalgroup': 'MA',
    }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'CF1', MIN: 1, MAX: 1},
    {ID: 'CF2', MIN: 1, MAX: 9999, LEVEL: [
        {ID: 'L11', MIN: 0, MAX: 99},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]

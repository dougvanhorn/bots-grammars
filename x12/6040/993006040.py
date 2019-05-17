from bots.botsconfig import *
from records006040 import recorddefs

syntax = {
    'version': '00604',
    'functionalgroup': 'NR',
    }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'AK1', MIN: 1, MAX: 1},
    {ID: 'AK2', MIN: 0, MAX: 1},
    {ID: 'SPE', MIN: 0, MAX: 1},
    {ID: 'APE', MIN: 0, MAX: 1},
    {ID: 'S4A', MIN: 0, MAX: 2, LEVEL: [
        {ID: 'SVA', MIN: 0, MAX: 1},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]

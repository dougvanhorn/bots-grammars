from bots.botsconfig import *
from records005030 import recorddefs

syntax = {
    'version': '00503',
    'functionalgroup': 'SN',
    }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'R9', MIN: 1, MAX: 50, LEVEL: [
        {ID: 'PER', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 1, MAX: 10},
        {ID: 'RDD', MIN: 0, MAX: 5},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]

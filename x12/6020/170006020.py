from bots.botsconfig import *
from records006020 import recorddefs

syntax = {
    'version': '00602',
    'functionalgroup': 'ER',
    }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'N1', MIN: 1, MAX: 1},
    {ID: 'PER', MIN: 0, MAX: 1},
    {ID: 'THE', MIN: 1, MAX: 9999, LEVEL: [
        {ID: 'LX', MIN: 1, MAX: 10, LEVEL: [
            {ID: 'REF', MIN: 1, MAX: 10},
            {ID: 'DTM', MIN: 1, MAX: 7, LEVEL: [
                {ID: 'BOX', MIN: 1, MAX: 250},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]

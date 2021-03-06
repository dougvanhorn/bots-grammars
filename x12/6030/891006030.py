from bots.botsconfig import *
from records006030 import recorddefs

syntax = {
    'version': '00603',
    'functionalgroup': 'UD',
    }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 2},
    {ID: 'PER', MIN: 0, MAX: 3},
    {ID: 'ENT', MIN: 1, MAX: 100, LEVEL: [
        {ID: 'N9', MIN: 0, MAX: 100, LEVEL: [
            {ID: 'AMT', MIN: 0, MAX: 1},
            {ID: 'ADX', MIN: 0, MAX: 1000, LEVEL: [
                {ID: 'AMT', MIN: 0, MAX: 1},
                {ID: 'REF', MIN: 0, MAX: 10},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]

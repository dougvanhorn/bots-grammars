from bots.botsconfig import *
from records006030 import recorddefs

syntax = {
    'version': '00603',
    'functionalgroup': 'BB',
    }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'M10', MIN: 1, MAX: 1},
    {ID: 'P4', MIN: 1, MAX: 1, LEVEL: [
        {ID: 'LX', MIN: 1, MAX: 999, LEVEL: [
            {ID: 'M13', MIN: 0, MAX: 1},
            {ID: 'M21', MIN: 0, MAX: 1},
            {ID: 'M12', MIN: 0, MAX: 1},
            {ID: 'N9', MIN: 0, MAX: 1},
            {ID: 'N1', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]

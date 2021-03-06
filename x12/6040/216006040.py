from bots.botsconfig import *
from records006040 import recorddefs

syntax = {
    'version': '00604',
    'functionalgroup': 'PU',
    }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'PUN', MIN: 1, MAX: 1},
    {ID: 'G61', MIN: 0, MAX: 1},
    {ID: 'TEM', MIN: 0, MAX: 1},
    {ID: 'PRF', MIN: 0, MAX: 99999},
    {ID: 'AT5', MIN: 0, MAX: 10},
    {ID: 'K2', MIN: 0, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 2, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]

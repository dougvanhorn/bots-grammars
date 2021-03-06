from bots.botsconfig import *
from records006010 import recorddefs

syntax = {
    'version': '00601',
    'functionalgroup': 'RZ',
    }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'AAA', MIN: 1, MAX: 1},
    {ID: 'REF', MIN: 1, MAX: 10},
    {ID: 'PWK', MIN: 0, MAX: 1},
    {ID: 'NTE', MIN: 0, MAX: 15},
    {ID: 'N1', MIN: 1, MAX: 2, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 1},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 1},
    ]},
    {ID: 'IN1', MIN: 1, MAX: 15, LEVEL: [
        {ID: 'IN2', MIN: 1, MAX: 10},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]

from bots.botsconfig import *
from records006020 import recorddefs

syntax = {
    'version': '00602',
    'functionalgroup': 'SO',
    }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'M10', MIN: 0, MAX: 1},
    {ID: 'P4', MIN: 0, MAX: 20, LEVEL: [
        {ID: 'V9', MIN: 0, MAX: 20},
        {ID: 'VEH', MIN: 0, MAX: 10},
        {ID: 'NM1', MIN: 0, MAX: 9999},
        {ID: 'VID', MIN: 0, MAX: 9999, LEVEL: [
            {ID: 'M7', MIN: 0, MAX: 5},
            {ID: 'M7A', MIN: 0, MAX: 22},
        ]},
        {ID: 'K1', MIN: 0, MAX: 4},
        {ID: 'X4', MIN: 0, MAX: 9999, LEVEL: [
            {ID: 'K1', MIN: 0, MAX: 4},
            {ID: 'N9', MIN: 0, MAX: 999},
            {ID: 'N7', MIN: 0, MAX: 999},
        ]},
    ]},
    {ID: 'BA1', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'X4', MIN: 0, MAX: 9999, LEVEL: [
            {ID: 'K1', MIN: 0, MAX: 4},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]

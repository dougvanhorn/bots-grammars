from bots.botsconfig import *
from records006020 import recorddefs

syntax = {
    'version': '00602',
    'functionalgroup': 'RE',
    }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'W17', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 10, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 5},
    ]},
    {ID: 'N9', MIN: 0, MAX: 10},
    {ID: 'G61', MIN: 0, MAX: 3},
    {ID: 'G62', MIN: 0, MAX: 5},
    {ID: 'NTE', MIN: 0, MAX: 20},
    {ID: 'W08', MIN: 0, MAX: 1},
    {ID: 'W18', MIN: 0, MAX: 10},
    {ID: 'G08', MIN: 0, MAX: 2},
    {ID: 'TD1', MIN: 0, MAX: 5},
    {ID: 'LX', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'MAN', MIN: 0, MAX: 1},
        {ID: 'PAL', MIN: 0, MAX: 99999},
        {ID: 'N9', MIN: 0, MAX: 5},
        {ID: 'W07', MIN: 0, MAX: 9999, LEVEL: [
            {ID: 'G69', MIN: 0, MAX: 5},
            {ID: 'N9', MIN: 0, MAX: 99999},
            {ID: 'W20', MIN: 0, MAX: 2},
            {ID: 'W13', MIN: 0, MAX: 50, LEVEL: [
                {ID: 'N9', MIN: 0, MAX: 200},
            ]},
        ]},
    ]},
    {ID: 'W14', MIN: 1, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]

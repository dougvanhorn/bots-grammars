from bots.botsconfig import *
from records006030 import recorddefs

syntax = {
    'version': '00603',
    'functionalgroup': 'HN',
    }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BHT', MIN: 1, MAX: 1},
    {ID: 'REF', MIN: 0, MAX: 10},
    {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 2},
        {ID: 'PER', MIN: 0, MAX: 1},
    ]},
    {ID: 'HL', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'SBR', MIN: 0, MAX: 1},
        {ID: 'PAT', MIN: 0, MAX: 1},
        {ID: 'DMG', MIN: 0, MAX: 1},
        {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'PER', MIN: 0, MAX: 1},
        ]},
        {ID: 'TRN', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'STC', MIN: 0, MAX: 99999},
            {ID: 'REF', MIN: 0, MAX: 9},
            {ID: 'DTP', MIN: 0, MAX: 2},
            {ID: 'QTY', MIN: 0, MAX: 5},
            {ID: 'AMT', MIN: 0, MAX: 5},
            {ID: 'PWK', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'PER', MIN: 0, MAX: 1},
                {ID: 'N1', MIN: 0, MAX: 1},
                {ID: 'N3', MIN: 0, MAX: 1},
                {ID: 'N4', MIN: 0, MAX: 1},
            ]},
            {ID: 'SVC', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'STC', MIN: 0, MAX: 99999},
                {ID: 'REF', MIN: 0, MAX: 9},
                {ID: 'DTP', MIN: 0, MAX: 1},
                {ID: 'TOO', MIN: 0, MAX: 99999},
                {ID: 'PWK', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'PER', MIN: 0, MAX: 1},
                    {ID: 'N1', MIN: 0, MAX: 1},
                    {ID: 'N3', MIN: 0, MAX: 1},
                    {ID: 'N4', MIN: 0, MAX: 1},
                ]},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]

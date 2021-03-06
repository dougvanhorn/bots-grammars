from bots.botsconfig import *
from records006030 import recorddefs

syntax = {
    'version': '00603',
    'functionalgroup': 'BL',
    }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BOL', MIN: 1, MAX: 1},
    {ID: 'B2A', MIN: 1, MAX: 1},
    {ID: 'MS3', MIN: 0, MAX: 12},
    {ID: 'MS2', MIN: 0, MAX: 1},
    {ID: 'L11', MIN: 0, MAX: 100},
    {ID: 'G62', MIN: 0, MAX: 6},
    {ID: 'AT5', MIN: 0, MAX: 50},
    {ID: 'K1', MIN: 0, MAX: 10},
    {ID: 'N1', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 1},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'G61', MIN: 0, MAX: 3},
    ]},
    {ID: 'AT1', MIN: 1, MAX: 9999, LEVEL: [
        {ID: 'L11', MIN: 0, MAX: 100},
        {ID: 'AT3', MIN: 0, MAX: 1},
        {ID: 'AT4', MIN: 0, MAX: 99},
        {ID: 'AT2', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'MAN', MIN: 0, MAX: 999999},
            {ID: 'OID', MIN: 0, MAX: 999999},
            {ID: 'L4', MIN: 0, MAX: 1},
        ]},
        {ID: 'LX', MIN: 0, MAX: 999999, LEVEL: [
            {ID: 'MAN', MIN: 0, MAX: 999999},
            {ID: 'OID', MIN: 0, MAX: 999999},
        ]},
        {ID: 'G61', MIN: 0, MAX: 2, LEVEL: [
            {ID: 'L11', MIN: 0, MAX: 5},
            {ID: 'LH6', MIN: 0, MAX: 6},
            {ID: 'LH1', MIN: 1, MAX: 25, LEVEL: [
                {ID: 'LH2', MIN: 0, MAX: 4},
                {ID: 'LH3', MIN: 0, MAX: 10},
                {ID: 'LFH', MIN: 0, MAX: 20},
                {ID: 'LEP', MIN: 0, MAX: 3},
                {ID: 'LH4', MIN: 0, MAX: 1},
                {ID: 'LHT', MIN: 0, MAX: 3},
                {ID: 'L11', MIN: 0, MAX: 5},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]

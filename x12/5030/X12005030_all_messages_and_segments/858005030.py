from bots.botsconfig import *
from records005030 import recorddefs

syntax = {
    'version': '00503',
    'functionalgroup': 'SI',
    }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'ZC1', MIN: 0, MAX: 1},
    {ID: 'BX', MIN: 1, MAX: 1},
    {ID: 'BNX', MIN: 0, MAX: 1},
    {ID: 'M3', MIN: 0, MAX: 1},
    {ID: 'N9', MIN: 0, MAX: 30},
    {ID: 'CM', MIN: 0, MAX: 3},
    {ID: 'Y6', MIN: 0, MAX: 4},
    {ID: 'Y7', MIN: 0, MAX: 1},
    {ID: 'C3', MIN: 0, MAX: 1},
    {ID: 'ITD', MIN: 0, MAX: 1},
    {ID: 'G62', MIN: 0, MAX: 10},
    {ID: 'PER', MIN: 0, MAX: 3},
    {ID: 'NA', MIN: 0, MAX: 999},
    {ID: 'F9', MIN: 0, MAX: 1},
    {ID: 'D9', MIN: 0, MAX: 1},
    {ID: 'R1', MIN: 0, MAX: 1},
    {ID: 'R2', MIN: 0, MAX: 13},
    {ID: 'R3', MIN: 0, MAX: 13},
    {ID: 'R4', MIN: 0, MAX: 5},
    {ID: 'MEA', MIN: 0, MAX: 10},
    {ID: 'H3', MIN: 0, MAX: 20},
    {ID: 'PS', MIN: 0, MAX: 5},
    {ID: 'H6', MIN: 0, MAX: 6},
    {ID: 'V4', MIN: 0, MAX: 1},
    {ID: 'V5', MIN: 0, MAX: 1},
    {ID: 'E1', MIN: 0, MAX: 2, LEVEL: [
        {ID: 'E4', MIN: 0, MAX: 1},
        {ID: 'E5', MIN: 0, MAX: 13},
        {ID: 'PI', MIN: 0, MAX: 1},
    ]},
    {ID: 'M1', MIN: 0, MAX: 1},
    {ID: 'M2', MIN: 0, MAX: 1},
    {ID: 'L7', MIN: 0, MAX: 30},
    {ID: 'NTE', MIN: 0, MAX: 50},
    {ID: 'XH', MIN: 0, MAX: 1},
    {ID: 'N7', MIN: 0, MAX: 600, LEVEL: [
        {ID: 'EM', MIN: 0, MAX: 1},
        {ID: 'NA', MIN: 0, MAX: 30},
        {ID: 'M7', MIN: 0, MAX: 5},
        {ID: 'N5', MIN: 0, MAX: 1},
        {ID: 'G62', MIN: 0, MAX: 2},
        {ID: 'REF', MIN: 0, MAX: 5},
        {ID: 'IC', MIN: 0, MAX: 1},
        {ID: 'VC', MIN: 0, MAX: 36},
        {ID: 'GA', MIN: 0, MAX: 15},
        {ID: 'E1', MIN: 0, MAX: 2, LEVEL: [
            {ID: 'E4', MIN: 0, MAX: 1},
            {ID: 'E5', MIN: 0, MAX: 13},
            {ID: 'PI', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'N1', MIN: 0, MAX: 12, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'PER', MIN: 0, MAX: 3},
        {ID: 'H3', MIN: 0, MAX: 5},
    ]},
    {ID: 'S5', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'G62', MIN: 0, MAX: 6},
        {ID: 'N9', MIN: 0, MAX: 10},
        {ID: 'H6', MIN: 0, MAX: 6},
        {ID: 'N1', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 12},
            {ID: 'PER', MIN: 0, MAX: 3},
        ]},
    ]},
    {ID: 'FA1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'FA2', MIN: 1, MAX: 99999},
        {ID: 'L10', MIN: 0, MAX: 1},
    ]},
    {ID: 'HL', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N7', MIN: 0, MAX: 1},
        {ID: 'NA', MIN: 0, MAX: 1},
        {ID: 'M7', MIN: 0, MAX: 5},
        {ID: 'N5', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 5},
        {ID: 'IC', MIN: 0, MAX: 1},
        {ID: 'VC', MIN: 0, MAX: 36},
        {ID: 'L7', MIN: 0, MAX: 10},
        {ID: 'SL1', MIN: 0, MAX: 1},
        {ID: 'N9', MIN: 0, MAX: 10},
        {ID: 'H3', MIN: 0, MAX: 1},
        {ID: 'X1', MIN: 0, MAX: 6},
        {ID: 'X2', MIN: 0, MAX: 1},
        {ID: 'L5', MIN: 0, MAX: 10},
        {ID: 'PER', MIN: 0, MAX: 5},
        {ID: 'LH2', MIN: 0, MAX: 6},
        {ID: 'LHR', MIN: 0, MAX: 1},
        {ID: 'LH6', MIN: 0, MAX: 10},
        {ID: 'Y7', MIN: 0, MAX: 2},
        {ID: 'G62', MIN: 0, MAX: 10},
        {ID: 'NTE', MIN: 0, MAX: 100},
        {ID: 'LP', MIN: 0, MAX: 1},
        {ID: 'AXL', MIN: 0, MAX: 12},
        {ID: 'L0', MIN: 0, MAX: 20, LEVEL: [
            {ID: 'L1', MIN: 0, MAX: 20},
            {ID: 'MEA', MIN: 0, MAX: 10},
        ]},
        {ID: 'LH1', MIN: 0, MAX: 1000, LEVEL: [
            {ID: 'LH2', MIN: 0, MAX: 4},
            {ID: 'LH3', MIN: 0, MAX: 12},
            {ID: 'LFH', MIN: 0, MAX: 20},
            {ID: 'LEP', MIN: 0, MAX: 3},
            {ID: 'LH4', MIN: 0, MAX: 4},
            {ID: 'LHT', MIN: 0, MAX: 3},
            {ID: 'LHR', MIN: 0, MAX: 10},
            {ID: 'PER', MIN: 0, MAX: 5},
            {ID: 'LHE', MIN: 0, MAX: 1},
        ]},
        {ID: 'FA1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'FA2', MIN: 1, MAX: 99999},
            {ID: 'L10', MIN: 0, MAX: 1},
        ]},
        {ID: 'NM1', MIN: 0, MAX: 4, LEVEL: [
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
        ]},
        {ID: 'N1', MIN: 0, MAX: 4, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'L3', MIN: 0, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]

from bots.botsconfig import *
from records005012 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'CA',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BCA', MIN: 1, MAX: 1},
    {ID: 'CUR', MIN: 0, MAX: 1},
    {ID: 'REF', MIN: 0, MAX: 99999},
    {ID: 'PER', MIN: 0, MAX: 3},
    {ID: 'TAX', MIN: 0, MAX: 99999},
    {ID: 'FOB', MIN: 0, MAX: 99999},
    {ID: 'CTP', MIN: 0, MAX: 99999},
    {ID: 'PAM', MIN: 0, MAX: 10},
    {ID: 'CSH', MIN: 0, MAX: 1},
    {ID: 'SAC', MIN: 0, MAX: 25, LEVEL: [
        {ID: 'CUR', MIN: 0, MAX: 1},
    ]},
    {ID: 'ITD', MIN: 0, MAX: 5},
    {ID: 'DIS', MIN: 0, MAX: 20},
    {ID: 'INC', MIN: 0, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 10},
    {ID: 'LIN', MIN: 0, MAX: 5},
    {ID: 'SI', MIN: 0, MAX: 99999},
    {ID: 'PID', MIN: 0, MAX: 200},
    {ID: 'MEA', MIN: 0, MAX: 40},
    {ID: 'PWK', MIN: 0, MAX: 25},
    {ID: 'PKG', MIN: 0, MAX: 25},
    {ID: 'TD1', MIN: 0, MAX: 2},
    {ID: 'TD5', MIN: 0, MAX: 12},
    {ID: 'TD3', MIN: 0, MAX: 12},
    {ID: 'TD4', MIN: 0, MAX: 5},
    {ID: 'PCT', MIN: 0, MAX: 99999},
    {ID: 'MAN', MIN: 0, MAX: 10},
    {ID: 'TXI', MIN: 0, MAX: 99999},
    {ID: 'CTB', MIN: 0, MAX: 99999},
    {ID: 'G53', MIN: 0, MAX: 99999},
    {ID: 'LDT', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'QTY', MIN: 0, MAX: 99999},
        {ID: 'MTX', MIN: 0, MAX: 99999},
    ]},
    {ID: 'N9', MIN: 0, MAX: 1000, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 99999},
        {ID: 'MTX', MIN: 0, MAX: 99999},
        {ID: 'PWK', MIN: 0, MAX: 99999},
        {ID: 'EFI', MIN: 0, MAX: 99999},
    ]},
    {ID: 'N1', MIN: 0, MAX: 200, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'IN2', MIN: 0, MAX: 99999},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'NX2', MIN: 0, MAX: 99999},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'PER', MIN: 0, MAX: 99999},
        {ID: 'SI', MIN: 0, MAX: 99999},
        {ID: 'FOB', MIN: 0, MAX: 1},
        {ID: 'TD1', MIN: 0, MAX: 2},
        {ID: 'TD5', MIN: 0, MAX: 12},
        {ID: 'TD3', MIN: 0, MAX: 12},
        {ID: 'TD4', MIN: 0, MAX: 5},
        {ID: 'PKG', MIN: 0, MAX: 25},
        {ID: 'MTX', MIN: 0, MAX: 99999},
    ]},
    {ID: 'AMT', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'PCT', MIN: 0, MAX: 99999},
    ]},
    {ID: 'ADV', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 99999},
        {ID: 'MTX', MIN: 0, MAX: 99999},
    ]},
    {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'LQ', MIN: 1, MAX: 99999},
    ]},
    {ID: 'POC', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'LIN', MIN: 0, MAX: 99999},
        {ID: 'SI', MIN: 0, MAX: 99999},
        {ID: 'CUR', MIN: 0, MAX: 1},
        {ID: 'PO3', MIN: 0, MAX: 25},
        {ID: 'CTP', MIN: 0, MAX: 99999},
        {ID: 'PAM', MIN: 0, MAX: 10},
        {ID: 'MEA', MIN: 0, MAX: 40},
        {ID: 'PID', MIN: 0, MAX: 1000, LEVEL: [
            {ID: 'MEA', MIN: 0, MAX: 10},
        ]},
        {ID: 'PWK', MIN: 0, MAX: 25},
        {ID: 'PKG', MIN: 0, MAX: 25},
        {ID: 'PO4', MIN: 0, MAX: 99999},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'PER', MIN: 0, MAX: 3},
        {ID: 'SAC', MIN: 0, MAX: 25, LEVEL: [
            {ID: 'CUR', MIN: 0, MAX: 1},
        ]},
        {ID: 'IT8', MIN: 0, MAX: 1},
        {ID: 'CSH', MIN: 0, MAX: 99999},
        {ID: 'ITD', MIN: 0, MAX: 2},
        {ID: 'DIS', MIN: 0, MAX: 20},
        {ID: 'INC', MIN: 0, MAX: 1},
        {ID: 'TAX', MIN: 0, MAX: 99999},
        {ID: 'FOB', MIN: 0, MAX: 99999},
        {ID: 'SDQ', MIN: 0, MAX: 500},
        {ID: 'DTM', MIN: 0, MAX: 10},
        {ID: 'TD1', MIN: 0, MAX: 1},
        {ID: 'TD5', MIN: 0, MAX: 12},
        {ID: 'TD3', MIN: 0, MAX: 12},
        {ID: 'TD4', MIN: 0, MAX: 5},
        {ID: 'TXI', MIN: 0, MAX: 99999},
        {ID: 'PCT', MIN: 0, MAX: 99999},
        {ID: 'ACK', MIN: 0, MAX: 104, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
        ]},
        {ID: 'MAN', MIN: 0, MAX: 10},
        {ID: 'SPI', MIN: 0, MAX: 99999},
        {ID: 'MTX', MIN: 0, MAX: 99999},
        {ID: 'CTB', MIN: 0, MAX: 99999},
        {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'LQ', MIN: 1, MAX: 99999},
        ]},
        {ID: 'AMT', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'PCT', MIN: 0, MAX: 99999},
        ]},
        {ID: 'QTY', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'SI', MIN: 0, MAX: 99999},
        ]},
        {ID: 'SCH', MIN: 0, MAX: 200, LEVEL: [
            {ID: 'TD1', MIN: 0, MAX: 2},
            {ID: 'TD5', MIN: 0, MAX: 12},
            {ID: 'TD3', MIN: 0, MAX: 12},
            {ID: 'TD4', MIN: 0, MAX: 5},
            {ID: 'REF', MIN: 0, MAX: 99999},
        ]},
        {ID: 'LDT', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'QTY', MIN: 0, MAX: 99999},
            {ID: 'MTX', MIN: 0, MAX: 99999},
            {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'LQ', MIN: 1, MAX: 99999},
            ]},
        ]},
        {ID: 'N9', MIN: 0, MAX: 1000, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 99999},
            {ID: 'MTX', MIN: 0, MAX: 99999},
            {ID: 'PWK', MIN: 0, MAX: 99999},
            {ID: 'EFI', MIN: 0, MAX: 99999},
        ]},
        {ID: 'N1', MIN: 0, MAX: 200, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'IN2', MIN: 0, MAX: 99999},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'QTY', MIN: 0, MAX: 99999},
            {ID: 'NX2', MIN: 0, MAX: 99999},
            {ID: 'REF', MIN: 0, MAX: 12},
            {ID: 'PER', MIN: 0, MAX: 3},
            {ID: 'SI', MIN: 0, MAX: 99999},
            {ID: 'DTM', MIN: 0, MAX: 1},
            {ID: 'FOB', MIN: 0, MAX: 1},
            {ID: 'SCH', MIN: 0, MAX: 200},
            {ID: 'TD1', MIN: 0, MAX: 2},
            {ID: 'TD5', MIN: 0, MAX: 12},
            {ID: 'TD3', MIN: 0, MAX: 12},
            {ID: 'TD4', MIN: 0, MAX: 5},
            {ID: 'PKG', MIN: 0, MAX: 25},
            {ID: 'LDT', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'MAN', MIN: 0, MAX: 10},
                {ID: 'QTY', MIN: 0, MAX: 5},
                {ID: 'MTX', MIN: 0, MAX: 99999},
            ]},
        ]},
        {ID: 'SLN', MIN: 0, MAX: 1000, LEVEL: [
            {ID: 'MTX', MIN: 0, MAX: 99999},
            {ID: 'SI', MIN: 0, MAX: 99999},
            {ID: 'PID', MIN: 0, MAX: 1000},
            {ID: 'PO3', MIN: 0, MAX: 25},
            {ID: 'MEA', MIN: 0, MAX: 99999},
            {ID: 'CTP', MIN: 0, MAX: 25},
            {ID: 'PAM', MIN: 0, MAX: 10},
            {ID: 'ACK', MIN: 0, MAX: 104},
            {ID: 'SAC', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'CUR', MIN: 0, MAX: 1},
            ]},
            {ID: 'DTM', MIN: 0, MAX: 10},
            {ID: 'PO4', MIN: 0, MAX: 1},
            {ID: 'TAX', MIN: 0, MAX: 3},
            {ID: 'ADV', MIN: 0, MAX: 99999},
            {ID: 'QTY', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'SI', MIN: 0, MAX: 99999},
            ]},
            {ID: 'N9', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 99999},
                {ID: 'MTX', MIN: 0, MAX: 99999},
            ]},
            {ID: 'N1', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 2},
                {ID: 'IN2', MIN: 0, MAX: 99999},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'NX2', MIN: 0, MAX: 99999},
                {ID: 'REF', MIN: 0, MAX: 12},
                {ID: 'PER', MIN: 0, MAX: 3},
                {ID: 'SI', MIN: 0, MAX: 99999},
            ]},
        ]},
        {ID: 'PD', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'PDD', MIN: 0, MAX: 99999},
        ]},
    ]},
    {ID: 'CTT', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'AMT', MIN: 0, MAX: 5},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]

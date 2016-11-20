from bots.botsconfig import *
from records004042 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'BC',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 1, MAX: 2, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'NX2', MIN: 0, MAX: 99999},
        {ID: 'PER', MIN: 0, MAX: 99999},
    ]},
    {ID: 'HL', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'N1', MIN: 1, MAX: 1},
        {ID: 'DTP', MIN: 0, MAX: 99999},
        {ID: 'LUI', MIN: 0, MAX: 1},
        {ID: 'C3', MIN: 0, MAX: 1},
        {ID: 'CRC', MIN: 0, MAX: 99999},
        {ID: 'MTX', MIN: 0, MAX: 99999},
        {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'TPB', MIN: 0, MAX: 3},
            {ID: 'DTP', MIN: 0, MAX: 99999},
        ]},
        {ID: 'NX1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'NX2', MIN: 0, MAX: 99999},
            {ID: 'COM', MIN: 0, MAX: 99999},
            {ID: 'YNQ', MIN: 0, MAX: 99999},
            {ID: 'DTP', MIN: 0, MAX: 99999},
            {ID: 'REQ', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'LOD', MIN: 0, MAX: 3},
                {ID: 'MTX', MIN: 0, MAX: 99999},
                {ID: 'FDA', MIN: 0, MAX: 99999},
                {ID: 'III', MIN: 0, MAX: 99999},
                {ID: 'DTP', MIN: 0, MAX: 99999},
                {ID: 'AWD', MIN: 0, MAX: 99999},
                {ID: 'QTY', MIN: 0, MAX: 99999},
                {ID: 'CRC', MIN: 0, MAX: 99999},
                {ID: 'N1', MIN: 0, MAX: 1},
                {ID: 'N2', MIN: 0, MAX: 2},
            ]},
        ]},
        {ID: 'INR', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'NX1', MIN: 0, MAX: 1},
            {ID: 'ITC', MIN: 0, MAX: 99999},
            {ID: 'C3', MIN: 0, MAX: 1},
            {ID: 'QTY', MIN: 0, MAX: 99999},
            {ID: 'ASO', MIN: 0, MAX: 99999},
            {ID: 'SPR', MIN: 0, MAX: 99999},
            {ID: 'DMG', MIN: 0, MAX: 1},
            {ID: 'EMS', MIN: 0, MAX: 1},
            {ID: 'TER', MIN: 0, MAX: 99999},
            {ID: 'YNQ', MIN: 0, MAX: 99999},
            {ID: 'ASI', MIN: 0, MAX: 1},
            {ID: 'CRC', MIN: 0, MAX: 99999},
            {ID: 'DTP', MIN: 0, MAX: 99999},
            {ID: 'N9', MIN: 0, MAX: 99999},
            {ID: 'MTX', MIN: 0, MAX: 99999},
            {ID: 'INQ', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'DTP', MIN: 0, MAX: 99999},
                {ID: 'C3', MIN: 0, MAX: 1},
                {ID: 'III', MIN: 0, MAX: 99999},
                {ID: 'PYT', MIN: 0, MAX: 99999},
                {ID: 'PYM', MIN: 0, MAX: 99999},
                {ID: 'AWD', MIN: 0, MAX: 99999},
                {ID: 'QTY', MIN: 0, MAX: 1},
                {ID: 'ACD', MIN: 0, MAX: 99999},
                {ID: 'MEA', MIN: 0, MAX: 99999},
                {ID: 'SPR', MIN: 0, MAX: 99999},
                {ID: 'ASO', MIN: 0, MAX: 99999},
            ]},
            {ID: 'LX', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'NM1', MIN: 0, MAX: 1},
                {ID: 'NX1', MIN: 0, MAX: 1},
                {ID: 'N2', MIN: 0, MAX: 2},
                {ID: 'TPB', MIN: 0, MAX: 6},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'NX2', MIN: 0, MAX: 99999},
                {ID: 'COM', MIN: 0, MAX: 99999},
                {ID: 'N9', MIN: 0, MAX: 99999},
                {ID: 'AWD', MIN: 0, MAX: 99999},
                {ID: 'ASO', MIN: 0, MAX: 99999},
                {ID: 'YNQ', MIN: 0, MAX: 99999},
                {ID: 'PCT', MIN: 0, MAX: 99999},
                {ID: 'DTP', MIN: 0, MAX: 99999},
                {ID: 'QTY', MIN: 0, MAX: 99999},
            ]},
            {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'III', MIN: 1, MAX: 99999},
                {ID: 'PCT', MIN: 0, MAX: 99999},
                {ID: 'LX', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'DTP', MIN: 0, MAX: 99999},
                    {ID: 'MTX', MIN: 0, MAX: 99999},
                    {ID: 'LQ', MIN: 0, MAX: 99999},
                    {ID: 'AWD', MIN: 0, MAX: 99999},
                    {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'N2', MIN: 0, MAX: 2},
                        {ID: 'TPB', MIN: 0, MAX: 6},
                    ]},
                ]},
            ]},
            {ID: 'REQ', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'AWD', MIN: 0, MAX: 99999},
                {ID: 'CRC', MIN: 0, MAX: 99999},
                {ID: 'QTY', MIN: 0, MAX: 99999},
                {ID: 'PCT', MIN: 0, MAX: 99999},
                {ID: 'DTP', MIN: 0, MAX: 99999},
                {ID: 'YNQ', MIN: 0, MAX: 99999},
                {ID: 'MTX', MIN: 0, MAX: 99999},
            ]},
            {ID: 'API', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'YNQ', MIN: 0, MAX: 1},
                {ID: 'N9', MIN: 0, MAX: 99999},
                {ID: 'CDS', MIN: 0, MAX: 1},
                {ID: 'DTP', MIN: 0, MAX: 99999},
                {ID: 'BBC', MIN: 0, MAX: 99999},
                {ID: 'MEA', MIN: 0, MAX: 99999},
                {ID: 'ASO', MIN: 0, MAX: 99999},
                {ID: 'MTX', MIN: 0, MAX: 99999},
                {ID: 'PCT', MIN: 0, MAX: 99999},
                {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'III', MIN: 1, MAX: 99999},
                ]},
                {ID: 'CRC', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'AWD', MIN: 0, MAX: 99999},
                ]},
                {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'N2', MIN: 0, MAX: 2},
                    {ID: 'TPB', MIN: 0, MAX: 6},
                    {ID: 'N3', MIN: 0, MAX: 2},
                    {ID: 'N4', MIN: 0, MAX: 1},
                    {ID: 'NX2', MIN: 0, MAX: 99999},
                    {ID: 'COM', MIN: 0, MAX: 99999},
                    {ID: 'DTP', MIN: 0, MAX: 99999},
                    {ID: 'ITC', MIN: 0, MAX: 1},
                    {ID: 'MTX', MIN: 0, MAX: 99999},
                    {ID: 'YNQ', MIN: 0, MAX: 99999},
                    {ID: 'AWD', MIN: 0, MAX: 99999},
                    {ID: 'IN1', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'IN2', MIN: 0, MAX: 99999},
                        {ID: 'TPB', MIN: 0, MAX: 3},
                        {ID: 'N3', MIN: 0, MAX: 2},
                        {ID: 'N4', MIN: 0, MAX: 1},
                        {ID: 'NX2', MIN: 0, MAX: 99999},
                    ]},
                ]},
                {ID: 'CED', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'DTP', MIN: 0, MAX: 99999},
                    {ID: 'MTX', MIN: 0, MAX: 99999},
                    {ID: 'NM1', MIN: 0, MAX: 1},
                    {ID: 'N2', MIN: 0, MAX: 2},
                    {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'LQ', MIN: 1, MAX: 99999},
                    ]},
                ]},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]

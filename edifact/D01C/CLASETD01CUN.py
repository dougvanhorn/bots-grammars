#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD01CUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 1},
    {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'PNA', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'ADR', MIN: 0, MAX: 1},
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'VLI', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'EQN', MIN: 0, MAX: 1},
        {ID: 'PNA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'LAN', MIN: 0, MAX: 1},
            {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'ADR', MIN: 0, MAX: 1},
                {ID: 'COM', MIN: 0, MAX: 9},
            ]},
        ]},
        {ID: 'STS', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
        ]},
        {ID: 'ATT', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'ELM', MIN: 0, MAX: 1},
            {ID: 'CAV', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'FTX', MIN: 0, MAX: 99},
            ]},
            {ID: 'STS', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 9},
            ]},
        ]},
        {ID: 'SCD', MIN: 0, MAX: 999999, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'EQN', MIN: 0, MAX: 1},
            {ID: 'STS', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 9},
            ]},
            {ID: 'ATT', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'ELM', MIN: 0, MAX: 1},
                {ID: 'CAV', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'FTX', MIN: 0, MAX: 99},
                ]},
                {ID: 'STS', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 9},
                ]},
            ]},
            {ID: 'IDE', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'EQN', MIN: 0, MAX: 1},
                {ID: 'STS', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 9},
                ]},
                {ID: 'ATT', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 2},
                    {ID: 'ELM', MIN: 0, MAX: 1},
                    {ID: 'CAV', MIN: 0, MAX: 99, LEVEL: [
                        {ID: 'FTX', MIN: 0, MAX: 99},
                    ]},
                    {ID: 'STS', MIN: 0, MAX: 99, LEVEL: [
                        {ID: 'DTM', MIN: 0, MAX: 9},
                    ]},
                ]},
            ]},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

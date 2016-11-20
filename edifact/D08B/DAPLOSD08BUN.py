#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD08BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 9},
    {ID: 'IMD', MIN: 0, MAX: 1},
    {ID: 'NAD', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 9},
    ]},
    {ID: 'LIN', MIN: 0, MAX: 9999, LEVEL: [
        {ID: 'DTM', MIN: 1, MAX: 9},
        {ID: 'PIA', MIN: 1, MAX: 9},
        {ID: 'QTY', MIN: 0, MAX: 1},
        {ID: 'CCI', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'CAV', MIN: 0, MAX: 1},
        ]},
        {ID: 'RFF', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'MEA', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'GPO', MIN: 0, MAX: 9999},
            ]},
        ]},
        {ID: 'IMD', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'QTY', MIN: 0, MAX: 1},
            {ID: 'NAD', MIN: 0, MAX: 1},
            {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'HYN', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'PIA', MIN: 0, MAX: 9},
            {ID: 'CCI', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'CAV', MIN: 0, MAX: 1},
            ]},
            {ID: 'IMD', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 1},
                {ID: 'QTY', MIN: 0, MAX: 1},
                {ID: 'NAD', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'DOC', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'NAD', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 9},
        ]},
        {ID: 'EVE', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'IMD', MIN: 0, MAX: 9},
            {ID: 'NAD', MIN: 0, MAX: 1},
            {ID: 'FTX', MIN: 0, MAX: 9},
            {ID: 'CCI', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'CAV', MIN: 0, MAX: 99},
            ]},
            {ID: 'MEA', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'GPO', MIN: 0, MAX: 9999},
            ]},
            {ID: 'IFD', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'PIA', MIN: 0, MAX: 9},
                {ID: 'QTY', MIN: 0, MAX: 9},
                {ID: 'NAD', MIN: 0, MAX: 1},
                {ID: 'COD', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'MEA', MIN: 0, MAX: 1},
                ]},
                {ID: 'CCI', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'CAV', MIN: 0, MAX: 1},
                ]},
                {ID: 'RFF', MIN: 0, MAX: 999, LEVEL: [
                    {ID: 'QTY', MIN: 0, MAX: 9},
                    {ID: 'MEA', MIN: 0, MAX: 1},
                ]},
                {ID: 'DOC', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'NAD', MIN: 0, MAX: 1},
                    {ID: 'DTM', MIN: 0, MAX: 9},
                ]},
            ]},
            {ID: 'HYN', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'NAD', MIN: 0, MAX: 1},
                {ID: 'FTX', MIN: 0, MAX: 9},
                {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 1},
                ]},
            ]},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD98AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 1},
    {ID: 'BUS', MIN: 0, MAX: 1},
    {ID: 'RFF', MIN: 0, MAX: 2, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'FII', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 5},
    ]},
    {ID: 'NAD', MIN: 0, MAX: 3, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 5},
    ]},
    {ID: 'LIN', MIN: 1, MAX: 9999, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
        {ID: 'RFF', MIN: 0, MAX: 2},
        {ID: 'BUS', MIN: 0, MAX: 1},
        {ID: 'FCA', MIN: 0, MAX: 1},
        {ID: 'MOA', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'CUX', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 2},
            {ID: 'RFF', MIN: 0, MAX: 1},
        ]},
        {ID: 'FII', MIN: 1, MAX: 1, LEVEL: [
            {ID: 'CTA', MIN: 0, MAX: 1},
            {ID: 'COM', MIN: 0, MAX: 5},
        ]},
        {ID: 'NAD', MIN: 0, MAX: 3, LEVEL: [
            {ID: 'CTA', MIN: 0, MAX: 1},
            {ID: 'COM', MIN: 0, MAX: 5},
        ]},
        {ID: 'INP', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 2},
        ]},
        {ID: 'GIS', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'MOA', MIN: 0, MAX: 1},
            {ID: 'LOC', MIN: 0, MAX: 2},
            {ID: 'NAD', MIN: 0, MAX: 1},
            {ID: 'RCS', MIN: 0, MAX: 1},
            {ID: 'FTX', MIN: 0, MAX: 10},
        ]},
        {ID: 'PRC', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'FTX', MIN: 1, MAX: 1},
        ]},
        {ID: 'SEQ', MIN: 1, MAX: 99999, LEVEL: [
            {ID: 'MOA', MIN: 1, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 1},
            {ID: 'RFF', MIN: 0, MAX: 3},
            {ID: 'PAI', MIN: 0, MAX: 1},
            {ID: 'FCA', MIN: 0, MAX: 1},
            {ID: 'FII', MIN: 0, MAX: 3, LEVEL: [
                {ID: 'CTA', MIN: 0, MAX: 1},
                {ID: 'COM', MIN: 0, MAX: 5},
            ]},
            {ID: 'NAD', MIN: 0, MAX: 3, LEVEL: [
                {ID: 'CTA', MIN: 0, MAX: 1},
                {ID: 'COM', MIN: 0, MAX: 5},
            ]},
            {ID: 'INP', MIN: 0, MAX: 3, LEVEL: [
                {ID: 'FTX', MIN: 0, MAX: 1},
                {ID: 'DTM', MIN: 0, MAX: 2},
            ]},
            {ID: 'GIS', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'MOA', MIN: 0, MAX: 1},
                {ID: 'LOC', MIN: 0, MAX: 2},
                {ID: 'NAD', MIN: 0, MAX: 1},
                {ID: 'RCS', MIN: 0, MAX: 1},
                {ID: 'FTX', MIN: 0, MAX: 10},
            ]},
            {ID: 'PRC', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'FTX', MIN: 0, MAX: 5},
                {ID: 'DOC', MIN: 0, MAX: 9999, LEVEL: [
                    {ID: 'MOA', MIN: 0, MAX: 5},
                    {ID: 'DTM', MIN: 0, MAX: 5},
                    {ID: 'RFF', MIN: 0, MAX: 5},
                    {ID: 'NAD', MIN: 0, MAX: 2},
                    {ID: 'CUX', MIN: 0, MAX: 5, LEVEL: [
                        {ID: 'DTM', MIN: 0, MAX: 1},
                    ]},
                    {ID: 'AJT', MIN: 0, MAX: 100, LEVEL: [
                        {ID: 'MOA', MIN: 1, MAX: 1},
                        {ID: 'RFF', MIN: 0, MAX: 1},
                        {ID: 'FTX', MIN: 0, MAX: 5},
                    ]},
                    {ID: 'DLI', MIN: 0, MAX: 1000, LEVEL: [
                        {ID: 'MOA', MIN: 1, MAX: 5},
                        {ID: 'PIA', MIN: 0, MAX: 5},
                        {ID: 'DTM', MIN: 0, MAX: 5},
                        {ID: 'CUX', MIN: 0, MAX: 5, LEVEL: [
                            {ID: 'DTM', MIN: 0, MAX: 1},
                        ]},
                        {ID: 'AJT', MIN: 0, MAX: 10, LEVEL: [
                            {ID: 'MOA', MIN: 1, MAX: 1},
                            {ID: 'RFF', MIN: 0, MAX: 1},
                            {ID: 'FTX', MIN: 0, MAX: 5},
                        ]},
                    ]},
                ]},
                {ID: 'GIS', MIN: 0, MAX: 1, LEVEL: [
                    {ID: 'MOA', MIN: 0, MAX: 5},
                ]},
            ]},
        ]},
    ]},
    {ID: 'CNT', MIN: 0, MAX: 5},
    {ID: 'AUT', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

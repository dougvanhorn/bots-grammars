#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD01AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 9},
    {ID: 'AGR', MIN: 1, MAX: 9},
    {ID: 'RFF', MIN: 1, MAX: 9},
    {ID: 'GEI', MIN: 0, MAX: 9},
    {ID: 'FTX', MIN: 0, MAX: 9},
    {ID: 'PNA', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'BUS', MIN: 0, MAX: 1},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'IDE', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'GEI', MIN: 0, MAX: 9},
        {ID: 'ICD', MIN: 0, MAX: 1},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'ATT', MIN: 0, MAX: 99},
        {ID: 'CUX', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'PER', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 2, LEVEL: [
                {ID: 'GEI', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'LOC', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'MEA', MIN: 0, MAX: 2},
            {ID: 'ADR', MIN: 0, MAX: 1},
        ]},
        {ID: 'CLA', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'APP', MIN: 0, MAX: 1},
            {ID: 'MOA', MIN: 0, MAX: 9},
            {ID: 'PCD', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'GEI', MIN: 0, MAX: 1},
            {ID: 'FTX', MIN: 0, MAX: 1},
        ]},
        {ID: 'PRV', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'APP', MIN: 0, MAX: 9},
            {ID: 'MOA', MIN: 0, MAX: 9},
            {ID: 'RTE', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'QTY', MIN: 0, MAX: 9},
            {ID: 'FOR', MIN: 0, MAX: 1},
            {ID: 'CUX', MIN: 0, MAX: 9},
            {ID: 'CLA', MIN: 0, MAX: 99},
            {ID: 'GEI', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 9},
            {ID: 'BAS', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'APP', MIN: 0, MAX: 1},
            ]},
            {ID: 'ATT', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'PCD', MIN: 0, MAX: 1},
            ]},
            {ID: 'LOC', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'MEA', MIN: 0, MAX: 2},
                {ID: 'ADR', MIN: 0, MAX: 1},
            ]},
            {ID: 'PYT', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'PCD', MIN: 0, MAX: 1},
            ]},
            {ID: 'RFF', MIN: 1, MAX: 99, LEVEL: [
                {ID: 'MOA', MIN: 0, MAX: 1},
                {ID: 'PCD', MIN: 0, MAX: 9},
                {ID: 'DTM', MIN: 0, MAX: 9},
            ]},
        ]},
        {ID: 'PNA', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'ATT', MIN: 1, MAX: 9},
            {ID: 'ADR', MIN: 0, MAX: 9},
            {ID: 'CTA', MIN: 0, MAX: 1},
            {ID: 'COM', MIN: 0, MAX: 9},
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'STS', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'RFF', MIN: 0, MAX: 9},
                {ID: 'DTM', MIN: 0, MAX: 9},
                {ID: 'MOA', MIN: 0, MAX: 9},
                {ID: 'PCD', MIN: 0, MAX: 9},
                {ID: 'QTY', MIN: 0, MAX: 9},
                {ID: 'FTX', MIN: 0, MAX: 9},
                {ID: 'RCS', MIN: 0, MAX: 999, LEVEL: [
                    {ID: 'FTX', MIN: 0, MAX: 9},
                    {ID: 'ATT', MIN: 0, MAX: 1},
                    {ID: 'RFF', MIN: 0, MAX: 1},
                    {ID: 'PCD', MIN: 0, MAX: 1},
                ]},
            ]},
        ]},
    ]},
    {ID: 'DOC', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'IDE', MIN: 0, MAX: 1},
        {ID: 'COM', MIN: 0, MAX: 1},
        {ID: 'EFI', MIN: 0, MAX: 1},
        {ID: 'PNA', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]

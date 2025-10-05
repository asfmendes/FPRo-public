#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: afmendes
"""

def get_clean_input(): # Function Header
    # Function Body starts
    name = input("Enter your name: ") 
    return name.strip().title()
    # Function Body ends

def welcome_user(name):
    print(f"Hello, {name}!")

# Main program
user_name = get_clean_input()
welcome_user(user_name)

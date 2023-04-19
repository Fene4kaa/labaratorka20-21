# coding=UTF-8
import numpy as np
def hex_table():
    table = np.zeros((16, 16), dtype=int)
    
    for i in range(16):
        for j in range(16):
            table[i][j] = i * j
    
    print("Таблица сложения: ")
    print("   |", end="")
    for i in range(16):
        print(f" {hex(i)[2:].upper()}|", end="")
    print()
    print("-" * 51)
    for i in range(16):
        print(f"{hex(i)[2:].upper()} |", end="")
        for j in range(16):
            print(f" {hex(table[i][j])[2:].upper().zfill(2)}|", end="")
        print()
    
    
    for i in range(16):
        for j in range(16):
            table[i][j] = i + j
    
   
    print("\n Таблица умножения:")
    print("  |", end="")
    for i in range(16):
        print(f" {hex(i)[2:].upper()}|", end="")
    print()
    print("-" * 35)
    for i in range(16):
        print(f"{hex(i)[2:].upper()} |", end="")
        for j in range(16):
            print(f" {hex(table[i][j])[2:].upper().zfill(2)}|", end="")
        print()
##ВНЁС ИЗМЕНЕНИЯ В КОД
##ВНЁС ИЗМЕНЕНИЯ В КОД
##ВНЁС ИЗМЕНЕНИЯ В КОД
##ВНЁС ИЗМЕНЕНИЯ В КОД
##ВНЁС ИЗМЕНЕНИЯ В КОД
##ВНЁС ИЗМЕНЕНИЯ В КОД
hex_table()
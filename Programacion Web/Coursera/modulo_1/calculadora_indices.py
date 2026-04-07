# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 16:37:08 2024

@author: tatia
"""

def calcular_IMC(peso:float, altura:float)-> float:
    IMC=peso/altura**2
    return IMC

def calcular_porcentaje_grasa(peso:float, altura:float, edad:int,valor_genero:float)-> float:
    IMC=calcular_IMC(peso, altura)
    GC = 1.2 * IMC + 0.23 * edad - 5.4 - valor_genero
    return GC

def calcular_calorias_en_reposo(peso:float, altura:float, edad:int,valor_genero:float)-> float:
    TMB = (10*peso) + (6.25*altura) - (5*edad) + valor_genero
    return TMB

def calcular_calorias_en_actividad(peso:float, altura:float, edad:int,valor_genero:float,valor_actividad:float)-> float:
    TMB=calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    TMB_actividad_fisica = TMB * valor_actividad
    return TMB_actividad_fisica

def consumo_calorias_recomendado_para_adelgazar (peso:float, altura:float, edad:int,valor_genero:float)-> str:
    TMB=calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    LI=round(0.80*TMB,2)
    LS=round(0.85*TMB,2)
    recomendacion="Para adelgazar es recomendado que consumas entre:", LI ," y ", LS," calorías al día."
    return recomendacion

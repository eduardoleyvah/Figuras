# -*- coding: utf-8 -*-
from lettuce import step, world
from Figuras import Figuras

@step(u'cuando realizo la operación')
def cuando_realizo_la_operacion(step):
    pass

@step(u'Dado que ingreso el radio "([^"]*)"')
def dado_que_ingreso_el_numero_group1(step, num1):
    world.cal = Calculadora()
    world.cal.circulo(int(num1))

@step(u'Dado que ingreso los lados "([^"]*)" y "([^"]*)"')
def dado_que_ingreso_los_numeros_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.rectangulo(int(num1), int(num2))

@step(u'Dado que ingreso el lado "([^"]*)"')
def dado_que_ingreso_el_lado_group1(step, num1):
    world.cal = Calculadora()
    world.cal.cuadrado(int(num1))

@step(u'Dado que ingreso los lados "([^"]*)", "([^"]*)" y "([^"]*)"')
def dado_que_ingreso_los_numeros_group1_group2_y_group3(step, num1, num2, num3):
    world.cal = Calculadora()
    world.cal.trapecio(int(num1), int(num2), int(num3))

@step(u'entonces obtengo el area "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, esperado):
    assert float(esperado) == world.cal.obtener_resultado(),'El resultado esperado es ' +esperado+ ' y el obtenido es ' +str(world.cal.obtener_resultado())

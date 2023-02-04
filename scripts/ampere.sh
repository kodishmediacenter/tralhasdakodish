#!/bin/bash
clear
echo "+++++++++++++++++++++++++++++++++++++++++++++++"
echo ""
echo "++++++++++ Calculadora de amperagem +++++++++++"
echo ""
echo "+++++++++++++++++++++++++++++++++++++++++++++++"
echo ""
echo ""
read -p "Informe a potência do equipamento em Watts: " w
read -p "Informe a voltagem do equipamento em Volts: " v

result=$(echo "scale=2; $w / $v" | bc)

echo "A amperagem do equipamento é de aproximadamente $result Amperes."

#!/bin/bash
clear
echo "+++++++++++++++++++++++++++++++++++++++++++++++"
echo ""
echo "++++++++++ Calculadora de amperagem +++++++++++"
echo ""
echo "+++++++++++++++++++++++++++++++++++++++++++++++"
echo ""
echo ""
read -p "Informe a voltagem em Volts: " v
read -p "Informe a corrente elétrica em Amperes: " i

result=$(echo "scale=2; $v / $i" | bc)

echo "A resistência elétrica é de aproximadamente $result Ohms."

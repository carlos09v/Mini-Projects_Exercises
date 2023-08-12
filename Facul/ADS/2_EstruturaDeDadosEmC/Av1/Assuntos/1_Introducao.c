#include <stdio.h>
// Obs: C é mt RUIM !! -> 02/03/23

// 1. Faça um programa que leia um número inteiro e retorne seu antecessor e sucessor
int sucessorAntecessor(int N) {
  printf("O sucessor de %d é %d \n", N, N+1);
  return printf("E o antecessor é %d.\n", N-1);
}

// 2. Leia quatro notas de 1 aluno. Calcule e exiba a média aritmética dessas notas
int mediaAritmetica() {
  float notas[4];
  float media=0;
  
  for(int c = 0; c < 4; c++) {
    printf("Qual a sua %d nota ? \n", c+1);
    scanf("%f", &notas[c]);
    media += notas[c];
  }
  
  media = media / 4;
  printf("A média é %.2f", media);

  return 0;
}

// 3. Faça um programa que leia um valor em reais e a cotação do dólar. Em seguida, imprima o valor correspondente em dólares
int converterEmDolar(float Reais, float CotaDolar){
  printf("Convertendo R$%.2f em dólares fica $%.2f", Reais, Reais*CotaDolar);

  return 0;
}

// 4. Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão é R = G * pi/180, sendo G o ângulo em graus e R em radianos e pi = 3.14

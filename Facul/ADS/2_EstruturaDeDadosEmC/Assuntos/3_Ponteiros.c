#include <stdio.h>
#include <stdlib.h>

// 1 -
int atribuindoPonteiro() {
  int *p;
  int num=10;
  
  p = &num; // Atribuindo variavel ao ponteiro

  printf("VALOR: %d\n", *p);
  printf("ENDEREÇO: %p", p);
  
  return 0;
}

// 2 -
int mudandoPonteiro() {
  int *p, x = 10;

  p = &x;
  printf("Conteudo apontado por p: %d \n", *p);
  printf("Endereço apontado por p: %p \n\n", p);

  (*p)++;
  printf("Conteudo apontado por p: %d \n", *p);
  printf("Endereço apontado por p: %p \n\n", p);

  *p = (*p) * 10;
  printf("Conteudo apontado por p: %d \n", *p);
  printf("Endereço apontado por p: %p \n\n", p);

  printf("Valor de P: %d", *p);
  
  return 0;
}

// 3 -
int vetorNoPonteiro() {
  int vet[5] = {1, 2, 3, 4, 5};
  int *p = vet;

  for(int i = 0;i < 5; i++) {
    printf("Valor: %d\n", *(p+i));
    printf("Endereço: %p\n", p+1);
  }
  
  return 0;
}

// 4 - Escreva um programa que contenha duas variáveis inteiras. Compare seus endereços e exiba o maior endereço.
int maiorEndereco() {
  int *p, *p1, x, y;
  p = &x;
  p1 = &y;

  if(p > p1) {
    printf("O ponteiro p aponta para uma posição a frente de p1\n");
    printf("Endereço de p: %p\n", p);
    printf("Endereço de p1: %p", p1);
  }else {
    printf("O ponteiro p aponta para uma posição a atrás de p1\n");
    printf("Endereço de p: %p\n", p);
    printf("Endereço de p1: %p", p1);
  }
  
  return 0;
}

// 5 - Escreva um programa que contenha duas variáveis inteiras. Leia essas variáveis do teclado. Em seguida, compare seus endereços e exiba o conteúdo do maior endereço.

// 6 - Crie um programa que contenha um array de float contendo 10 elementos. Imprima o endereço de cada posição desse array.
int enderecoDeArray() {
  float v[10];
  float *p = v;
  
  printf("Digite 10 valores: \n");
  for(int c = 0; c < 10; c++) {
    printf("%d valor: ", c+1);
    scanf("%f", &v[c]);
  }

  printf("Endereços de cada posição do Array:\n");
  for(int c = 0; c < 10; c++) {
    printf("%p\n", p+1);
  }
  
  return 0;
}

// 7 - Crie um programa que contenha um array de inteiros contendo 5 elementos. Utilizando apenas aritmética de ponteiros, leia esse array do teclado e imprima o dobro de cada valor lido.

// Alocação na Memória
// 8 -
int funcoesPraAlocar() {
  int *p1;
  p1 = (int *) calloc(5, sizeof(int));

  for(int i = 0; i < 5; i++) {
    printf("Digite o valor da posição %d: ", i+1);
    scanf("%d", &p1[i]);
  }

  printf("VALORES E ENDEREÇOS \n");
  for(int i = 0; i < 5; i++) {
    printf("VALOR: %d\n", *p1);
    printf("ENDEREÇO: %p\n", p1);
    p1++;
  }

  free(p1); // Liberar espaço na memória e apagar variável
  
  return 0;
}

// 9 -
int funcoes2PraAlocar() {
  int *p;
  p = (int *) malloc(3 * sizeof(int));

  for(int i = 0;i < 3;i++){
    printf("Digite um valor da posição %d: ", i+1);
    scanf("%d", p+1);
  }

  printf("VALORES E ENDEREÇOS \n");
  for(int i = 0; i < 3; i++) {
    printf("VALOR: %d\n", *p);
    printf("ENDEREÇO: %p\n", p);
    p++;
  }

  free(p); // Liberar espaço na memória e apagar variável

  return 0;
}
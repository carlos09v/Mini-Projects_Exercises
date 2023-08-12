#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// 1 -
int manipulandoVetor() {
  int vetor[5];
  printf("Digite 5 valores: \n");
  
  for(int count = 0; count < 5; count++) {
    printf("%d valor: ", count+1);
    scanf("%d", &vetor[count]);

    // printf("vetor[%d] = %d\n", count, vetor[count]);
  }

  printf("Valores do Vetor:");
  for(int count = 0; count < 5; count++) {
    printf(" %d", vetor[count]);
  }
  
  return 0;
}

// 2 - Faça um programa que preencha um vetor de dez elementos númericos e escreva na tela o DOBRO de cada número digitado.
int dobroVetor() {
  int v[10];

  printf("Digite 10 valores: \n");
  for(int c = 0; c < 10; c++) {
    printf("%d valor: ", c+1);
    scanf("%d", &v[c]);
  }

  printf("O dobro de cada número é:");
  for(int c = 0; c < 10; c++) {
     printf(" %d", v[c]*2);
  }
  
  return 0;
}

// 3 - Faça um programa que preencha um vetor de dez números inteiros, SOME todos e exiba o resultado.
int somaVetor() {
  int v[10];
  int soma=0;

  printf("Digite 10 valores: \n");
  for(int c = 0; c < 10; c++) {
    printf("%d valor: ", c+1);
    scanf("%d", &v[c]);
    soma += v[c];
  }
  
  printf("A soma dos números é: %d", soma);

  return 0;
}

// 4 - Encontre o MAIOR elemento de vetor com dez números inteiros
int maiorNumVetor() {
  int v[10];
  int maiorNum=0;

  printf("Digite 10 valores: \n");
  for(int c = 0; c < 10; c++) {
    printf("%d valor: ", c+1);
    scanf("%d", &v[c]);

    if(v[c] > maiorNum) {
      maiorNum = v[c];
    }
  }

  printf("O maior número do Vetor é: %d", maiorNum);
  return 0;
}

// 5 - Faça um programa que leia um vetor de oito posiçoes. Em seguida, leia também dois valores X e Y quaisquer correspondentes a duas posiçoes no vetor. Seu programa deverá exibir a soma dos valores encontrados nas respectivas posiçoes X e Y.
int somaEspecifica() {
  int v[10], soma=0;
  
  return 0;
}


// 6 - Faça um programa que receba do usuário dois arrays, A e B, com 10 números inteiros cada. Crie um novo array C calculando C = A - B. Mostre na tela os dados do array C.
int diminuindoVetor() {
  int vA[10];
  int vB[10];
  int vC[10];

  printf("Digite 10 valores para preencher no vetor A: \n");
  for(int c = 0; c < 10; c++) {
    printf("%d valor: ", c+1);
    scanf("%d", &vA[c]);
  }

  printf("Digite 10 valores para preencher no vetor B: \n");
  for(int c = 0; c < 10; c++) {
    printf("%d valor: ", c+1);
    scanf("%d", &vB[c]);

    vC[c] = vA[c] - vB[c];
  }

  printf("Valores do vetor C: \n");
  for(int c = 0; c < 10; c++) {
    printf("%d ", vC[c]);
  }
  
  return 0;
}

// 7 - Escreva um programa que leia um vetor de 10 posições. Escreva na tela quantos valores PARES foram armazenados nesse vetor.
int numerosPar() {
  int v[10];
  int pares=0;

  printf("Digite 10 valores: \n");
  for(int c = 0; c < 10; c++) {
    printf("%d valor: ", c+1);
    scanf("%d", &v[c]);

    if(v[c] % 2 == 0) {
      pares++;
    }
  }
  
  printf("Foram encontrados %d valores PARES !", pares);
  return 0;
}

// 8 - Crie um programa que leia do teclado seis valores inteiros e em seguida mostre os valores em ordem inversa.
int inverso() {
  int v[6], c;

  printf("Digite 6 valores: \n");
  for(c = 0; c < 6; c++) {
    printf("%d valor: ", c+1);
    scanf("%d", &v[c]);
  }

  for(c = 5; c >= 0; c--) {
    printf("%d ", v[c]);
  }
  
  return 0;
}

// 9 - Faça um programa que preencha um vetor com 10 números reais. Em seguida, calcule e mostre na tela a quantidade de números NEGATIVOS e a soma dos números positivos desse vetor.
int showNegativesAndPlusPositives() {
  float v[10];
  int somaPositivos=0, qntdNegativos=0;
  
  printf("Digite 10 valores c/ negativos: \n");
  for(int c = 0; c < 10; c++) {
    printf("%d valor: ", c+1);
    scanf("%f", &v[c]);

    if(v[c] >= 0) {
      somaPositivos += v[c];
    }else {
      qntdNegativos += 1;
    }
  }
  
  printf("Números do Vetor: ");
  for(int c = 0; c < 10; c++) {
    printf("%.2f ", v[c]);
    
  }
  printf("\nPossui %d números NEGATIVOS.", qntdNegativos);
  printf("\nA soma dos POSITIVOS é %d", somaPositivos);
  
  return 0;
}

// 10 --- NÚMEROS ALETÓRIOS - RAND
int gerarNumsAleat() {
  int qntidade;
  
  // Gerando a semente
  srand(time(NULL));

  printf("Quantidade de números que vão ser gerados até 100: ");
  scanf("%d", &qntidade);
  for(int c = 0; c < qntidade; c++) {
    printf("%d ", rand() % 100);
  }

  return 0;
}

// 11 - Faça um programa que preencha um vetor com quinze números, determine e mostre:
  // a) o maior número e a posição ocupada por ele
  // b) o menor número e a posição ocupada por ele
  // c) A soma das posições e o produto do maior pelo menor
int preenchendoVetorAleat() {
  int v[15], maiorNum=0, menorNum=0;

  // Gerando a semente
  srand(time(NULL));

  printf("Números gerados no Vetor: \n");
  for(int c = 0; c < 15; c++) {
    v[c] = rand() % 100;
    printf("%d ", v[c]);
    
    if(v[c] > maiorNum) {
      maiorNum = v[c];
    }
    if(v[c] > menorNum) {
      menorNum = v[c];
    }
  }

//   for(int c = 0; c < 15; c++) {
    
//   }
  
  printf("O maior número gerado foi: %d - na %d posição", maiorNum, maiorNum );
  printf("O menor número gerado foi: %d - na %d posição", maiorNum, maiorNum );
  
  return 0;
}

// 12 - Faça um programa que preencha um vetor de tamanho 100 com os 100 primeiros números naturais que não são múltiplos de 7. Ao final, imprima esse vetor na tela.
int naoMultiplosDe7() {
  int v[100], c=0, num=1;

  while(c < 100) {
    if(num % 7 != 0) {
      v[c] = num;
      c++;
    }
    num++;
  }

  for(int i = 0; i < 100; i++) {
    printf("%d ", v[i]);
  }
  
  return 0;
}

// 13 - Leia um conjunto de números reais, armazenando-o em vetor. Em seguida, calcule o quadrado de cada elemento de vetor armazenando esse resultado em outro vetor. Os conjuntos têm, no máximo, 20 elementos. Imprima os dois conjuntos de números.

// 14 - Faça um programa que leia um vetor de 10 posições. Verifique se existem valores iguais e os escreva na tela. Parte 2: Salve em um vetor a parte sem repeti-los e mostre ao final.
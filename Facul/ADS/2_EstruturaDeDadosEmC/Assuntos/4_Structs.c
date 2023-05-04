#include <stdio.h>
#include <stdlib.h>

// 1 - Criar um Struct Acadêmico
typedef struct {
  char *nome;
  char curso[40];
  int matricula;
  int qntd_faltas;
  float nota1, nota2, nota3;
  float media;
} Alunos;

struct aluno {
  char teste[50];
};

int savingStudentData(Alunos salaA[10]) {
  printf("\n---------- Cadastro de 10 Alunos -----------\n\n");
  
  // Capturar Dados
  for(int i = 0; i < 3; i++) {
    salaA[i].nome = (char *) malloc(40 * sizeof(char));
    printf("-- %d° Registro\n", i+1);
    printf("Qual o seu nome? ");
    fgets(salaA[i].nome, 40, stdin);
    // scanf("%s", salaA[i].nome);

    printf("Qual o seu curso? ");
    fgets(salaA[i].curso, 40, stdin);
    // scanf("%s", salaA[i].curso);

    printf("Qual a sua matricula? ");
    scanf("%d", &salaA[i].matricula);

    printf("Quantas vezes você faltou? ");
    scanf("%d", &salaA[i].qntd_faltas);

    printf("Qual a sua primeira nota? ");
    scanf("%f", &salaA[i].nota1);
    printf("Qual a sua segunda nota? ");
    scanf("%f", &salaA[i].nota2);
    printf("Qual a sua terceira nota? ");
    scanf("%f", &salaA[i].nota3);

    salaA[i].media = (salaA[i].nota1 + salaA[i].nota2 + salaA[i].nota3) / 3;
    scanf("%c", (char *) stdin); // to fgets remove new line
  }

  // Imprimir na tela
  for(int i = 0; i < 3; i++) {
    printf("\n--- Dados do %d° aluno\n", i+1);
    printf("Nome: %s\n", salaA[i].nome);
    printf("Curso: %s\n", salaA[i].curso);
    printf("Matricula: %d\n", salaA[i].matricula);
    printf("Quantidade de Faltas: %d\n", salaA[i].qntd_faltas);
    printf("Notas: %f - %f - %f\n", salaA[i].nota1, salaA[i].nota2, salaA[i].nota3);
    printf("Media: %.2f", salaA[i].media);
  }
  
  return 0;
}
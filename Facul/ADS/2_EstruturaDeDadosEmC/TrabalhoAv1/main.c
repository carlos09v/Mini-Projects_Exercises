// Dupla: Carlos Vinicius e João Victor Mendes - 27/04/23

#include <stdio.h>
#include <unistd.h>
#include <time.h>

typedef struct {
  char nome[50];
  char matricula[14];
  float nota1, nota2, nota3;
  float media;
  int qntd_faltas;
} aluno;

int menu(){
  int opc = 0;
  
  printf("\n========================= MENU =========================\n"
  "1 - Cadastrar Aluno\n"
  "2 - Alterar Aluno\n"
  "3 - Listar Alunos\n"
  "4 - Listar Alunos Aprovados\n"
  "5 - Listar Alunos Reprovados por média\n"
  "6 - Listar Alunos Reprovados por falta\n"  
  "7 - Sair\n");

  printf("\nQual a opção? ");
  scanf("%d", &opc);
  while (opc < 1 || opc > 7) {
    printf("Opção Inválida ! Digite um número de 1 a 7 :)");
    printf("\nQual a opção? ");
    scanf("%d", &opc);
  }

  return opc;
}

// Criar/Cadastrar Aluno
void registerStudent(aluno sala[10]){
  time_t t;
  t = time(NULL);
  struct tm tm = *localtime(&t);

  printf("--------- Cadastro de Aluno(a) ---------\n");
  for(int c = 0; c < 10; c++) {
    if(sala[c].nome[0] == NULL) { // Verificar se está vazio
      printf("Qual o nome? ");
      fgets(sala[c].nome, 50, stdin);

      snprintf(sala[c].matricula, 14, "%d%d%d%d%d%d", tm.tm_year+1900, tm.tm_mday, tm.tm_mon+1, tm.tm_hour, tm.tm_min, tm.tm_sec); // Generate Matricula as a String

      printf("\nQual a sua primeira nota? ");
      scanf("%f", &sala[c].nota1);
      printf("\nQual a sua segunda nota? ");
      scanf("%f", &sala[c].nota2);
      printf("\nQual a sua terceira nota? ");
      scanf("%f", &sala[c].nota3);

      printf("\nQuantas vezes você faltou? ");
      scanf("%d", &sala[c].qntd_faltas);
  
      sala[c].media = (sala[c].nota1 + sala[c].nota2 + sala[c].nota3) / 3;
      printf("Dados cadastrados com sucesso!\n"), sleep(2);
      scanf("%c", (char *) stdin); // to fgets remove new line
      break;
    }
  }
  
}

// Listar Alunos
void showStudents(aluno sala[10]){
  for(int c = 0; c < 10; c++) {
    if(sala[c].qntd_faltas != NULL) { // Verificar se não está vazio
      printf("= Cadastro ================================\n");
      printf("\t- Nome: %s\n", sala[c].nome);
      printf("\t- Matricula: %s\n", sala[c].nome);
      printf("\t- Notas: [%.1f, %.1f, %.1f]\n", sala[c].nota1, sala[c].nota2, sala[c].nota3);
      printf("\t- Quantidade de Faltas: %d", sala[c].qntd_faltas);
      printf("\t- Media: %.1f\n", sala[c].media);
    }
  }
  
}


int mainTrabalhoAv1(){
  aluno Sala[10];
  int opc = menu();

  switch (opc) {
    case 1:
      registerStudent(Sala);
      break;
    case 2:
      mainTrabalhoAv1();
      break;
    case 3:
      showStudents(Sala);
      mainTrabalhoAv1();
      break;
    case 4:
      mainTrabalhoAv1();
      break;
    case 5:
      mainTrabalhoAv1();
      break;
    case 6:
      mainTrabalhoAv1();
      break;
    case 7:
      printf("Encerrando...\n"), sleep(3);
      break;
  }

  return 0;
}
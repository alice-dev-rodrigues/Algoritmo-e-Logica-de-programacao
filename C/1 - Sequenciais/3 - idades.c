#include <stdio.h>
#include <string.h>

int main() {

    int idade1, idade2;
    double media;
    char nome1[50], nome2[50];
    char buf[100];

    printf("Dados da primeira pessoa:\n");
    printf("Nome: ");
    fgets(nome1, 50, stdin);
    nome1[strcspn(nome1, "\n")] = '\0';
    printf("Idade: ");
    fgets(buf, 100, stdin);
    sscanf(buf, "%d", &idade1);

    printf("Dados da segunda pessoa:\n");
    printf("Nome: ");
    fgets(nome2, 50, stdin);
    nome2[strcspn(nome2, "\n")] = '\0';
    printf("Idade: ");
    fgets(buf, 100, stdin);
    sscanf(buf, "%d", &idade2);
    
    media = ((double) idade1 + idade2) / 2;

    printf("A idade media de %s e %s eh de %.1lf", nome1, nome2, media);

    return 0;
}
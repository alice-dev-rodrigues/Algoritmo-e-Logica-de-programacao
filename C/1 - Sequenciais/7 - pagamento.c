#include <stdio.h>
#include <string.h>


int main(){

    char nome[50];
    char buffer[100];
    float valor, pagamento;
    int horas;

    printf("Nome: ");
    fgets(nome, 50, stdin);
    nome[strcspn(nome, "\n")] = '\0'; 

    printf("Valor por hora: ");
    fgets(buffer, 100, stdin);
    sscanf(buffer, "%f", &valor);

    printf("Horas trabalhadas: ");
    fgets(buffer, 100, stdin);
    sscanf(buffer, "%d", &horas);

    pagamento = valor * horas;

    printf("O pagamento para %s deve ser de R$%.2f", nome, pagamento);




    return 0;
}
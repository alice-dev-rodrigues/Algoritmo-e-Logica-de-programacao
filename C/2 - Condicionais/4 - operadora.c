#include <stdio.h>

int main() {

    int minutos, excedencia;
    double valor;

    printf("Digite a quantidade de minutos: ");
    scanf("%d", &minutos);

    if (minutos < 100) {
        printf("Valor a pagar: R$ 50.00");
    }
    else {
        excedencia = minutos - 100;
        valor = 50 + (double) excedencia * 2;
        printf("Valor a pagar: R$ %.2lf", valor);
    }

    return 0;
}
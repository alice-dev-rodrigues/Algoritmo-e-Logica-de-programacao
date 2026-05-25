#include <stdio.h>

int main() {
    
    int codigo, quant;
    double valor;

    printf("Codigo do produto comprado: ");
    scanf("%d", &codigo);
    printf("Quantidade comprada: ");
    scanf("%d", &quant);

    if (codigo == 1) {
        valor = quant * 5.00;
    }
    else if (codigo == 2) {
        valor = quant * 3.50;
    }
    else if (codigo == 3) {
        valor = quant * 4.80;
    }
    else if (codigo == 4) {
        valor = quant * 8.90;
    }
    else {
        valor = quant * 7.32;
    }

    printf("Valor a pagar: R$ %.2lf", valor);
    
    return 0;
}
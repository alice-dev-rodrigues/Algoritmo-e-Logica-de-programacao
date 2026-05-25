#include <stdio.h>

int main() {
    
    double preco, quant, dinheiro, troco;

    printf("Preco unitario do produto: ");
    scanf("%lf", &preco);
    printf("Quantidade comprada: ");
    scanf("%lf", &quant);
    printf("Dinheiro recebido: ");
    scanf("%lf", &dinheiro);

    troco = dinheiro - preco * quant;

    if (troco > 0) {
        printf("TROCO = %.2lf", troco);
    }
    else {
        printf("DINHEIRO INSUFICIENTE. FALTAM %.2lf REAIS", preco * quant - dinheiro);
    }

    return 0;
}
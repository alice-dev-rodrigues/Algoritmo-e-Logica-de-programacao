#include <stdio.h>

int main(){

    int distancia;
    double combustivel, media;

    printf("Distancia percorrida: ");
    scanf("%d", &distancia);

    printf("Combustivel gasto: ");
    scanf("%lf", &combustivel);

    media = distancia / combustivel;

    printf("Consumo medio = %.3lf", media);

    return 0;
}
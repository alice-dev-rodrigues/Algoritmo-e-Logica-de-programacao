#include <stdio.h>
#include <math.h>

int main() {

    double segundos, minutos, horas, duracao;

    printf("Digite a duracao em segundos: ");
    scanf("%lf", &duracao);

    horas = duracao / 3600;
    minutos = floor(fmod(duracao, 3600) / 60);
    segundos = fmod(duracao, 60);

    printf("%.0lf:%.0lf:%.0lf", horas, minutos, segundos);

    return 0;
}
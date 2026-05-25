#include <stdio.h>

int main() {

    double glicose;

    printf("Digite a medida da glicose: ");
    scanf("%lf", &glicose);

    if (glicose <= 100) {
        printf("normal");
    }
    else if (glicose > 100 && glicose <= 140) {
        printf("elevado");
    }
    else {
        printf("diabetes");
    }

    return 0;
}
#include <stdio.h>

int main() {
    
    char temperatura;
    double fahrenheit, celsius;

    printf("Voce vai digitar a temperatura em qual escala (C/F)? ");
    scanf("%c", &temperatura);

    if (temperatura == 'F') {
        printf("Digite a temperatura em Fahrenheit: ");
        scanf("%lf", &fahrenheit);
        celsius =  (5.0 / 9.0) * (fahrenheit - 32.0);
        printf("Temperatura equivalente em Celsius: %.2lf", celsius);
    }
    else {
        printf("Digite a temperatura em Celsius: ");
        scanf("%lf", &celsius);
        fahrenheit = 1.8 * celsius + 32.0;
        printf("Temperatura equivalente em Fahrenheit: %.2lf", fahrenheit);

    }

    return 0;
}
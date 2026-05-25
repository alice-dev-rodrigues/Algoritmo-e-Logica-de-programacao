#include <stdio.h>

int main() {
    
    double n1, n2, notafinal;

    printf("Digite a primeira nota: ");
    scanf("%lf", &n1);
    printf("Digite a segunda nota: ");
    scanf("%lf", &n2);
    notafinal = n1 + n2;
    printf("NOTA FINAL = %.1lf\n", notafinal);

    if (notafinal < 60) {
        printf("REPROVADO");
    }
    return 0;
}
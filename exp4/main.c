#include<stdio.h>


int main(){
    printf("--- Power Calculator ---\n");
    printf("Enter a number:");
    int base;
    scanf("%d", &base);
    printf("Enter a power:");
    int power;
    scanf("%d", &power);
    
    int result = 1;
    for(int i = 0; i < power; i++){
        result *= base;
    }
    printf("%d to the power of %d is %d.\n", base, power, result);
    return 0;
}
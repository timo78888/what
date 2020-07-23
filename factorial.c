//factorials

#include <stdio.h>

int factorial(int n)
{
    int result = 1;
    for (int i = n; i > 0; i--)
    {
        result *= i;
    }
    return result;
}

int main(void)
{
    printf("Enter number to calculate factorial of: ");
    int number;
    scanf("%i", &number);
    if (number < 0)
    {
        printf("Number needs to be non-negative\n");
        return 1;
    }
    else
    {
        printf("Factorial of %i is %i\n", number, factorial(number));
        return 0;
    }
}

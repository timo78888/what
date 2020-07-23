//use mechanic's rule to approximate square roots, without using math.h
#include <stdio.h>
double magnitude(double x)
{
    double result;
    if (x < 0)
    {
        result = -1 * x;
    }
    else
    {
        result = x;
    }
    return result;
}

int main(void)
{
    double input;
    int steps;
    printf("Approximate square root of: ");
    scanf("%lf", &input);
    printf("Number of steps to use for approximation: ");
    scanf("%i", &steps);
    if (steps <= 0)
    {
       printf("Number of steps must be positive!\n");
       return 1;
    }

    double inpt = magnitude(input);
    double x = (double) inpt;

    for (int i = 0; i < steps; i++)
    {
        x = 0.5 * (x + inpt/x);
    }

    if (input >= 0)
    {
        printf("%.15g\n", x);
    }
    else
    {
        printf("%.15gi\n", x);
        printf("(i denotes the imaginary unit)\n");
    }
    return 0;
}
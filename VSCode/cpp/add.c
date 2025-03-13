#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

int main(int argc, char* argv[]) {
    int b = 2;
    int c = add(a, b);
    printf("c = %d\n", c);
    return 0;
}
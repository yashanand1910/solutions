#include <stdio.h>

int main() {
  short arr[] = {0x1234, 0x8326, 0x9742, 0x4200, 0x1521, 0x3531};

  printf("arr addr: %lx\n", (unsigned long)arr);

  printf("2: %lx\n", *((long *)&arr[2]));
  printf("3: %x\n", (unsigned char)*((char *)&arr[3]));
  printf("4: %x\n", (unsigned char)*(((char *)arr) + 3));
  printf("5: %x\n", ((int *)arr)[1]);
}

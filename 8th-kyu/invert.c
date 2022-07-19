#include <stddef.h>

void invert(int *values, size_t values_size)
{
  for (int x = 0; x < values_size; values[x++] *= -1);
}

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while -program that creates an infinite loop making
 * programs hang
 * Return: void.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main = Program that creats five zombies processes
 * Return: Sucess always (0)
 */
int main(void)
{
	int xty = 0;
	pid_t alx;

	while (xty <= 4)
	{
		alx = fork();
		if (!alx)
			return (0);
		printf("Zombie process created, PID: %u\n", alx);
		xty = xty + 1;
	}
	if (alx != 0)
		infinite_while();
	else
		return (0);
	return (0);
}

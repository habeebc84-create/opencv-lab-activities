#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main()
{
    pid_t pid;

    pid = fork();   // Create a new process

    if (pid < 0)
    {
        printf("Process creation failed!\n");
        return 1;
    }
    else if (pid == 0)
    {
        // Child Process
        printf("\n--- Child Process ---\n");
        printf("Child PID  : %d\n", getpid());
        printf("Parent PID : %d\n", getppid());
    }
    else
    {
        // Parent Process
        printf("\n--- Parent Process ---\n");
        printf("Parent PID : %d\n", getpid());
        printf("Parent's Process PID : %d\n", getppid());
        printf("Child PID  : %d\n", pid);
    }

    return 0;
}  
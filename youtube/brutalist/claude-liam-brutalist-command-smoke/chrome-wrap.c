#include <unistd.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

#define CHROME "/Users/bear/node_modules/.remotion/chrome-headless-shell/mac-arm64/chrome-headless-shell-mac-arm64/chrome-headless-shell"

int main(int argc, char *argv[]) {
    char **new_argv = malloc((argc + 4) * sizeof(char *));
    if (!new_argv) return 1;
    new_argv[0] = CHROME;
    new_argv[1] = "--single-process";
    new_argv[2] = "--in-process-gpu";
    new_argv[3] = "--disable-crash-reporter";
    for (int i = 1; i < argc; i++) {
        new_argv[i + 3] = argv[i];
    }
    new_argv[argc + 3] = NULL;
    execv(CHROME, new_argv);
    perror("execv failed");
    return 1;
}

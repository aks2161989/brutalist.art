#include <unistd.h>
#include <stdlib.h>
int main(int argc, char *argv[]) {
    const char *chrome = "/Users/bear/node_modules/.remotion/chrome-headless-shell/mac-arm64/chrome-headless-shell-mac-arm64/chrome-headless-shell";
    const char *extra[] = {"--single-process","--in-process-gpu",
        "--disable-crash-reporter","--disable-features=MojoIpcz",
        "--no-sandbox","--disable-dev-shm-usage",NULL};
    int n = 6, total = 1+n+(argc-1)+1;
    char **nargv = malloc(total*sizeof(char*));
    nargv[0] = (char*)chrome;
    for (int i=0;i<n;i++) nargv[1+i]=(char*)extra[i];
    for (int i=1;i<argc;i++) nargv[n+i]=argv[i];
    nargv[n+argc]=NULL;
    execv(chrome,nargv);
    return 1;
}

#include <unistd.h>

int main(void) {

execlp("python3", "python3",  "/opt/fancontrol/src/fan.py", (char*)0);

  return 0;
}

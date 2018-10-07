/* 编写一个程序，从标准输入读取几行输入。每行输入都要打引到标准输出上，前面要加上行号。编写这个程序时要试图让程序能够处理的输入行的长度没有限制 */
#include <stdio.h>
#include <stdlib.h>

int main(void) {
	int ch;
	int line;
	int at_begining;

	line = 0;
	at_begining = 1;

	while((ch=getchar()) != EOF) {
		if(at_begining == 1) {
			at_begining = 0;
			line += 1;
			printf("%d: ", line);
		}

	putchar(ch);
	if(ch == '\n')
		at_begining = 1;
	}

	return EXIT_SUCCESS;
} 
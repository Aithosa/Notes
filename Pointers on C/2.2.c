/* 编写一个程序， 从标准输入读取C源代码，并验证所有的花括号都正确成对出现。
注：你不必担心注释内部、字符串常量内部和字符常量形式的花括号 */

#include <stdio.h>
#include <stdlib.h>

int main(void) {
	int ch;
	int braces;

	braces = 0;

	// 逐字符读取
	while((ch=getchar()) != EOF) {
		// 左花括号始终是合法的
		if(ch == '{')
			braces += 1;
		
		// 右花括号只有当他和一个左花括号匹配时才是合法的
		if(ch == '}')
			if(braces ==0)
				printf("Extra closing brace!\n");
			else
				brace -= 1;
	}

	// 没有更多输入：验证不存在任何未被匹配的左花括号
	if(braces > 0)
		printf("%d unmatched openoing brace(s)!\n", braces);

	return EXIT_SUCCESS;
}
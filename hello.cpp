#include "hello.h"
hello::hello() {
	message = "hello world";
}

void hello::sayHi() {
	for (int i = 0; i < 5; i++) {
		std::cout << message[i];
	}
	std::cout << std::endl;
	return;
}
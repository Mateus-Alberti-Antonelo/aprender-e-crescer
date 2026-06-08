#include <iostream>
#include <string>

class Animal {
public:
    void fazerSom() {
        std::cout << "Barulho generico" << std::endl;
    };

    void fazerSom( std::string som ) {
        std::cout << som << std::endl;
    };
};

int main() {
    Animal animal;
    animal.fazerSom();
    animal.fazerSom("meu som diferente");
}

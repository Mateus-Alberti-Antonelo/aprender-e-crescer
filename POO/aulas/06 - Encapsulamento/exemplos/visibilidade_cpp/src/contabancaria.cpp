#include "contabancaria.h"

ContaBancaria::ContaBancaria(const int numeroConta ) : numeroConta(numeroConta) {}

void ContaBancaria::depositar(const float valor) {
    this->saldo += valor;
}

void ContaBancaria::sacar(const float valor) {
    this->saldo -= valor;
}

float ContaBancaria::consultarSaldo() const {
    return this->saldo;
}


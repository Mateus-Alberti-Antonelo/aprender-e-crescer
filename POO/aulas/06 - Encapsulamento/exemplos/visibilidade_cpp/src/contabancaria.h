class ContaBancaria {
public:
    explicit ContaBancaria( const int numeroConta );

    void depositar( const float valor );
    void sacar( const float valor);
    float consultarSaldo() const;

protected:
    int numeroConta;

private:
    float saldo;
};
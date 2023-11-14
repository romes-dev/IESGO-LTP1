extern crate regex;

use regex::Regex;

fn main() {
    // Texto de exemplo contendo endereços de e-mail
    let texto = "Olá, meu e-mail é exemplo1@email.com, e o outro é contato@email.com.br.";

    // Define o padrão da expressão regular para encontrar endereços de e-mail
    let padrao = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b";
    // Este padrão corresponde a um e-mail e utiliza metacaracteres:
    // - '\b' para indicar limites de palavra (garante que o que precede e o que segue seja não alfanumérico)
    // - '[A-Za-z0-9._%+-]+' corresponde ao nome do usuário (parte local do e-mail)
    // - '@' corresponde ao caractere "@" literal
    // - '[A-Za-z0-9.-]+' corresponde ao nome do domínio (parte do domínio do e-mail)
    // - '\.' corresponde ao caractere "." literal (é necessário escapar com '\')
    // - '[A-Z|a-z]{2,}' corresponde à extensão do domínio (como com, com.br, etc.)

    // Cria uma instância de Regex com o

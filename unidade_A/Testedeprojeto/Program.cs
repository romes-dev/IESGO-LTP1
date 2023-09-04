using System;

public class AFDMultiplosDe3
{
    // Definição dos estados
    private enum Estado
    {
        Q0,
        Q1,
        Q2
    }

    private Estado estadoAtual;

    public AFDMultiplosDe3()
    {
        estadoAtual = Estado.Q0; // Definindo o estado inicial
    }

    public bool ProcessarEntrada(string entrada)
    {
        foreach (char digito in entrada)
        {
            switch (estadoAtual)
            {
                case Estado.Q0:
                    if (digito == '0')
                    {
                        estadoAtual = Estado.Q0; // Continua em Q0
                    }
                    else if (digito == '1')
                    {
                        estadoAtual = Estado.Q1; // Move para Q1
                    }
                    break;

                case Estado.Q1:
                    if (digito == '0')
                    {
                        estadoAtual = Estado.Q2; // Move para Q2
                    }
                    else if (digito == '1')
                    {
                        estadoAtual = Estado.Q0; // Move para Q0
                    }
                    break;

                case Estado.Q2:
                    if (digito == '0')
                    {
                        estadoAtual = Estado.Q1; // Move para Q1
                    }
                    else if (digito == '1')
                    {
                        estadoAtual = Estado.Q2; // Continua em Q2
                    }
                    break;
            }
        }

        // Verifica se o estado final é Q0 (aceitação)
        return estadoAtual == Estado.Q0;
    }
}

class Program
{
    static void Main()
    {
        AFDMultiplosDe3 afd = new AFDMultiplosDe3();

        Console.Write("Insira um número binário: ");
        string entrada = Console.ReadLine();

        bool aceito = afd.ProcessarEntrada(entrada);

        if (aceito)
        {
            Console.WriteLine("Aceito: O número binário é múltiplo de 3.");
        }
        else
        {
            Console.WriteLine("Rejeitado: O número binário não é múltiplo de 3.");
        }
    }
}

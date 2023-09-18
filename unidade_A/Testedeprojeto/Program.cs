using System;

namespace ComparacaoDeValores
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Por favor, insira sua idade:");
            int idade = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Por favor, insira sua altura em centímetros:");
            int altura = Convert.ToInt32(Console.ReadLine());

            if (idade > 18 && altura > 170)
            {
                Console.WriteLine("Você é maior de 18 anos e tem mais de 170 cm de altura.");
            }
            else if (idade > 18 || altura > 170)
            {
                if (idade > 18)
                {
                    Console.WriteLine("Você é maior de 18 anos.");
                }
                if (altura > 170)
                {
                    Console.WriteLine("Você tem mais de 170 cm de altura.");
                }
            }
            else
            {
                Console.WriteLine("Você não atende a nenhum dos critérios acima.");
            }

            if (idade == 21)
            {
                Console.WriteLine("Você tem exatamente 21 anos!");
            }
            if (idade != 21)
            {
                Console.WriteLine("Você não tem 21 anos.");
            }
        }
    }
} 


using System;

namespace ComparacaoDeValores
{
    class Program
    {
        static void Main(string[] args)
        {
            int idade = GetValidInput("Por favor, insira sua idade:");
            int altura = GetValidInput("Por favor, insira sua altura em centímetros:");

            EvaluateAndPrintMessage(idade, altura);
        }

        static int GetValidInput(string message)
        {
            Console.WriteLine(message);
            int output;
            while (!int.TryParse(Console.ReadLine(), out output))
            {
                Console.WriteLine("Entrada inválida. Por favor, insira um número inteiro.");
            }
            return output;
        }

        static void EvaluateAndPrintMessage(int idade, int altura)
        {
            string message = "";

            if (idade > 18 && altura > 170)
            {
                message = "Você é maior de 18 anos e tem mais de 170 cm de altura.";
            }
            else if (idade > 18 && altura <= 170)
            {
                message = "Você é maior de 18 anos, mas tem menos de 170 cm de altura.";
            }
            else if (idade <= 18 && altura > 170)
            {
                message = "Você é menor de 18 anos, mas tem mais de 170 cm de altura.";
            }
            else
            {
                message = "Você não atende a nenhum dos critérios acima.";
            }

            if (idade == 21)
            {
                message += " Você tem exatamente 21 anos!";
            }
            else
            {
                message += " Você não tem 21 anos.";
            }

            Console.WriteLine(message);
        }
    }
}

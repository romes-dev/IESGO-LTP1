using System;

namespace Programa
{
    public static class Principal
    {
        public static void Main(string[] args)
        {
            Console.Write("Qual o seu nome: ");
			string nome = Console.ReadLine();
			
			Console.WriteLine("Qual o seu nome: ");
			string sobrenome = Console.ReadLine();
			
			Console.WriteLine($"Seu nome completo é: {nome} {sobrenome}");
			
			
        }
    }
}
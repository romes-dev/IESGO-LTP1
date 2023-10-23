using System;
using System.Collections.Generic;

public class Livro 
{
    public string Titulo { get; set; }
    public string Autor { get; set; }
    public string ISBN { get; set; }

    public void ExibirDetalhes()
    {
        Console.WriteLine($"Título: {Titulo}");
        Console.WriteLine($"Autor: {Autor}");
        Console.WriteLine($"ISBN: {ISBN}");
    }
}

public class Biblioteca
{
    private List<Livro> livros = new List<Livro>();

    public void AdicionarLivro(Livro livro)
    {
        livros.Add(livro);
    }

    public void ExibirLivros()
    {
        foreach(var livro in livros)
        {
            Console.WriteLine("#####################");
            livro.ExibirDetalhes();
            Console.WriteLine("#####################");
        }
    }
}

public class Program
{
    public static void Main()
    {
        var livro01 = new Livro 
        { 
            Titulo = "Harry Potter and the Cursed Child - Parts One and Two (Special Rehearsal Edition)", 
            Autor = "J. K. Rowling", 
            ISBN = "1234-9843"  
        }; 

        var biblioteca = new Biblioteca();
        biblioteca.AdicionarLivro(livro01);

        biblioteca.ExibirLivros(); 
    }
}

package exemplo;

public class Livro {

    public String titulo;
    public String autores;
    public int ano; // ano de publicação
    public String editora;
    
    public String ToSTRING() {
        return 
            String.format("Livro: %s, de %s, publicado por %s em %d",
            this.titulo, this.autores, this.editora, this.ano);
    }
    
    public Livro(String tit, String aut, int ano, String ed) {
        this.titulo = tit;
        this.autores = aut;
        this.ano = ano;
        this.editora = ed;               
    }
    
    public static void main(String[] args) {
        Livro exemplo = new Livro("O homem mais rico da Babilônia", 
                "George S Clason", 2017, "Harper Business");
        System.out.println(exemplo);        
    }
    
}

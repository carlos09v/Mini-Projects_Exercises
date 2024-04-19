import produto.ListaProdutos;
import produto.Produto;
import produto.ProdutoImportado;

public class App {
    public static void main(String[] args) throws Exception {
        ListaProdutos lista = new ListaProdutos();

        Produto produto1 = new Produto("Arroz", 10.0);
        Produto produto2 = new Produto("Feijão", 8.0);
        ProdutoImportado produto3 = new ProdutoImportado("Smartphone", 1500.0, 1);
        ProdutoImportado produto4 = new ProdutoImportado("Chocolate", 5.0, 2);

        // Adicionando os produtos à lista
        lista.insereProduto(produto1);
        lista.insereProduto(produto2);
        lista.insereProduto(produto3);
        lista.insereProduto(produto4);

        // Imprimindo o relatório dos produtos armazenados
        System.out.println("Relatório dos Produtos Armazenados:");
        lista.imprimirProdutos();
        
        produto1.exibirRelatorio();
        produto3.exibirRelatorio();
    }
}

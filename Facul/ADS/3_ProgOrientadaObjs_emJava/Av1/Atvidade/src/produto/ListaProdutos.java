package produto;

public class ListaProdutos {
    private Produto[] produtos;
    private int tamanho;

    // Construtor
    public ListaProdutos() {
        this.produtos = new Produto[10]; // Array de produtos com tamanho máximo de 10 elementos
        this.tamanho = 0; // Inicializa o tamanho como 0
    }

    // Método para inserir um produto na lista
    public void insereProduto(Produto p) {
        if (tamanho < produtos.length) {
            produtos[tamanho] = p; // Insere o produto no próximo índice disponível
            tamanho++; // Incrementa o tamanho da lista
        } else {
            System.out.println("A lista de produtos está cheia. Não é possível adicionar mais produtos.");
        }
    }

    // Método para imprimir todos os produtos
    public void imprimirProdutos() {
        System.out.println("Produtos Nacionais:");
        for (int i = 0; i < tamanho; i++) {
            if (produtos[i] instanceof Produto) {
                System.out.println("- " + produtos[i].getNome());
            }
        }
        
        System.out.println("Produtos Importados:");
        for (int i = 0; i < tamanho; i++) {
            if (produtos[i] instanceof ProdutoImportado) {
                System.out.println("- " + produtos[i].getNome());
            }
        }
    }
}

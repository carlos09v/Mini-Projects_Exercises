package produto;
 
public class Produto {
    private String nome; 
    private double preco; 
    
    public Produto(String nome, double preco) {
        this.nome = nome;
        this.preco = preco;
    }

    // Gets e Setters
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }

    public double getPreco() {
        return preco;
    }
    public void setPreco(double preco) {
        this.preco = preco;
    }


    // Método para calcular o imposto
    public double calcularImposto() {
        if (preco < 100.00) {
            return preco * 0.05; // Imposto de 5% se o preço for menor que R$ 100,00
        } else {
            return preco * 0.10; // Imposto de 10% se o preço for maior que R$ 100,00
        }
    }

    // Método para exibir um relatório
    public void exibirRelatorio() {
        double imposto = calcularImposto();
        System.out.println("Nome do Produto: " + nome);
        System.out.println("Preço: R$ " + preco);
        System.out.println("Imposto Pago: R$ " + imposto);
    }
}

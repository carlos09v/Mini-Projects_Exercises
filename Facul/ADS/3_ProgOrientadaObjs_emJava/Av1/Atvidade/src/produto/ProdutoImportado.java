package produto;

public class ProdutoImportado extends Produto {
    private int tipo; // 1 - eletrônico, 2 - alimento, 3 - outros

    // Construtor
    public ProdutoImportado(String nome, double preco, int tipo) {
        super(nome, preco);
        this.tipo = tipo;
    }

    @Override
    public double calcularImposto() {
        double imposto;
        switch (tipo) {
            case 1: // Eletrônico
                imposto = getPreco() * 0.35;
                break;
            case 2: // Alimento
                imposto = getPreco() * 0.15;
                break;
            case 3: // Outros
            default:
                imposto = getPreco() * 0.20;
                break;
        }
        return imposto;
    }

    @Override
    public void exibirRelatorio() {
        double imposto = calcularImposto();
        System.out.println("Nome do Produto: " + getNome());
        System.out.println("Preço: R$ " + getPreco());
        System.out.println("Imposto Pago: R$ " + imposto);
    }
}

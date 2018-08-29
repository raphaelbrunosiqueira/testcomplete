import App
import Order
import Principal

def CalcularValorDoDescontoTotalEProduto():
  #Abertura da aplicação
  App.AbrirOrders()
    
  #Acesso ao formulário de orders
  Principal.AcessarFormularioDeOrders()
  
#  for item in [Project.Variables.dadosDeTeste.RowCount]:
#    item = 0 
#    Order.EscolherProduto(Project.Variables.dadosDeTeste.Produto[item])
#    Order.LimparCampoQuantidade()
#    Order.DigitarQuantidade(Project.Variables.dadosDeTeste.Quantidade[item])
#    Order.DigitarNomeCliente('Raphael')
#    Order.DigitarNomeRua('Frei Matheus')
#    Order.PreencherCartao('999999999999')
#    Order.SelecionarMastercard()
#    Order.DigitarNomeCidade('Brusque')s
#    Order.ValidarPreco(Project.Variables.dadosDeTeste.PrecoEsperado[item])
#    Order.ClickCampoDesconto()
#    Order.ValidarDesconto(Project.Variables.dadosDeTeste.DescontoEsperado[item])
#    Order.ValidarTotal(Project.Variables.dadosDeTeste.TotalEsperado[item])

  ArquivoCSV = DDT.CSVDriver('D:\\TestCompleteProjetos\\testcomplete\\Dados_de_teste.csv')
  while not ArquivoCSV.EOF :
    Order.EscolherProduto(ArquivoCSV.Value['produto'])
    Order.LimparCampoQuantidade()
    Order.DigitarQuantidade(ArquivoCSV.Value['quantidade'])
    Order.DigitarNomeCliente('Raphael')
    Order.DigitarNomeRua('Frei Matheus')
    Order.PreencherCartao('999999999999')
    Order.SelecionarMastercard()
    Order.DigitarNomeCidade('Brusque')
    Order.ValidarPreco(ArquivoCSV.Value['precoesperado'])
    Order.ClickCampoDesconto()
    Order.ValidarDesconto(ArquivoCSV.Value['descontoesperado'])
    Order.ValidarTotal(ArquivoCSV.Value['totalesperado'])
    ArquivoCSV.Next()

  Order.DigitarDataOrder(Project.Variables.dataAtual)
  Order.ClicarCancelar() 
  App.FecharOrders()
  
def ValidaPrecoMymoney():
  App.AbrirOrders()
  Principal.AcessarFormularioDeOrders()
  Order.EscolherProduto('MyMoney')
  Order.ValidarPreco('$100')
  Order.ClicarCancelar() 
  App.FecharOrders()
  
def ClicaIconeNewOrder():
  App.AbrirOrders()
  Order.ClicarIcone()
  App.FecharOrders()


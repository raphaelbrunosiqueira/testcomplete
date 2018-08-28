import App
import Order
import Principal

def CalcularValorDoDescontoTotalEProduto():
  #Abertura da aplicação
  App.AbrirOrders()
    
  #Acesso ao formulário de orders
  Principal.AcessarFormularioDeOrders()
  
  #Preenchemos o produto e quantidade
  Order.EscolherProduto('ScreenSaver')
  Order.LimparCampoQuantidade()
  Order.DigitarQuantidade(10)
  
  #Validar os valores contidos nos campos
  Order.ValidarPreco('$20')
  Order.ClickCampoDesconto()
  Order.ValidarDesconto('10')
  Order.ValidarTotal('180')
  
  #Digitar a data
  #Order.LimparCampoData()
  Order.DigitarDataOrder('01202018')
  
  #Clicar no botao cancelar
  Order.ClicarCancelar()
  
  #Clique no botão Fechar do Orders 
  App.FecharOrders()

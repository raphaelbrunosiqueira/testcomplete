def EscolherProduto(selecaoproduto):
  Aliases.Orders.OrderForm.Group.ProductNames.ClickItem(selecaoproduto)
  
def LimparCampoQuantidade():
  Aliases.Orders.OrderForm.Group.Quantity.ResetText()

def DigitarQuantidade(quantidade):
  Aliases.Orders.OrderForm.Group.Quantity.Keys(quantidade)
  
def DigitarNomeCliente(cliente):
  Aliases.Orders.OrderForm.Group.Customer.Keys(cliente)

def DigitarNomeRua(rua):
  Aliases.Orders.OrderForm.Group.Street.Keys(rua)
  
def ClicarIcone():
  ImageRepository.Imagens.IconeNewOrder.Click()
  
def PreencherCartao(numero):
  Aliases.Orders.OrderForm.Group.CardNo.Keys(numero)
  
def DigitarNomeCidade(cidade):
  Aliases.Orders.wndOrder.WindowsForms10Window8app033c0d9d.Cidade.SetText(cidade)
  
def SelecionarMastercard():
  Aliases.Orders.OrderForm.Group.MasterCard.Click()
  
def ValidarPreco(preco):
  aqObject.CheckProperty(Aliases.Orders.OrderForm.Group.Price, "wText", cmpEqual, preco)
  
def ClickCampoDesconto():
  Aliases.Orders.OrderForm.Group.Discount.Click()
  
def ValidarDesconto(desconto):
  aqObject.CheckProperty(Aliases.Orders.OrderForm.Group.Discount, "wText", cmpContains, desconto)
  
def ValidarTotal(total):
  aqObject.CheckProperty(Aliases.Orders.OrderForm.Group.groupBox1.Total, "wText", cmpEqual, total)
#--------------------------------------------------------------------  
def LimparCampoData():
  Aliases.Orders.OrderForm.Group.Date.ResetText()  
#--------------------------------------------------------------------  
def DigitarDataOrder(dataOrder):
  Aliases.Orders.OrderForm.Group.Date.Keys(dataOrder)

def ClicarCancelar():
  Aliases.Orders.OrderForm.ButtonCancel.ClickButton()
﻿def GerarDatas():
  #gerar datas dinamicamente
  dataAtual = aqConvert.DateTimeToFormatStr(aqDateTime.Today(), '%m%d%y')
  Project.Variables.dataAtual = dataAtual
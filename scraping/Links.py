from scraping import Link

url1 = "http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=INCO&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000"
url2 = "http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=INNI&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000"
url3 = "http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=INRO&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000"
url4 = "http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=INCE&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000"
url5 = "http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=INBI&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000"
url6 = "http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=IGFO&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000"


link1 = Link()
link1.scrapping(url1)
link1.to_json();

link2 = Link()
link2.scrapping(url2)
link2.to_json();

link3 = Link()
link3.scrapping(url3)
link3.to_json();

link4 = Link()
link4.scrapping(url4)
link4.to_json();

link5 = Link()
link5.scrapping(url5)
link5.to_json();

link6 = Link()
link6.scrapping(url6)
link6.to_json();

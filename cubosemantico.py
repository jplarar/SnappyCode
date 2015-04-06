#----------------------------------------------
# cubosemantico.py
# cubosemantico
# Manuel Calzado Maycotte A00811102
# Juan Paulo Lara Rodriguez A00999823
# CREADO: 18/03/2014
#----------------------------------------------

cubo_semantico = {
  	"ENTERO": {
			"ENTERO": {
				"+":"ENTERO", 
				"-":"ENTERO", 
				"*":"ENTERO", 
				"/":"ENTERO", 
				">":"BOOLEANO", 
				">=":"BOOLEANO",
				"<=":"BOOLEANO",
				"<":"BOOLEANO", 
				"=":"ENTERO",
				"==": "BOOLEANO", 
				"!=":"BOOLEANO",
				"&&":"Error", 
				"||":"Error",
				}, 
			"DECIMAL": {
				"+":"DECIMAL", 
				"-":"DECIMAL", 
				"*":"DECIMAL", 
				"/":"DECIMAL", 
				">":"BOOLEANO", 
				">=":"BOOLEANO",
				"<=":"BOOLEANO",
				"<":"BOOLEANO", 
				"=":"ENTERO", 
				"==": "BOOLEANO",
				"!=":"BOOLEANO",
				"&&":"Error", 
				"||":"Error",
				}, 
			"TEXTO": {
				"+":"Error", 
				"-":"Error", 
				"*":"Error", 
				"/":"Error", 
				">":"Error", 
				">=":"Error",
				"<=":"Error",
				"<":"Error", 
				"=":"Error", 
				"==": "Error",
				"!=":"Error",
				"&&":"Error", 
				"||":"Error",
				}, 
			"BOOLEANO": {
				"+":"Error", 
				"-":"Error", 
				"*":"Error", 
				"/":"Error", 
				">":"Error", 
				">=":"Error",
				"<=":"Error",
				"<":"Error", 
				"=":"Error", 
				"==": "Error",
				"!=":"Error",
				"&&":"Error", 
				"||":"Error",
				},
			"LISTA": {
				"+":"Error", 
				"-":"Error", 
				"*":"Error", 
				"/":"Error", 
				">":"Error", 
				">=":"Error",
				"<=":"Error",
				"<":"Error", 
				"=":"Error", 
				"==": "Error",
				"!=":"Error",
				"&&":"Error", 
				"||":"Error",
				},
			}, 
		"DECIMAL":{
			"ENTERO": {
				"+":"DECIMAL", 
				"-":"DECIMAL", 
				"*":"DECIMAL", 
				"/":"DECIMAL", 
				">":"BOOLEANO", 
				">=":"BOOLEANO",
				"<=":"BOOLEANO",
				"<":"BOOLEANO", 
				"=":"DECIMAL", 
				"==": "BOOLEANO",
				"!=":"BOOLEANO",
				"&&":"Error", 
				"||":"Error",
				}, 
			"DECIMAL": {
				"+":"DECIMAL", 
				"-":"DECIMAL", 
				"*":"DECIMAL", 
				"/":"DECIMAL", 
				">":"BOOLEANO", 
				">=":"BOOLEANO",
				"<=":"BOOLEANO",
				"<":"BOOLEANO", 
				"=":"DECIMAL",
				"==": "BOOLEANO", 
				"!=":"BOOLEANO",
				"&&":"Error", 
				"||":"Error",
				}, 
			"TEXTO": {
				"+":"Error", 
				"-":"Error", 
				"*":"Error", 
				"/":"Error", 
				">":"Error", 
				">=":"Error",
				"<=":"Error",
				"<":"Error", 
				"=":"Error", 
				"==": "Error",
				"!=":"Error",
				"&&":"Error", 
				"||":"Error",
				}, 
			"BOOLEANO": {
				"+":"Error", 
				"-":"Error", 
				"*":"Error", 
				"/":"Error", 
				">":"Error", 
				">=":"Error",
				"<=":"Error",
				"<":"Error", 
				"=":"Error", 
				"==": "Error",
				"!=":"Error",
				"&&":"Error", 
				"||":"Error",
				},
			"LISTA": {
				"+":"Error", 
				"-":"Error", 
				"*":"Error", 
				"/":"Error", 
				">":"Error", 
				">=":"Error",
				"<=":"Error",
				"<":"Error", 
				"=":"Error", 
				"==": "Error",
				"!=":"Error",
				"&&":"Error", 
				"||":"Error",
				},
			}, 
		"TEXTO":{
			"ENTERO": {
				"+":"Error", 
				"-":"Error", 
				"*":"Error", 
				"/":"Error", 
				">":"Error", 
				">=":"Error",
				"<=":"Error",
				"<":"Error", 
				"=":"Error", 
				"==": "Error",
				"!=":"Error",
				"&&":"Error", 
				"||":"Error",
				}, 
			"DECIMAL": {
				"+":"Error", 
				"-":"Error", 
				"*":"Error", 
				"/":"Error", 
				">":"Error", 
				">=":"Error",
				"<=":"Error",
				"<":"Error", 
				"=":"Error", 
				"==": "Error",
				"!=":"Error",
				"&&":"Error", 
				"||":"Error",
				}, 
			"TEXTO": {
				"+":"TEXTO", 
				"-":"Error", 
				"*":"Error", 
				"/":"Error", 
				">":"Error", 
				">=":"Error",
				"<=":"Error",
				"<":"Error", 
				"=":"TEXTO", 
				"==": "BOOLEANO",
				"!=":"BOOLEANO",
				"&&":"Error", 
				"||":"Error",
				}, 
			"BOOLEANO": {
				"+":"Error", 
				"-":"Error", 
				"*":"Error", 
				"/":"Error", 
				">":"Error", 
				">=":"Error",
				"<=":"Error",
				"<":"Error", 
				"=":"Error", 
				"==": "Error",
				"!=":"Error",
				"&&":"Error", 
				"||":"Error",
				},
			"LISTA": {
				"+":"Error", 
				"-":"Error", 
				"*":"Error", 
				"/":"Error", 
				">":"Error", 
				">=":"Error",
				"<=":"Error",
				"<":"Error", 
				"=":"Error", 
				"==": "Error",
				"!=":"Error",
				"&&":"Error", 
				"||":"Error",
				},
			}, 
		"BOOLEANO":{
			"ENTERO": {
				"+":"Error", 
				"-":"Error", 
				"*":"Error", 
				"/":"Error", 
				">":"Error", 
				">=":"Error",
				"<=":"Error",
				"<":"Error", 
				"=":"Error", 
				"==": "Error",
				"!=":"Error",
				"&&":"Error", 
				"||":"Error",
				}, 
			"DECIMAL": {
				"+":"Error", 
				"-":"Error", 
				"*":"Error", 
				"/":"Error", 
				">":"Error", 
				">=":"Error",
				"<=":"Error",
				"<":"Error", 
				"=":"Error", 
				"==":"Error",
				"!=":"Error",
				"&&":"Error", 
				"||":"Error",
				}, 
			"TEXTO": {
				"+":"Error", 
				"-":"Error", 
				"*":"Error", 
				"/":"Error", 
				">":"Error", 
				">=":"Error",
				"<=":"Error",
				"<":"Error", 
				"=":"Error", 
				"==":"Error",
				"!=":"Error",
				"&&":"Error", 
				"||":"Error",
				}, 
			"BOOLEANO": {
				"+":"Error", 
				"-":"Error", 
				"*":"Error", 
				"/":"Error", 
				">":"Error", 
				">=":"Error",
				"<=":"Error",
				"<":"Error", 
				"=":"BOOLEANO", 
				"==":"BOOLEANO",
				"!=":"BOOLEANO",
				"&&":"BOOLEANO", 
				"||":"BOOLEANO",
				},
			"LISTA": {
				"+":"Error", 
				"-":"Error", 
				"*":"Error", 
				"/":"Error", 
				">":"Error", 
				">=":"Error",
				"<=":"Error",
				"<":"Error", 
				"=":"Error", 
				"==": "Error",
				"!=":"Error",
				"&&":"Error", 
				"||":"Error",
				},
			},
		"LISTA":{
			"ENTERO": {
				"+":"Error", 
				"-":"Error", 
				"*":"Error", 
				"/":"Error", 
				">":"Error", 
				">=":"Error",
				"<=":"Error",
				"<":"Error", 
				"=":"Error", 
				"==": "Error",
				"!=":"Error",
				"&&":"Error", 
				"||":"Error",
				}, 
			"DECIMAL": {
				"+":"Error", 
				"-":"Error", 
				"*":"Error", 
				"/":"Error", 
				">":"Error", 
				">=":"Error",
				"<=":"Error",
				"<":"Error", 
				"=":"Error", 
				"==":"Error",
				"!=":"Error",
				"&&":"Error", 
				"||":"Error",
				}, 
			"TEXTO": {
				"+":"Error", 
				"-":"Error", 
				"*":"Error", 
				"/":"Error", 
				">":"Error", 
				">=":"Error",
				"<=":"Error",
				"<":"Error", 
				"=":"Error", 
				"==":"Error",
				"!=":"Error",
				"&&":"Error", 
				"||":"Error",
				}, 
			"BOOLEANO": {
				"+":"Error", 
				"-":"Error", 
				"*":"Error", 
				"/":"Error", 
				">":"Error", 
				">=":"Error",
				"<=":"Error",
				"<":"Error", 
				"=":"Error", 
				"==":"Error",
				"!=":"Error",
				"&&":"Error", 
				"||":"Error",
				},
			"LISTA": {
				"+":"LISTA", 
				"-":"Error", 
				"*":"Error", 
				"/":"Error", 
				">":"Error", 
				">=":"Error",
				"<=":"Error",
				"<":"Error", 
				"=":"Error", 
				"==": "BOOLEANO",
				"!=":"BOOLEANO",
				"&&":"Error", 
				"||":"Error",
				},

			},

		}

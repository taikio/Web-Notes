angular.module("Notas").filter("datahora",function () {
	return function (input) {

		var data = input.split(" ");
		var auxData = data[1].split("-");
		var dataFormatada = [];

		for (var i = auxData.length -1; i >=0; i--){
			dataFormatada.push(auxData[i]);			
		}

		var a = input.split(" ");
		var h = a[2].split(".");
		var hora = h[0];

		var dataHora = '';

		for (var i = 0; i < dataFormatada.length; i++){
			dataHora += dataFormatada[i];
			if (i <2) {
				dataHora += '/';
			}
		}

		dataHora += ' ';
		dataHora += hora; 

		return dataHora; 
	
	};
});
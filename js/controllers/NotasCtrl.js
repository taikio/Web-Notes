angular.module('Notas').controller('NotasCtrl', ['$scope','notasApi','empresasApi', function ($scope,notasApi,empresasApi) {
	$scope.app = "Web Notes";
	$scope.notas = [];
	$scope.empresas = [];

	$scope.criarNota = function (nota) {
		notasApi.adicionarNota(nota).success(function (data) {
			delete $scope.nota;
			$scope.notaForm.$setPristine();
			carregarNotas();
		})
	};

	$scope.cancelar = function () {
		delete $scope.nota;
		$scope.notaForm.$setPristine();
	}

	var carregarNotas = function () {
		notasApi.getNotas().success(function (data) {
			$scope.notas = data;
		}).error(function (err) {
			alert(err);
		})
	};

	var carregarEmpresas = function () {
		empresasApi.getEmpresas().success(function (data) {
			$scope.empresas = data;
		}).error(function (err) {
			alert(err);
		})
	}

	$scope.deletarNotas = function (nota) {
	 	/* var lista = notas.filter(function(nota){
			if (nota.selecionada) return nota;
		}); */

		var lista = [];
		lista.push(nota);
		
		notasApi.deleteNotas(lista).success(function(data){
			carregarNotas();
		}).error(function (err) {
			alert(err);
		});
	};

	$scope.isNotaSelecionada = function(notas){
		return notas.some(function(nota){
			return nota.selecionada;
		});
	};

	oldId = 0;
	$scope.notaSelecionada = function (nota) {
		angular.forEach($scope.notas, function (nota) {
			nota.selecionada = false;
		})


		if (nota.id === oldId) {
			nota.selecionada = !nota.selecionada;
		}else{
			nota.selecionada = true;
		}
		var oldId = nota.id;
		$scope.tituloSelecionada = nota.titulo;		
		$scope.detalhesSelecionada = nota.descricao;
		$scope.dataSelecionada = nota.data;
	}

	carregarNotas();
	carregarEmpresas();
}])
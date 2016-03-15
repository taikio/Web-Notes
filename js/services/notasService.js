angular.module('Notas').factory('notasApi', function ($http,config) {
	var _getNotas = function () {
		return $http.get(config.baseUrl + "/tarefas");
	};

	var _adicionarNota = function (nota) {
		return $http.post(config.baseUrl + "/add", nota);
	};

	var _deleteNotas = function (notas) {
		return $http.post(config.baseUrl + "/delete", notas);
	}

	return {
		getNotas : _getNotas,
		adicionarNota : _adicionarNota,
		deleteNotas : _deleteNotas
	};
});
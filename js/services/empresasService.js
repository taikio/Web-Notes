angular.module('Notas').factory('empresasApi', function ($http,config) {
	var _getEmpresas = function () {
		return $http.get(config.baseUrl + "/empresas");
	};

	return {
		getEmpresas : _getEmpresas
	};
});
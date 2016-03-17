angular.module('Notas').factory('empresasApi', ['$http','config',function ($http,config) {
	var _getEmpresas = function () {
		return $http.get(config.baseUrl + "/empresas");
	};

	return {
		getEmpresas : _getEmpresas
	};
}]);
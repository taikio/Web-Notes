angular.module('Notas').directive('alert', [function () {
	return {
		templateUrl: 'view/alert.html',
		restrict: 'E',
		replace: true,
		transclude: true,
		scope :{
			criterio: '=criterio'
			
		}
	};
}])
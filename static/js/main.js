/*
 * depends on jquery
 */

function clear_validation_errors(form) {
	var inputs = form.find('[name]');
	var form_groups = inputs.closest('.form-group');
	var error_containers = form_groups.find('.with-errors');

	inputs.removeClass('contact__form-error');
	error_containers.empty();
}

function show_validation_errors(form, errors) {
	Object.keys(errors).forEach(function(key) {
		var input = form.find('[name=' + key + ']');
		var form_group = input.closest('.form-group');
		var error_container = form_group.find('.with-errors');

		input.addClass('contact__form-error');
		var error_item = errors[key];
		// there might be many validation errors for 1 field
		var error_array = Array.isArray(error_item) ? error_item : [error_item];
		var first = true;
		error_array.forEach(function(err) {
			if (first) {
				first = false;
			} else {
				error_container.append($('<br>'));
			}
			error_container.append($('<span>' + err + '</span>'));
		});
	});
}

let HMIS = {
    validate: (wrapperElement) => {
        let valid = true;
        $(wrapperElement).find('input, select, textarea,number').each(function () {
            /**
             * Validate if element has required attribute and no value/input given
             */
            if ($(this).attr('required') !== undefined && $(this).val() === "") {
                valid = false;
                $(this).addClass('is-invalid');
                if ($(this).next().hasClass('select2')) {
                    $(this).next().addClass('is-invalid');
                }
            }
            else {
                $(this).removeClass('is-invalid');
            }
        });

        return valid;
    },

    hmisLoading: (bool) => {
        let status = bool === true ? 'show' : 'hide';
        $.LoadingOverlay(status, { text: "Saving..." });
    },

    reloadList: (item) => {
        let newUrl;
        let params = {};

        let form = item.form;
        let slug = form.getAttribute('slug');

        let field = item.name;
        let value = item.value;


        newUrl = window.location.origin + window.location.pathname;
        if (value) {
            newUrl = window.location.origin + window.location.pathname + '?' + field + '=' + value;
            params[field] = value;
        }
        history.pushState({}, null, newUrl);
        loadDatatableList(slug, params);
    },
}
window.HMIS = HMIS;

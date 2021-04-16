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
        let updateUrl;
        let params = {};

        let form = item.form;
        let slug = form.getAttribute('slug');

        let field = item.name;
        let value = item.value;


        updateUrl = window.location.origin + window.location.pathname;
        fullUrl = window.location.href;

        // check if current url already contains some query parameters
        // if it contains , then just append the next parameters 
        if (fullUrl.includes("?")) {

            //check if the field already exists in current url
            // if exits just update the field value, and do not append to url
            if (fullUrl.includes(field)) {
                old_search_params = new URLSearchParams(location.search);

                //check if the selected field has value or not
                // if field value is empty, just remove the paramter from url
                if (value) {
                    old_search_params.set(field, value);
                    new_search_params = '?' + old_search_params.toString();
                } else {
                    old_search_params.delete(field);
                    new_search_params = old_search_params.toString();
                    //if new search params in empty, remove '?' from url
                    if (new_search_params != "") { 
                        new_search_params = '?' + new_search_params;
                    }
                }

                updateUrl = updateUrl + new_search_params;

            } else {
                updateUrl = fullUrl + '&' + field + '=' + value;
            }
            history.pushState({}, null, updateUrl);
            params = Object.fromEntries(new URLSearchParams(location.search));
        } else {
            // if current url doesnot contains any query parameters, then add new paramaters
            updateUrl = updateUrl + '?' + field + '=' + value;
            history.pushState({}, null, updateUrl);
            params = Object.fromEntries(new URLSearchParams(location.search));
        }

        // reload datatable according to selected filters
        loadDatatableList(slug, params);
    },

    clearFilter: (item) => {
        let slug = item.getAttribute('slug');

        if (slug != '' && window.location.href.includes('?')) {
            updateUrl = window.location.origin + window.location.pathname;
            
            $('.filter-field').val('').trigger('change');
            history.pushState({}, null, updateUrl);
            loadDatatableList(slug);
        }
    }
}
window.HMIS = HMIS;

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
}
window.HMIS = HMIS;

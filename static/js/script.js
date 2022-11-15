// Navbar class gets applied
const nav = document.querySelector('nav');

window.addEventListener('scroll', () => {
    if ((window.scrollY >= 50)) {
        nav.classList.add('scrolled');
    } else {
        nav.classList.remove('scrolled');
    }
})

function datePicker() {
    $("#id_requested_date").datepicker({
        dateFormat: 'dd/mm/yy'
    });
}

// Remove disabled attribute so that the form can be submitted without throwing errors
function removeDisableAttrOnSubmit() {
    $("#customer-details-form").one('submit', (function (e) {
        e.preventDefault();
        var $this = $(this);
        $("#customer-details-form>.full-form>#div_id_email>.controls>.emailinput").attr("disabled", false);
        $this.submit();
    }));
}


// Opens the modal on delete_booking
function deleteModal() {
    $("#delete-booking").on('click', function () {
        $('#confirmationModal').modal('show');
    });

    $(".close").on('click', function () {
        $('#confirmationModal').modal('hide');
    });
}
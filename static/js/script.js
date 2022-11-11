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

// Stops user from selecting a date in the past
function checkDate() {
    $(".booking-enquiry").one('submit', (function (e) {
        e.preventDefault();
        var $this = $(this);
        var selectedDate = $('#id_requested_date').datepicker('getDate');
        if ((selectedDate.getTime() < Date.now())) {
            alert("Selected date is in the past, please choose a date in the future.");
        } else {
            $this.submit();
        }
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

// The debounce function is edded to make sure
//a given task doesn't fire so often that it 
// breaks the browser performance
function debounce(func, wait, immediate) {
    var timeout;
    return function () {
        var context = this,
            args = arguments;
        var later = function () {
            timeout = null;
            if (!immediate) func.apply(context, args);
        };
        var callNow = immediate && !timeout;
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
        if (callNow) func.apply(context, args);
    };
}

// Call all functions 
$(document).ready(function () {

    datePicker();

    deleteModal();

    checkDate();

});
// Navbar class gets applied
const nav = document.querySelector('nav');

window.addEventListener('scroll', () => {
    if ((window.scrollY >= 50)) {
        nav.classList.add('scrolled');
    } else {
        nav.classList.remove('scrolled');
    }
})

// Opens the modal on delete_booking
function deleteModal() {
    $("#delete-booking").on('click', function () {
        $('#confirmationModal').modal('show');
    });

    $(".close").on('click', function () {
        $('#confirmationModal').modal('hide');
    });
}

// The debounce function is added to make sure
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

    deleteModal();

});
document.addEventListener('DOMContentLoaded', function () {
    const deleteForms = document.querySelectorAll('form[action*="delete_todo"]');
    deleteForms.forEach(form => {
        form.addEventListener('submit', (e) => {
            if (!confirm('Are you sure you want to delete this todo?')) {
                e.preventDefault();
            }
        });
    });

    const checkboxes = document.querySelectorAll('input[type="checkbox"][name="completed"]');
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', () => {
            checkbox.form.submit();
        });
    });
});
document.addEventListener('DOMContentLoaded', function () {
    const preferences = [
        'Education', 'Entertainment', 'Medical', 'Food',
        'Transportation', 'Kids', 'Pets', 'Clothing',
        'Savings', 'Maintenance', 'Personal Expenses','EMI','Other'
    ];

    const dropdowns = document.querySelectorAll('.preference-dropdown');

    // Populate each dropdown with options
    dropdowns.forEach(dropdown => {
        preferences.forEach(pref => {
            const option = document.createElement('option');
            option.value = pref;
            option.text = pref;
            dropdown.appendChild(option);
        });
    });

    // Function to handle option disabling
    function updateDropdowns() {
        // Get all selected values
        const selectedValues = Array.from(dropdowns)
            .map(dropdown => dropdown.value)
            .filter(value => value !== '');  // Filter out empty values

        // Loop through each dropdown and update its options
        dropdowns.forEach(dropdown => {
            Array.from(dropdown.options).forEach(option => {
                // If the option is selected in another dropdown, disable it
                if (selectedValues.includes(option.value) && option.value !== dropdown.value) {
                    option.disabled = true;
                } else {
                    option.disabled = false; // Enable the option if it's not selected
                }
            });
        });
    }

    // Attach event listener to each dropdown
    dropdowns.forEach(dropdown => {
        dropdown.addEventListener('change', updateDropdowns);
    });

    // Handle form submission
    document.querySelector('#preferencesForm').addEventListener('submit', function (event) {
        event.preventDefault();  // Prevent default form submission

        // Get the selected values from all dropdowns
        const selectedValues = Array.from(dropdowns)
            .map(dropdown => dropdown.value)
            .filter(value => value !== '');  // Only include non-empty values

        // Send the selected values to the backend using fetch
        fetch('/your-django-url/', {  // Replace with your Django URL
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken()  // Handle CSRF token
            },
            body: JSON.stringify({ preferences: selectedValues })  // Send as JSON
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    // Function to get CSRF token
    function getCSRFToken() {
        return document.querySelector('[name=csrfmiddlewaretoken]').value;
    }
});

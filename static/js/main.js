document.addEventListener('DOMContentLoaded', () => {
    // Handle File Upload styling
    const fileInput = document.getElementById('file-upload');
    if (fileInput) {
        fileInput.addEventListener('change', (e) => {
            const label = document.getElementById('file-label');
            if (label && e.target.files.length > 0) {
                label.textContent = e.target.files[0].name;
            }
        });
    }

    // Auto-dismiss alerts
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 500);
        }, 4000);
    });
});

function confirmAction(message) {
    return confirm(message || 'Are you sure you want to perform this action?');
}

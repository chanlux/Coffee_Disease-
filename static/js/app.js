document.addEventListener('DOMContentLoaded', function() {
    window.addEventListener('scroll', function() {
        const navbar = document.querySelector('.navbar');
        if (navbar) {
            navbar.style.boxShadow = window.scrollY > 50 ? '0 2px 20px rgba(0,0,0,0.1)' : 'none';
        }
    });

    const searchInput = document.getElementById('searchInput');
    if (searchInput) {
        searchInput.addEventListener('keyup', function() {
            let filter = this.value.toLowerCase();
            let rows = document.querySelectorAll('table tbody tr'); 
            rows.forEach(row => {
                row.style.display = row.textContent.toLowerCase().includes(filter) ? '' : 'none';
            });
        });
    }

    const diseaseFilter = document.getElementById('diseaseFilter');
    if (diseaseFilter) {
        diseaseFilter.addEventListener('change', function() {
            let filter = this.value.toLowerCase();
            let rows = document.querySelectorAll('table tbody tr');
            rows.forEach(row => {
                let diseaseCell = row.cells[1].textContent.toLowerCase();
                row.style.display = (filter === "" || diseaseCell.includes(filter)) ? '' : 'none';
            });
        });
    }
});

function viewCase(id) {
    window.location.href = `/cases/${id}`;
}

function shareCase(id) {
    const url = window.location.origin + '/cases/' + id;
    navigator.clipboard.writeText(url).then(() => alert('បានចម្លងតំណ!'));
}

function deleteCase(id) {
    if (confirm('តើអ្នកប្រាកដថាចង់លុបករណីនេះមែនទេ? សកម្មភាពនេះមិនអាចត្រឡប់វិញបានទេ។')) {
        fetch(`/cases/${id}/delete`, { 
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        })
        .then(res => res.json())
        .then(data => {
            if (data.success) {
                const row = document.getElementById(`case-row-${id}`);
                if (row) {
                    row.remove();
                } else {
                    location.reload();
                }
            } else {
                alert('កំហុស៖ ' + data.message);
            }
        })
        .catch(err => console.error('Error:', err));
    }
}

function applyFilter(period) {
    window.location.href = '/cases/?period=' + encodeURIComponent(period);
}
document.getElementById('downloadButton').addEventListener('click', function() {
    event.preventDefault(); // Prevent form submission
    
    console.log("Button clicked");
        
    // Get table data and create CSV (example code)
    var table = document.getElementById('example');
    var csv = [];
        
    // Collect headers
    var headers = [];
    table.querySelectorAll(".itemheader").forEach(function(header) {
        headers.push(header.textContent);
    });
    csv.push(headers.join(','));

    // Collect rows (example code)
    table.querySelectorAll('tbody tr').forEach(function(row) {
        var rowData = [];
        row.querySelectorAll('td').forEach(function(cell) {
            rowData.push(cell.textContent.trim()); // Adjust as per your data structure
        });
        csv.push(rowData.join(','));
    });
    
    // Create download link
    var csvFile = new Blob([csv.join('\n')], { type: 'text/csv' });
    var downloadLink = document.createElement('a');
    downloadLink.download = 'table.csv';
    downloadLink.href = window.URL.createObjectURL(csvFile);
    downloadLink.style.display = 'none';
    document.body.appendChild(downloadLink);
    
    // Trigger download
    downloadLink.click();
    
    // Clean up
    document.body.removeChild(downloadLink);

});
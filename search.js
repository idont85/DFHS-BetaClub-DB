var currentSearchMethod = "name"
var currentSearch = ""
var result = ""


function changeSearchMethod(method, buttonID) {
    currentSearchMethod = method

    if (currentSearchMethod == "id") {
        document.getElementById('nameSearch').style.backgroundColor = '#BEFFE9';
        document.getElementById('nameSearch').style.color = 'black';
        document.getElementById('idSearch').style.backgroundColor = '#459063';
        document.getElementById('idSearch').style.color = 'white';
    }

    if (currentSearchMethod == "name") {
        document.getElementById('idSearch').style.backgroundColor = '#BEFFE9';
        document.getElementById('idSearch').style.color = 'black';
        document.getElementById('nameSearch').style.backgroundColor = '#459063';
        document.getElementById('nameSearch').style.color = 'white';
    }
}

function searchTable() {
    const table = document.getElementsByClassName('mainLoggingTable')[0];
    currentSearch = document.getElementById('searchInput').value;
    var foundValue = false
    if (currentSearchMethod == "name") {
        const rows = table.querySelectorAll('tr:not(:first-child)');
        for (const row of rows) {
            if (row.cells[2].textContent.trim() === currentSearch) {
                result = `ℹ️\n Times Scanned: ${row.cells[0].textContent}\n ID#: ${row.cells[1].textContent}\n Name: ${row.cells[2].textContent}\n Fee Status: ${row.cells[3].textContent}`
                alert(result);
                foundValue = true
                break;
            }
        }

    } else if (currentSearchMethod == "id") {
                const rows = table.querySelectorAll('tr:not(:first-child)');
        for (const row of rows) {
            if (row.cells[1].textContent.trim() === currentSearch) {
                result = `ℹ️\n Times Scanned: ${row.cells[0].textContent}\n ID#: ${row.cells[1].textContent}\n Name: ${row.cells[2].textContent}\n Fee Status: ${row.cells[3].textContent}`
                alert(result);
                foundValue = true
                break;
            }
        }

    }

    if (foundValue == false) {
        alert("Error locating search term. Check search term validity or change search type.")
    }

}

function toggleInfoInRow(infoRow) {
    [...infoRow.cells].forEach(function(cell, index) {
        if (cell.lastElementChild != null && cell.lastElementChild.className==="dop-info"){
            infoRow.cells[index].lastElementChild.style.display = 
            cell.lastElementChild.style.display === 'block' ? 'none' : 'block';
        }
    });
}

function toggleInfoInH1(infoH1) {
    if (infoH1.lastElementChild != null && infoH1.lastElementChild.className==="dop-info"){
        infoH1.lastElementChild.style.display = 
        infoH1.lastElementChild.style.display === 'block' ? 'none' : 'block';
    }
}
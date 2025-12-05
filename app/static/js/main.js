async function fetchAPI(url, method = "GET", data = null) {
    const options = { method, headers: { "Content-Type": "application/json" } };
    if (data) options.body = JSON.stringify(data);

    const res = await fetch(url, options);
    return res.json();
}

function renderTable(elementId, rows) {
    const table = document.getElementById(elementId);
    table.innerHTML = "";

    rows.forEach(row => {
        const tr = document.createElement("tr");
        Object.values(row).forEach(val => {
            const td = document.createElement("td");
            td.textContent = val;
            tr.appendChild(td);
        });
        table.appendChild(tr);
    });
}

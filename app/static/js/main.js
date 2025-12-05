/**
 * ============================================
 * BIBLIOTECA - Funciones JavaScript Comunes
 * Utilidades compartidas para todas las páginas
 * ============================================
 */

/**
 * Realiza una petición HTTP a la API
 *
 * @param {string} url - URL completa del endpoint
 * @param {string} method - Método HTTP (GET, POST, PUT, DELETE)
 * @param {object|null} data - Datos a enviar en el body (para POST/PUT)
 * @returns {Promise<object>} - Respuesta JSON de la API
 * @throws {Error} - Si la respuesta no es exitosa (status >= 400)
 */
async function fetchAPI(url, method = "GET", data = null) {
  const options = {
    method,
    headers: {
      "Content-Type": "application/json",
    },
  };

  // Agregar body solo si hay datos
  if (data) {
    options.body = JSON.stringify(data);
  }

  const response = await fetch(url, options);

  // Verificar si la respuesta es exitosa
  if (!response.ok) {
    throw new Error(`HTTP ${response.status}: ${response.statusText}`);
  }

  return response.json();
}

/**
 * Renderiza una tabla genérica con los datos proporcionados
 * Útil para tablas simples sin formato especial
 *
 * @param {string} elementId - ID del elemento tbody donde renderizar
 * @param {Array<object>} rows - Array de objetos con los datos
 */
function renderTable(elementId, rows) {
  const table = document.getElementById(elementId);
  if (!table) {
    console.error(`Elemento con ID "${elementId}" no encontrado`);
    return;
  }

  table.innerHTML = "";

  rows.forEach((row) => {
    const tr = document.createElement("tr");
    Object.values(row).forEach((val) => {
      const td = document.createElement("td");
      td.textContent = val;
      tr.appendChild(td);
    });
    table.appendChild(tr);
  });
}

/**
 * Muestra u oculta un indicador de carga
 *
 * @param {string} elementId - ID del elemento loading
 * @param {boolean} show - true para mostrar, false para ocultar
 */
function toggleLoading(elementId, show) {
  const el = document.getElementById(elementId);
  if (el) {
    el.classList.toggle("active", show);
  }
}

/**
 * Formatea un número como moneda colombiana (COP)
 *
 * @param {number|string} value - Valor a formatear
 * @returns {string} - Valor formateado con separadores de miles
 */
function formatCOP(value) {
  const num = typeof value === "string" ? parseInt(value) : value;
  return `$${num.toLocaleString("es-CO")} COP`;
}

/**
 * Formatea un peso en kilogramos
 *
 * @param {number|string} value - Peso a formatear
 * @returns {string} - Peso formateado con 2 decimales
 */
function formatPeso(value) {
  const num = typeof value === "string" ? parseFloat(value) : value;
  return `${num.toFixed(2)} Kg`;
}

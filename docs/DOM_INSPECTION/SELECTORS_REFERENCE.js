/**
 * SELECTORS_REFERENCE.js
 * Referencia de selectores JavaScript para elturf.com
 * DOM Inspection Project
 */

// ═══════════════════════════════════════════════════════════════════════════════
// 1. EXTRACCIÓN DE IEA (Índice de Equipo Actual)
// ═══════════════════════════════════════════════════════════════════════════════

function extractIEA() {
    const ieas = [];
    const strongElements = document.querySelectorAll('strong');
    
    for (const el of strongElements) {
        if (el.textContent.includes('IEA')) {
            const match = el.parentElement.textContent.match(/IEA\s+([\d,]+)/);
            if (match) {
                ieas.push(match[1]);
            }
        }
    }
    
    return ieas;
}

// ═══════════════════════════════════════════════════════════════════════════════
// 2. EXTRACCIÓN DE IR (Índice de Reciente)
// ═══════════════════════════════════════════════════════════════════════════════

function extractIR() {
    const irs = [];
    const strongElements = document.querySelectorAll('strong');
    
    for (const el of strongElements) {
        if (el.textContent.includes('IR')) {
            const match = el.parentElement.textContent.match(/IR\s+([\d,]+)/);
            if (match) {
                irs.push(match[1]);
            }
        }
    }
    
    return irs;
}

// ═══════════════════════════════════════════════════════════════════════════════
// 3. EXTRACCIÓN DE CC (Carreras Corridas)
// ═══════════════════════════════════════════════════════════════════════════════

function extractCC() {
    const ccs = [];
    const tables = document.querySelectorAll('table');
    
    for (const table of tables) {
        const headers = Array.from(table.querySelectorAll('th, td')).slice(0, 10);
        const headerText = headers.map(h => h.textContent).join(' ');
        
        if (headerText.includes('Años') && headerText.includes('CC')) {
            const firstRow = table.querySelector('tbody tr');
            if (firstRow) {
                const cols = firstRow.querySelectorAll('td');
                if (cols.length > 1) {
                    ccs.push(cols[1].textContent);
                }
            }
        }
    }
    
    return ccs;
}

// ═══════════════════════════════════════════════════════════════════════════════
// 4. EXTRACCIÓN DE ÚLTIMAS 5 LLEGADAS
// ═══════════════════════════════════════════════════════════════════════════════

function extractUltimasLlegadas() {
    const llegadas = [];
    const tables = document.querySelectorAll('table');
    const datePattern = /\d{2}[A-Z][a-z]{2}\d{2}/;
    
    for (const table of tables) {
        const firstRow = table.querySelector('tbody tr');
        if (firstRow && datePattern.test(firstRow.textContent)) {
            // Es tabla de historial
            const raceRows = Array.from(table.querySelectorAll('tbody tr')).slice(0, 5);
            
            for (const row of raceRows) {
                const cols = row.querySelectorAll('td');
                if (cols.length > 10) {
                    llegadas.push({
                        fecha: cols[0].textContent,
                        hipodromo: cols[1].textContent,
                        distancia: cols[2].textContent,
                        posicion: cols[10].textContent
                    });
                }
            }
            break;
        }
    }
    
    return llegadas;
}

// ═══════════════════════════════════════════════════════════════════════════════
// 5. EXTRACCIÓN COMPLETA
// ═══════════════════════════════════════════════════════════════════════════════

function extractAllAttributes() {
    return {
        iea: extractIEA(),
        ir: extractIR(),
        cc: extractCC(),
        ultimas_llegadas: extractUltimasLlegadas()
    };
}

// Uso:
const datos = extractAllAttributes();
console.log(datos);
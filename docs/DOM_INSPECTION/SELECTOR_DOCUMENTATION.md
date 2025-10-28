# 🔍 DOCUMENTACIÓN TÉCNICA DE SELECTORES

## Introducción

Esta guía documenta los selectores CSS/XPath identificados durante la inspección del DOM de elturf.com para extraer atributos de caballos en programas de carreras.

---

## 1. IEA (Índice de Equipo Actual)

### Ubicación en el DOM
```html
<div class="col-xs-3">
  <strong>IEA</strong>
  <strong>4,4</strong>
</div>
```

### Selector
```javascript
page.query_selector_all('strong')
// Filtrar para elementos que contengan 'IEA'
```

### Extracción en Python
```python
iea_elements = page.query_selector_all('strong')
for strong_el in iea_elements:
    if 'IEA' in strong_el.inner_text():
        parent_text = strong_el.evaluate('el => el.parentElement.textContent')
        iea_match = re.search(r'IEA\s+([\d,]+)', parent_text)
        iea_value = iea_match.group(1)  # Ej: "4,4"
```

### Ejemplos
- "4,4"
- "5,3"
- "5,7"

---

## 2. IR (Índice de Reciente)

### Ubicación en el DOM
```html
<div class="col-xs-3">
  <strong>IR</strong>
  <strong>21,1</strong>
</div>
```

### Selector
Similar a IEA, buscar en `<strong>` tags

### Extracción en Python
```python
container_text = page.evaluate('el => el.textContent', container)
ir_match = re.search(r'IR\s+([\d,]+)', container_text)
ir_value = ir_match.group(1)  # Ej: "21,1"
```

### Ejemplos
- "21,1"
- "0,0"
- "22,0"

---

## 3. CC (Carreras Corridas)

### Ubicación en el DOM
```html
<table>
  <thead>
    <tr>
      <th>Años</th>
      <th>CC</th>
      <th>1°</th>
      <th>2°</th>
      ...
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2025</td>
      <td>34</td>  <!-- CC siempre en posición [1] -->
      <td>5</td>
      ...
    </tr>
  </tbody>
</table>
```

### Selector
```javascript
tables = page.query_selector_all('table')
for table in tables:
    headers = table.query_selector_all('th, td')[:10]
    if 'Años' in headers_text and 'CC' in headers_text:
        # Esta es la tabla de estadísticas
        first_row = table.query_selector('tbody tr')
        cc_value = first_row.query_selector_all('td')[1].inner_text()
```

### Ejemplos
- "34"
- "16"
- "15"

---

## 4. Últimas 5 Llegadas

### Ubicación en el DOM
```html
<table>
  <tbody>
    <tr>
      <td>21Oct25</td>    <!-- [0] Fecha -->
      <td>CHC</td>         <!-- [1] Hipódromo -->
      <td>1000m</td>       <!-- [2] Distancia -->
      <td>...</td>         <!-- [3-9] Otros datos -->
      <td>2°/12</td>       <!-- [10] Posición -->
    </tr>
  </tbody>
</table>
```

### Selector
```javascript
for table in tables:
    first_row = table.query_selector('tbody tr')
    if re.search(r'\d{2}[A-Z][a-z]{2}\d{2}', first_row.inner_text()):
        # Es tabla de historial
        race_rows = table.query_selector_all('tbody tr')[:5]
```

### Extracción
```python
for row in race_rows:
    cols = row.query_selector_all('td')
    llegada = {
        'fecha': cols[0].inner_text(),      # "21Oct25"
        'hipodromo': cols[1].inner_text(),  # "CHC"
        'distancia': cols[2].inner_text(),  # "1000m"
        'posicion': cols[10].inner_text()   # "2°/12"
    }
```

### Ejemplos
- {"fecha": "21Oct25", "hipodromo": "CHC", "posicion": "2°/12"}
- {"fecha": "14Oct25", "hipodromo": "CHC", "posicion": "(2°/10)"}
- {"fecha": "7Oct25", "hipodromo": "CHC", "posicion": "1°/10"}
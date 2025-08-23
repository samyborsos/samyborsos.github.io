// nailsv2/colors.js
// Handles preset color logic for Nailverse calendar

console.log('Nailverse calendar color presets loaded');

// JSONBin.io config
const BIN_ID = '68446a408561e97a5020b8c5';
const API_KEY = '$2a$10$J7fi24LcCk1TF8IfMHC4.e/IaKxCzRvCdOdE5F3YrDVrMRjhID4lC';

let presetColors = [];

function loadPresets() {
    try {
        presetColors = JSON.parse(localStorage.getItem('nailColorPresets') || '[]');
    } catch { presetColors = []; }
    if (!Array.isArray(presetColors)) presetColors = [];
    // Convert old string-only presets to object with color and empty desc
    presetColors = presetColors.map(p => typeof p === 'string' ? { color: p, desc: '' } : { color: p.color, desc: p.desc || '' });
    if (presetColors.length === 0) {
        presetColors = [
            { color: '#e57373', desc: 'red' },
            { color: '#6264f0ff', desc: 'blue' },

        ];
    }
    console.debug('[colors.js] loadPresets result:', presetColors);
}
function savePresets() {
    localStorage.setItem('nailColorPresets', JSON.stringify(presetColors));
    console.debug('[colors.js] savePresets:', presetColors);
}
function renderPresets(colorInput, descInput, presetColorsDiv) {
    console.debug('[colors.js] renderPresets called');
    presetColorsDiv.innerHTML = presetColors.map((preset, i) => {
        let color = preset.color;
        let desc = preset.desc || '';
        return `<div class="bg-gray-800 rounded-lg shadow flex flex-col items-center p-2 w-24 group relative">
  <button type="button" class="w-8 h-8 rounded-full border-2 border-gray-600 focus:ring-2 focus:ring-indigo-400 transition-all mb-1" style="background:${color}" title="${color}" tabindex="0"></button>
  <span class="text-xs text-gray-400">${color}</span>
  <input type="text" value="${desc.replace(/"/g, '&quot;')}" class="text-xs text-gray-300 text-center break-words bg-gray-700 rounded px-1 py-0.5 mt-1 w-full focus:outline-none focus:border-indigo-400 border border-gray-600 preset-desc-input" data-index="${i}" placeholder="Név vagy leírás..." />
  <button type="button" class="absolute top-0 right-0 text-xs text-red-400 hover:text-red-600 transition-colors bg-gray-900 rounded-full px-1 py-0.5 opacity-0 group-hover:opacity-100" title="Törlés" tabindex="-1">×</button>
</div>`;
    }).join('');
    Array.from(presetColorsDiv.children).forEach((card, i) => {
        const colorBtn = card.querySelector('button');
        colorBtn.addEventListener('click', () => {
            const preset = presetColors[i];
            colorInput.value = preset.color;
            descInput.value = preset.desc || '';
            console.debug('[colors.js] Color selected:', preset);
        });
        const delBtn = card.querySelectorAll('button')[1];
        delBtn.addEventListener('click', (e) => {
            e.preventDefault();
            if (confirm('Törlöd ezt a kedvenc színt?')) {
                console.debug('[colors.js] Deleting preset:', presetColors[i]);
                presetColors.splice(i, 1);
                savePresets();
                renderPresets(colorInput, descInput, presetColorsDiv);
            }
        });
        // Inline edit for description
        const descInputEl = card.querySelector('.preset-desc-input');
        descInputEl.addEventListener('change', (e) => {
            presetColors[i].desc = e.target.value;
            savePresets();
            renderPresets(colorInput, descInput, presetColorsDiv);
            console.debug('[colors.js] Description changed:', presetColors[i]);
        });
    });
    // Render color legend (description list)
    const legendList = document.getElementById('legendList');
    if (legendList) {
        legendList.innerHTML = presetColors
            .map(preset => {
                let color = preset.color;
                let desc = preset.desc || '';
                if (!desc) return '';
                return `<div class="flex items-center gap-2 bg-gray-800 rounded px-2 py-1 mb-1">
                    <span class="inline-block w-5 h-5 rounded-full border-2 border-gray-600" style="background:${color}"></span>
                    <span class="text-xs text-gray-200">${desc}</span>
                </div>`;
            })
            .filter(Boolean)
            .join('');
    }
    console.debug('[colors.js] renderPresets finished');
}
function addPreset(colorInput, descInput, presetColorsDiv) {
    const c = colorInput.value;
    const d = descInput.value.trim();
    if (!presetColors.some(p => p.color === c)) {
        presetColors.push({ color: c, desc: d });
        savePresets();
        renderPresets(colorInput, descInput, presetColorsDiv);
        console.debug('[colors.js] Preset added:', { color: c, desc: d });
    }
}
// ...existing code for other calendar logic remains in index.html...

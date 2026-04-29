document.addEventListener('DOMContentLoaded', () => {
    // --- Elements ---
    const dropZone = document.getElementById('drop-zone');
    const fileInput = document.getElementById('image-upload');
    const previewContainer = document.getElementById('preview-container');
    const previewImage = document.getElementById('preview-image');
    const removeBtn = document.getElementById('remove-btn');
    
    const vibePills = document.querySelectorAll('.vibe-pill');
    const countPills = document.querySelectorAll('.count-pill');
    
    const generateBtn = document.getElementById('generate-btn');
    const faqItems = document.querySelectorAll('.faq-item');

    const vibeInput = document.getElementById('vibe-input');
    const countInput = document.getElementById('count-input');
    const form = document.querySelector('form');
    
    let selectedVibe = 'Aesthetic';
    let selectedCount = 3;

    // --- Count Logic ---
    countPills.forEach(pill => {
        pill.addEventListener('click', () => {
            countPills.forEach(p => p.classList.remove('active'));
            pill.classList.add('active');
            selectedCount = parseInt(pill.dataset.count);
            countInput.value = selectedCount;
        });
    });

    // --- Vibe Logic ---
    vibePills.forEach(pill => {
        pill.addEventListener('click', () => {
            vibePills.forEach(p => p.classList.remove('active'));
            pill.classList.add('active');
            selectedVibe = pill.textContent;
            vibeInput.value = selectedVibe;
        });
    });

    // --- Upload & Preview ---
    dropZone.addEventListener('click', () => fileInput.click());

    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.style.borderColor = '#E63946';
    });

    dropZone.addEventListener('dragleave', () => {
        dropZone.style.borderColor = '';
    });

    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        const files = e.dataTransfer.files;
        if (files.length) handleFile(files[0]);
    });

    fileInput.addEventListener('change', (e) => {
        if (e.target.files.length) handleFile(e.target.files[0]);
    });

    function handleFile(file) {
        if (!file.type.startsWith('image/')) return;
        
        const reader = new FileReader();
        reader.onload = (e) => {
            previewImage.src = e.target.result;
            dropZone.style.display = 'none';
            previewContainer.style.display = 'block';
        };
        reader.readAsDataURL(file);
    }

    removeBtn.addEventListener('click', () => {
        fileInput.value = '';
        previewImage.src = '';
        previewContainer.style.display = 'none';
        dropZone.style.display = 'flex';
    });

    // --- FAQ Accordion ---
    faqItems.forEach(item => {
        const trigger = item.querySelector('.faq-trigger');
        trigger.addEventListener('click', () => {
            const isActive = item.classList.contains('active');
            faqItems.forEach(i => i.classList.remove('active'));
            if (!isActive) item.classList.add('active');
        });
    });

    // --- Scroll Reveal Logic ---
    const revealCallback = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
            }
        });
    };

    const revealObserver = new IntersectionObserver(revealCallback, {
        threshold: 0.15
    });

    document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

    // --- Generation Trigger ---
    form.addEventListener('submit', (e) => {
        if (!fileInput.files.length) {
            e.preventDefault();
            alert('Please upload an image first.');
            return;
        }

        generateBtn.disabled = true;
        generateBtn.innerHTML = `
            <svg class="animate-spin" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-right: 8px; vertical-align: middle;"><path d="M21 12a9 9 0 1 1-6.219-8.56"></path></svg>
            Analyzing Canvas...
        `;
    });
});

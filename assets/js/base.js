function searchMaterial() {
    let eleSelectType = document.querySelector('#select-type');
    let eleSearchInput = document.querySelector('#search-box input');
    let eleSearchButton = document.querySelector('#search-box button');
    let eleMaterialContainers = document.querySelectorAll('.material-container');
    let eleNoResult = document.querySelector('#no-result');
    let materialContainersCount = eleMaterialContainers.length;
    let typeChinese = false;
    
    eleSelectType.addEventListener('change', () => displayMaterialContainer());

    eleSearchButton.addEventListener('click', () => {
        let keywords = eleSearchInput.value;
        displayMaterialContainer(keywords);
    })
    
    eleSearchInput.addEventListener('compositionstart', () => {
        typeChinese = true;
    })
    
    eleSearchInput.addEventListener('input', () => {
        if (!typeChinese) {
            let keywords = eleSearchInput.value;
            displayMaterialContainer(keywords);
        }
    })

    eleSearchInput.addEventListener('compositionend', () => {
        let keywords = eleSearchInput.value;
        displayMaterialContainer(keywords);
        typeChinese = false;
    })

    function displayNoResult() {
        eleNoResult.style.display = 'block';
    }

    function hideNoResult() {
        eleNoResult.style.display = 'none';
    }

    function displayMaterialContainer(keywords='') {
        let count = 0
        let selectType = eleSelectType.value;
        Array.from(eleMaterialContainers).forEach((ele) => {
            if (selectType === 'all') {
                ele.classList.remove('hide');
            } else {
                let materialType = ele.querySelector('.type').innerText;
                if (materialType === selectType) {
                    ele.classList.remove('hide');
                } else {
                    ele.classList.add('hide');
                }
            }
            if (keywords !== '') {
                let materialName = ele.querySelector('.name .info').innerText;
                let materialAuthor = ele.querySelector('.author .info').innerText;
                if (!materialName.includes(keywords) && !materialAuthor.includes(keywords)) {
                    ele.classList.add('hide');
                }
            }
        })
        let hiddenMaterialContainersCount = document.querySelectorAll('.material-container.hide').length;
        if (hiddenMaterialContainersCount === materialContainersCount) {
            displayNoResult();
        } else {
            hideNoResult();
        }
    }
}


function displayAbout() {
    let display = false;
    let eleAboutButton = document.querySelector('#about-button');
    let eleAboutContent = document.querySelector('#about-content');
    let eleMaterials = document.querySelector('#materials');
    eleAboutButton.addEventListener('pointerdown', () => {
        eleAboutContent.style.display = 'block';
        eleMaterials.style.filter = 'brightness(0.1)';
        display = true;
    })
    eleMaterials.addEventListener('pointerdown', () => {
        if (display) {
            eleAboutContent.style.display = 'none';
            eleMaterials.style.filter = 'brightness(1)';
        }
    })
            
}


function adjustSearchBoxLength() {
    if (/Android|webOS|iPhone|iPad|iPod|BlackBerry/i.test(navigator.userAgent)) {
        let eleHeader = document.querySelector('#header');
        let eleHeaderLeft = document.querySelector('#header-left');
        let eleSelectType = document.querySelector('#select-type');
        let eleSearchButton = document.querySelector('#search-button');
        let eleAboutButton = document.querySelector('#about-button');
        let eleInput = document.querySelector('#search-box input');
        let width = `${eleHeader.clientWidth - eleHeaderLeft.clientWidth - eleSelectType.clientWidth - eleSearchButton.clientWidth - eleAboutButton.clientWidth - 6}px`;
        alert(eleHeader.clientWidth, eleHeaderLeft.clientWidth, eleSelectType.clientWidth, eleSearchButton.clientWidth, eleAboutButton.clientWidth, width);
        eleInput.style.width = width;
    }
}

searchMaterial();
displayAbout();
adjustSearchBoxLength()

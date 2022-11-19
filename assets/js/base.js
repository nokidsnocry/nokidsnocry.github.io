function searchMaterial() {
    let eleSearchInput = document.querySelector('#search-box input');
    let eleSearchButton = document.querySelector('#search-box button');
    let eleMaterialContainers = document.querySelectorAll('.material-container');
    let eleNoResult = document.querySelector('#no-result');
    let materialContainersCount = eleMaterialContainers.length;
    eleSearchButton.addEventListener('click', function() {
        let count = 0;
        let keywords = eleSearchInput.value;
        Array.from(eleMaterialContainers).forEach((ele) => {
            let materialName = ele.querySelector('.name .info').innerText;
            let materialAuthor = ele.querySelector('.author .info').innerText;
            if (!materialName.includes(keywords) && !materialAuthor.includes(keywords)) {
                ele.style.display = 'none';
                count ++;
            }
        })
        if (count === materialContainersCount) {
            eleNoResult.style.display = 'block';
        }
            
    })
    eleSearchInput.addEventListener('keyup', () => {
        eleNoResult.style.display = 'none';
        Array.from(eleMaterialContainers).forEach((ele) => {
            ele.style.display = 'block';
        })
    })
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

searchMaterial();
displayAbout();

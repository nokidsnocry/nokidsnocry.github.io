function searchMaterial() {
    let eleSearchInput = document.querySelector('#search-box input');
    let eleSearchButton = document.querySelector('#search-box button');
    let eleMaterialContainers = document.querySelectorAll('.material-container');
    eleSearchButton.addEventListener('click', function() {
        let keywords = eleSearchInput.value;
        Array.from(eleMaterialContainers).forEach((ele) => {
            let materialName = ele.querySelector('.name .info').innerText;
            let materialAuthor = ele.querySelector('.author .info').innerText;
            if (!materialName.includes(keywords) && !materialAuthor.includes(keywords)) {
                ele.style.display = 'none';
            }
        })
    })
    eleSearchInput.addEventListener('keyup', () => {
        Array.from(eleMaterialContainers).forEach((ele) => {
            ele.style.display = 'block';
        })
    })
}

searchMaterial();
            

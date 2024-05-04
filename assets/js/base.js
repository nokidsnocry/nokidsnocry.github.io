const eleSelectType = document.querySelector('#select-type');
const eleSearchInput = document.querySelector('#search-box input');
const eleSearchButton = document.querySelector('#search-box button');
const eleContainer = document.querySelector('#container');
const eleMaterials = document.querySelector('#materials');
const eleMaterialContainers = document.querySelectorAll('.material-container');
const eleNoResult = document.querySelector('#no-result');
const eleLoading = document.querySelector('#loading');
const eleModal = document.querySelector('#modal');
const eleModalButton = document.querySelector('#modal button');


function searchMaterial() {
    let materialContainersCount = eleMaterialContainers.length;
    let typeChinese = false;
    
    eleSelectType.addEventListener('change', () => {
        displayLoading();
        let keywords = eleSearchInput.value;
        setTimeout(() => displayMaterialContainer(keywords), 100);
        setTimeout(hideLoading, 100);
    })

    eleSearchButton.addEventListener('pointerdown', () => {
        displayLoading();
        let keywords = eleSearchInput.value;
        setTimeout(() => displayMaterialContainer(keywords), 100);
        setTimeout(hideLoading, 100);
    })

    document.addEventListener("keyup", (e) => {
      if (e.key === "Enter") {
        displayLoading();
        let keywords = eleSearchInput.value;
        setTimeout(() => displayMaterialContainer(keywords), 100);
        setTimeout(hideLoading, 100);
      }
    })

    function displayLoading() {
        eleLoading.style.display = 'block';
        eleContainer.style.filter = 'blur(10px)';
    }

    function hideLoading() {
        eleLoading.style.display = 'none';
        eleContainer.style.filter = 'blur(0px)';
    }


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
        eleMaterials.scrollIntoView();
    }
}


function displayAbout() {
    let display = false;
    let eleAboutButton = document.querySelector('#about-button');
    let eleAboutContent = document.querySelector('#about-content');
    let eleMaterials = document.querySelector('#materials');
    eleAboutButton.addEventListener('pointerdown', () => {
        eleAboutContent.style.display = 'block';
        eleContainer.style.filter = 'blur(10px)';
        display = true;
    })
    eleMaterials.addEventListener('pointerdown', () => {
        if (display) {
            eleAboutContent.style.display = 'none';
            eleContainer.style.filter = 'blur(0px)';
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
        let width = `${eleHeader.clientWidth - eleHeaderLeft.clientWidth - eleSelectType.clientWidth - eleSearchButton.clientWidth - eleAboutButton.clientWidth - 30}px`;
        eleInput.style.width = width;
    }
}


function setNewBanner() {
    let timeStamp = Math.floor(new Date().getTime() / 1000);
    let eleMaterialContainers = document.querySelectorAll('.material-container');
    Array.from(eleMaterialContainers).forEach((ele) => {
        let utime = ele.getAttribute('data-utime');
        let timeGap = timeStamp - utime;
        if (timeGap < 259200) {
            ele.classList.add('new');
        }
    })
}


function goHome() {
    let eleHeader = document.querySelector('#header-left');
    eleHeader.addEventListener('pointerdown', () => window.location.href='/');
}


function customScrollbar() {
    let { 
        OverlayScrollbars, 
        ScrollbarsHidingPlugin, 
        SizeObserverPlugin, 
        ClickScrollPlugin  
    } = OverlayScrollbarsGlobal;
    OverlayScrollbars(document.querySelector('#container'), {
        overflow: {
            x: 'hidden',
        },
    });
}

function setContainerHeight() {
    let height = window.innerHeight;
    eleContainer.style.height = (height - 60) + 'px';
}

function displayModal() {
  eleModal.style.display = 'block';
  setTimeout(() => {
    eleModal.classList.add('animate');
    eleContainer.style.filter = 'blur(10px)';
  }, 100)
  eleModalButton.addEventListener('click', () => {
    eleModal.classList.remove('animate');
    setTimeout(() => {
      eleContainer.style.filter = 'blur(0px)';
      eleModal.style.display = 'none';
    }, 800);
  })
}

searchMaterial();
displayAbout();
adjustSearchBoxLength()
setNewBanner();
goHome();
customScrollbar();
setContainerHeight();
displayModal();

import { data } from "./data.js"

function customScrollbar() {
    let { 
        OverlayScrollbars, 
    } = OverlayScrollbarsGlobal;
    document.querySelectorAll('[data-overlayscrollbars-initialize]').forEach((ele) => {
        if (ele.classList.value === "modal") {
            OverlayScrollbars(ele, {
                scrollbars: {
                    visibility: 'hidden',
                }
            })
        } else {
            OverlayScrollbars(ele, {
                scrollbars: {
                    visibility: "visible",
                }
            });
        }
    });
}

function setNewBanner(ele) {
    let timeStamp = Math.round(new Date().getTime() / 1000);
    let utime = ele.getAttribute('data-utime');
    let timeGap = timeStamp - utime;
    if (timeGap < 259200) {
        ele.classList.add('new');
    }
}


function blinkButton() {
    let eles = document.querySelectorAll("button");
    [...eles].forEach((ele) => {
        let bgColor = window.getComputedStyle(ele).backgroundColor;
        ele.addEventListener("pointerdown", () => {
            ele.style.backgroundColor = "#fff";
            setTimeout(() => {
                ele.style.backgroundColor = bgColor;
            }, 100);
        })
    })
}

function displayNoResult() {
    let eleNoResult = document.querySelector("#no-result");
    eleNoResult.style.display = 'block';
}

function hideNoResult() {
    let eleNoResult = document.querySelector("#no-result");
    eleNoResult.style.display = 'none';
}

function toggleAbout() {
    let display = false;
    let eleAboutButton = document.querySelector('#about-button');
    let eleAboutContent = document.querySelector('.about');
    let eleContainer = document.querySelector('#materials');
    eleAboutButton.addEventListener('pointerdown', () => {
        document.querySelector('.changelog').style.display = "none";
        if (window.getComputedStyle(document.querySelector(".modal")).display === "none") {
            eleAboutContent.style.display = 'block';
            eleContainer.style.filter = 'blur(10px)';
            display = true;
        }
    })
    eleContainer.addEventListener('pointerdown', () => {
        if (display) {
            eleAboutContent.style.display = 'none';
            eleContainer.style.filter = 'blur(0px)';
        }
    })    
}

function toggleChangelog() {
    let display = false;
    let eleChangelogButton = document.querySelector('#changelog-button');
    let eleChangelogContent = document.querySelector('.changelog');
    let eleContainer = document.querySelector('#materials');
    eleChangelogButton.addEventListener('pointerdown', () => {
        document.querySelector('.about').style.display = "none"
        if (window.getComputedStyle(document.querySelector(".modal")).display === "none") {
            eleChangelogContent.style.display = 'block';
            eleContainer.style.filter = 'blur(10px)';
            display = true;
        }
    })
    eleContainer.addEventListener('pointerdown', () => {
        if (display) {
            eleChangelogContent.style.display = 'none';
            eleContainer.style.filter = 'blur(0px)';
        }
    })    
}

function closeModalListener() {
    let eleMaterials = document.querySelector("#materials");
    let eleModal = document.querySelector(".modal");
    let eleModalButton = document.querySelector(".modal button");
    eleModalButton.addEventListener("pointerdown", () => {
        eleModal.style.animation = "fadeOut 1s ease";
        eleMaterials.style.animation = "blurOut 1s ease-in-out";
        setTimeout(() => {
            eleModal.style.display = "none";
            eleMaterials.style.filter = "blur(0)";
        }, 1000);
    })
}


function dynamicLoadMaterial() {
    // let materialData = data.content;
    let materialData = data.content.sort((b, a) => a.utime - b.utime);
    let filteredMaterialData = materialData;
    let eleMaterials = document.querySelector("#materials");
    let loadedAmount = 0;
    let perLoadAmount = 6;

    loadMaterial(30);

    searchMaterialListener();
    continueLoadListener();

    function getType(mData) {
        let typeEngArray = data.metadata.type;
        let typeChiArray = data.metadata.type_chinese;
        return typeChiArray[typeEngArray.indexOf(mData.type)][0];
    }

    function initSearch() {
        while (eleMaterials.firstChild) {
            eleMaterials.removeChild(eleMaterials.firstChild);
        }
        filteredMaterialData = [];
        loadedAmount = 0;
        hideNoResult();
        eleMaterials.scrollIntoView();
    }

    function searchMaterial(type) {
        console.log(type);
        let eleSearchInput = document.querySelector(".searcher > input");
        let searchTerm = eleSearchInput.value;
        materialData.forEach((data) => {
            if (type === "all") {
                if ((data?.author ?? "").includes(searchTerm) || data.name.includes(searchTerm)) {
                    filteredMaterialData.push(data);
                }
            } else {
                if (data.type === type && ((data?.author ?? "").includes(searchTerm) || data.name.includes(searchTerm))) {
                    filteredMaterialData.push(data);
                }
            }
        })
        if (filteredMaterialData.length === 0) {
            displayNoResult();
        }
    }

    function loadMaterial(amount) {
        for (let i=0; i<amount; i++) {
            if (loadedAmount < filteredMaterialData.length) {
                let mData = filteredMaterialData[loadedAmount];
                let materialType = getType(mData);
                let eleMaterial = 
                `<div class='material-container' data-utime=${mData.utime}>
                    <div class='material ${mData.type}'>
                        <div class='material-image'>
                            <img src="${mData.cover_url}" referrerpolicy="no-referrer" loading='lazy' />
                        </div>
                        <div class='material-info'>
                            <div class='type' style='display:none'>${mData.type}</div>
                            <div class='type'>
                                <span>💼类型：</span>
                                <span class='info' title="${materialType}">${materialType ?? '🍼🍹'}</span>
                            </div>
                            <div class='author'>
                                <span>👩‍🎓作者：</span>
                                <span class='info' title="${mData.author}">${mData.author || '🏃🏃‍♀️'}</span>
                            </div>
                            <div class='year'>
                                <span>📅日期：</span>
                                <span class='info' title="${mData.year}">${mData.year ?? '🍦🍮'}</span>
                            </div>
                            <div class='pages'>
                                <span>📃页数：</span>
                                <span class='info' title="${mData.pages}">${mData.pages ?? '🍼🍹'}</span>
                            </div>
                        </div>
                    </div>
                    <div class='material-name'>《${mData.name}》</div>
                    <div class='material-modal'>
                        <div class='urls'>
                            <span>🔑下载:</span>
                            <a href="${mData.file_url}" target='_blank' rel="noopener noreferrer">yukaidi</a>
                        </div>
                    </div>
                </div>`
                eleMaterials.insertAdjacentHTML('beforeend', eleMaterial);
                setNewBanner(document.querySelector("#materials .material-container:last-child"));
                loadedAmount ++;
            }
        }
    }


    function searchMaterialListener() {
        let eleSelect = document.querySelector(".searcher > select");
        let eleSearchButton = document.querySelector(".searcher > button");

        document.addEventListener("keyup", (e) => {
            let type = eleSelect.value;
            if (e.key === "Enter" && document.activeElement === document.querySelector(".searcher > input")) {
              initSearch();
              searchMaterial(type);
              loadMaterial(30);
            }
        })
    
        eleSearchButton.addEventListener("pointerdown", () => {
            let type = eleSelect.value;
            initSearch();
            searchMaterial(type);
            loadMaterial(30);
        });

        eleSelect.addEventListener("change", () => {
            let type = eleSelect.value;
            initSearch();
            searchMaterial(type);
            console.log(filteredMaterialData);
            loadMaterial(30);
        })
    }

    function continueLoadListener() {
        window.addEventListener("wheel", () => {
            let eleLastMaterial = document.querySelector(".material-container:last-child");
            let eleLastMaterialTop = eleLastMaterial.getBoundingClientRect().top;
            let windowHeight = window.innerHeight;
            if (eleLastMaterialTop - windowHeight < 100) {
            loadMaterial(perLoadAmount);
            }
        })
    }
}

toggleAbout();
toggleChangelog();
closeModalListener();
customScrollbar();
blinkButton();
dynamicLoadMaterial();

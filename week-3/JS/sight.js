/***************************************************************  
    runder   函數=>從sightData陣列中新增每8張景點圖片到網頁上
    picIndex 參數=>sightData陣列中的每張圖片索引值(index:0~57)
***************************************************************/
function runder(picIndex){
    for(let i = picIndex; i < (picIndex+8); i++){
        /*索引值超過景點筆數就跳出*/
        if(i >= sightData.length){
            break;
        }

        /*文字資料*/
        sightName = sightData[i].stitle; 
        /*新增p標籤*/
        let p = document.createElement('p');
        let newText = document.createTextNode(sightName);
        p.appendChild(newText);
        /*p設置class屬性*/
        p.classList.add('cap');
        

        /*圖片資料*/
        sightPic = sightData[i].file;
        let picLink = sightPic.split('https://');
        let firstPicLink = 'https://'+ picLink[1];
        /*新增img標籤*/
        let img = document.createElement('img');
        /*img設置src屬性*/
        let src = document.createAttribute('src');
        src.value = firstPicLink;
        img.setAttributeNode(src);
        /*img設置alt屬性*/
        let alt = document.createAttribute('alt');
        alt.value = 'picture';
        img.setAttributeNode(alt);
        /*img設置width、height屬性*/
        let width = document.createAttribute('width');
        width.value = '275px';
        img.setAttributeNode(width);
        let height = document.createAttribute('height');
        height.value = '200px';
        img.setAttributeNode(height);

        /*新增div標籤*/
        let div = document.createElement('div'); 
        /*div設置class屬性*/
        div.classList.add('cards');
        /*div新增img、p子節點*/
        div.appendChild(img);
        div.appendChild(p);
        
        /*取得section父節點位置*/
        let section = document.querySelector('.images');
        /*section新增div子節點*/
        section.appendChild(div); 
        
    }
}


async function getSight(){
    let object = await fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json");
    object = await object.json();
    sightData = object.result.results;

    let sightName; /*文字*/
    let sightPic; /*圖片*/

    /*************************************** 
        綁監聽按鈕:每點擊一次，就會新增8張圖片
    ****************************************/
    let picStartIdx = 8;
    let btn = document.querySelector('#btn');
    btn.addEventListener('click', e => {
        runder(picStartIdx);
        picStartIdx += 8;
    })

    /*網頁初始的8張景點圖片*/
    runder(0);
    
}
getSight();


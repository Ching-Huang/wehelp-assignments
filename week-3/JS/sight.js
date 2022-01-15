async function getSight(){
    let object = await fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json");
    object = await object.json();
    sightData = object.result.results;
    // console.log(sightData);
    let sightName; /*文字*/
    let sightPic; /*圖片*/
    for(let i = 0; i < 8; i++){
        /*文字*/
        sightName = sightData[i].stitle; 
        // console.log(sightName);
        /*新增p標籤*/
        let p = document.createElement('p');
        let newText = document.createTextNode(sightName);
        // console.log(newText);
        p.appendChild(newText);/*文字要去除兩邊雙引號!*/
        /*p設置class屬性*/
        p.classList.add('cap');
        // console.log(p); 

        /*圖片*/
        sightPic = sightData[i].file;
        // console.log(sightPic);
        let picLink = sightPic.split('https://');
        // console.log(picLink);
        let firstPicLink = 'https://'+ picLink[1];
        // console.log(firstPicLink);

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
        
        // console.log(img);

        /*新增div標籤*/
        let div = document.createElement('div'); 
        /*div設置class屬性*/
        div.classList.add("cards");

        /*div新增img、p子節點*/
        div.appendChild(img);
        div.appendChild(p);
        // console.log(div);

        /*取得section父節點位置*/
        let section = document.querySelector('.images');

        /*section新增div子節點*/
        section.appendChild(div); 
        // console.log(section);

         
    }
       
}
getSight();


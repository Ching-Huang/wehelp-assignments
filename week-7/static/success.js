console.clear();

async function searchUsername(){

    // 從 DOM 中取得 username 的"欄位值"
    let inputSearchUsername = document.querySelector('input').value;
    
    // 串接 API 並將 查詢 username 的欄位作為"樣板字串"代入 API網址中
    let apiUrl = await fetch(`http://127.0.0.1:3000/api/members?username=${inputSearchUsername}`);
    apiUrl = await apiUrl.json();
    
    // 從 DOM 中取得查詢 username 結果的欄位
    let showUsername = document.querySelector('.searchResult');

    // 查詢結果的欄位預留"空字串"
    let showTextResult   = '';

    // 取得 API 並搜尋 data 物件
    let searchUsernameResult = apiUrl.data

    // 查有此人
    if(searchUsernameResult !== null){
        let name     = apiUrl.data.name;
        let username = apiUrl.data.username;
        showTextResult   =  `${name}`+ " " +`(${username})`;
    
    }else{
        showTextResult   = "查無此人";
    }

    // 顯示查詢結果
    showUsername.textContent = showTextResult;
}

// 從 DOM 中取得 查詢按鈕 的欄位
let searchBtn = document.querySelector('button#search');

// 搜尋按鈕 綁監聽，點擊按鈕後執行 查詢會員姓名 
searchBtn.addEventListener('click', e => {
    searchUsername(); 
})
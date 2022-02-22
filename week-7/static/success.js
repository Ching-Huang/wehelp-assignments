console.clear();

/*----------------------- 前端透過 Fetch 連接 API 查詢會員資料 ----------------------- */
async function searchUsername(){

    // [DOM] 取得 username 的"欄位值"
    let inputSearchUsername = document.querySelector('input').value;
    
    // 串接 API 並將 查詢 username 的欄位作為"樣板字串"代入 API網址中
    let apiUrl = await fetch(`http://127.0.0.1:3000/api/members?username=${inputSearchUsername}`);
    apiUrl = await apiUrl.json();
    
    // [DOM] 取得查詢 username 結果的欄位
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
    }
    else{
        showTextResult   = "查無此人";
    }

    // 顯示查詢結果
    showUsername.textContent = showTextResult;

    // 清空 input 輸入框
    let inputClean = document.querySelector('.search input.search');
    inputClean.value = "";
}

// [DOM] 取得 查詢按鈕 的欄位
let searchBtn = document.querySelector('button#search');

// 搜尋按鈕 綁監聽，點擊按鈕後執行 查詢會員姓名 
searchBtn.addEventListener('click', searchUsername)


/*------------------------------- 完成修改 姓名 的功能 ------------------------------- */
async function modifyName(){
    
    // [DOM] 取得 name 的"欄位值"
    let inputModifyName = document.querySelector('.modify input.modify').value;
    
    // 串接 API ，處理 Request Body 請求資料 => 設定 method、headers 的參數值
    const apiUrl = 'http://127.0.0.1:3000/api/member';
    fetch(apiUrl, {
        method: 'POST',
        body: JSON.stringify({
            'name': inputModifyName
        }),
        headers:{
            'Content-Type': 'application/json;'
        }
    })
    .then(res => {
        return res.json();  // 轉換為JSON
    }).then(result =>{
        // console.log('inputModifyName:', inputModifyName);

        // [DOM] 取得修改 姓名 狀態結果的欄位
        let showModifyStatus = document.querySelector('.modifyStatus');
        // console.log('==showModifyStatus==', showModifyStatus);

        // 成功修改資料
        if ('ok' in result){
            // [DOM] 取得  <h2 id="loginName"> ，歡迎登入系統</h2> 
            let showLoginNewName = document.querySelector('#member #loginName');  
            // console.log('==showLoginNewName==', showLoginNewName);

        // 將修改後姓名，顯示在歡迎訊息中
        showLoginNewName.textContent = inputModifyName + '，歡迎登入系統';

        showModifyStatus.textContent = '更新成功';

        // 清空 input 輸入框
        let inputClean = document.querySelector('.modify input.modify');
        inputClean.value = "";
        
        }
        else{
            showModifyStatus.textContent = '更新失敗'; 
        }
    });
}

function btnBindProcess(){

    // [DOM] 取得 查詢按鈕 的欄位
    let searchBtn = document.querySelector('button#search');

    // 搜尋按鈕 綁監聽，點擊按鈕後執行 查詢會員姓名 
    searchBtn.addEventListener('click', searchUsername)

    // [DOM] 取得 修改按鈕 的欄位
    let modifyBtn = document.querySelector('button#modify');

    // 修改按鈕 綁監聽，點擊按鈕後執行 修改會員姓名 
    modifyBtn.addEventListener('click', modifyName);
}

//等待網頁完全讀取完畢, 再綁監聽
window.addEventListener('load', btnBindProcess);





    
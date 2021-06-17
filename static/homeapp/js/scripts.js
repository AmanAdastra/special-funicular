console.log("i ma here")


function getuserinfo(obj){
    console.log(obj)
    let uname= document.getElementById('username')
    let info = document.getElementById('myinfo')
    let source = obj.firstElementChild.firstElementChild.getAttribute('src')
    let img = document.createElement('img')
    img.src = source
    
    axios.get('/logsys/user/'+obj.id)
  .then(response=>{
      uname.innerHTML=response.data.username
      info.innerHTML = ""
      info.appendChild(img)
     console.log(response)
  })
  
}


console.log("i ma here");

function getuserinfo(obj) {
  let uname = document.getElementById("username");
  let info = document.getElementById("myinfo");
  let login = document.getElementById("last-login");
  let source = obj.firstElementChild.firstElementChild.getAttribute("src");
  let anchor = document.getElementById('anchor')
  let a = document.createElement('a')
  a.href = "/logsys/uprofile/"+obj.id
  a.text="Check out my profile"
  let img = document.createElement("img");
  img.src = source.replace("35", "200");
  img.setAttribute("class", "img-fluid");

  axios.get("/logsys/user/" + obj.id).then((response) => {
    anchor.innerHTML =""
    anchor.appendChild(a)
    uname.innerHTML =
      response.data.username.charAt(0).toUpperCase() +
      response.data.username.slice(1).toLowerCase();
    login.innerHTML = "Last Seen: " + response.data.last_login.split("T")[0];
    info.innerHTML = "";
    info.appendChild(img);
  });
}


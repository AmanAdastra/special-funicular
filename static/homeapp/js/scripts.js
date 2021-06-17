console.log("i ma here");

function getuserinfo(obj) {
  let uname = document.getElementById("username");
  let info = document.getElementById("myinfo");
  let login = document.getElementById("last-login");
  let source = obj.firstElementChild.firstElementChild.getAttribute("src");
  let img = document.createElement("img");
  img.src = source.replace("35", "200");
  img.setAttribute("class", "img-fluid");

  axios.get("/logsys/user/" + obj.id).then((response) => {
    uname.innerHTML =
      response.data.username.charAt(0).toUpperCase() +
      response.data.username.slice(1).toLowerCase();
    login.innerHTML = response.data.last_login.split("T")[0];
    info.innerHTML = "";
    info.appendChild(img);
  });
}

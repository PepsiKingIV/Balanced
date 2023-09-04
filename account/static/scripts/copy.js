var result = 'token'

var executeCopy = function() {
    var copyhelper = document.createElement("input");
    copyhelper.className = 'copyhelper'
    document.body.appendChild(copyhelper);
    copyhelper.value = result;
    copyhelper.select();
    document.execCommand("copy");
    document.body.removeChild(copyhelper);
  };
  
  document.getElementById('mybutton').addEventListener('click', function() {
    executeCopy();
  
    alert("Токен скопирован в буфер обмена");
  });
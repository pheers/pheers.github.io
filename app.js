let tg = window.Telegram.WebApp;
var params = window
    .location
    .search
    .replace('?','')
    .split('&')
    .reduce(
        function(p,e){
            var a = e.split('=');
            p[ decodeURIComponent(a[0])] = decodeURIComponent(a[1]);
            return p;
        },
        {}
    );

h = document.getElementById("h1")
h.innerHTML = `Запись на кастинг | ${params["team"]}`

aname = document.getElementById("name")
last_name = document.getElementById("last_name")
third_name = document.getElementById("third_name")
phone = document.getElementById("phone")

onblur = function(){
    if (aname.value && last_name.value && third_name.value && phone.value){
        if(!tg.MainButton.isVisible){
            tg.MainButton.text = "Записаться"
            tg.MainButton.show()
        }
        
    }else{
        if(tg.MainButton.isVisible){
            tg.MainButton.hide()
        }
    }
}

aname.oninput = onblur
last_name.oninput = onblur
third_name.oninput = onblur
phone.oninput = onblur

tg.MainButton.onClick(function(){
    tg.sendData(`name:${aname.value},last_name:${last_name.value},third_name:${third_name.value},phone:${phone.value}`)
    tg.close()
})

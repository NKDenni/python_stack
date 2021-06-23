function display_c() {
    var refresh = 1000; // Refresh rate in milli seconds
    mytime = setTimeout('display_ct()', refresh)
}

function display_ct() {
    var x = new Date()
    var hours = x.getHours().toString()
    hours = hours.length == 1 ? 0 + hours : hours;

    var minutes = x.getMinutes().toString()
    minutes = minutes.length == 1 ? 0 + minutes : minutes;

    var seconds = x.getSeconds().toString()
    seconds = seconds.length == 1 ? 0 + seconds : seconds;

    var month = (x.getMonth() + 1).toString();
    month = month.length == 1 ? 0 + month : month;

    var dt = x.getDate().toString();
    dt = dt.length == 1 ? 0 + dt : dt;

    var x1 = x.getFullYear() + "年" + " " + month + "月" + " " + dt + "日";
    x1 = x1 + " - " + hours + ":" + minutes + ":" + seconds;
    document.getElementById('ct').innerHTML = x1;
    display_c();
}
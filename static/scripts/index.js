var interval_timer = "";

function delTable(name){
    $(`#${name}`).empty();
}

function create_wifi_row(wifidata){
    var wifitable = document.getElementById('showwifi');
    var row = wifitable.insertRow(-1);
    var namecell = row.insertCell(0);
    var frequency = row.insertCell(1);
    var channel = row.insertCell(2);
    var quality = row.insertCell(3);
    var signal = row.insertCell(4);
    namecell.innerHTML = wifidata[0].replaceAll('"',"",);
    frequency.innerHTML = wifidata[1];
    channel.innerHTML = wifidata[2];
    quality.innerHTML = wifidata[3];
    signal.innerHTML = wifidata[4];
}

function create_bluetooth_row(bluetoothdata){
    var bluetoothtable = document.getElementById('showbluetooth');
    var row = bluetoothtable.insertRow(-1);
    var name = row.insertCell(0);
    var address = row.insertCell(1);
    name.innerHTML = bluetoothdata[1];
    address.innerHTML = bluetoothdata[0];
}

function addWIFI(wifidata){
    for (let i = 0; i < wifidata.length; i++){
        create_wifi_row(wifidata[i])
    }
}

function addBluetooth(bluetoothdata){
    for (let i = 0; i < bluetoothdata.length; i++){
        create_bluetooth_row(bluetoothdata[i])
    }

}

function refreshData(){
    $.ajax({
                url: "/getdata",
                type: 'GET'
            }).done(function(data){
                console.log(data);
                delTable('showwifi');
                delTable('showbluetooth');
                addWIFI(data.data.ed);
                addBluetooth(data.data.bd);
            });
}

if (interval_timer == ""){
    interval_timer = setInterval(function() {
        refreshData();
    }, 500)
}
refreshData();
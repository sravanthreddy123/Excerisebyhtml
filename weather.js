async function weather(){
    let cityname=document.getElementById("test");
    let url='https://api.openweathermap.org/data/2.5/weather?q='+cityname.value+'&appid=df4d68895fde02b80e7fe7ce4ab4a765&units=metric'
    const res=await fetch(url);
    let data=await res.json();
    console.log(data);
    let{ main:{temp,temp_min,temp_max}}=data;
    console.log("TEMP:"+temp);
    console.log("MIN_TEMP: "+temp_min);
    console.log("MAX_TEMP: "+temp_max);
}

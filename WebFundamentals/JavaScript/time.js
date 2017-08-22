var HOUR
var MINUTE
var PERIOD //AM, or PM

function time(HOUR, MINUTE, PERIOD){
  if (PERIOD === "AM"){
    PERIOD = "in the morning";
  }
  else if (PERIOD === "PM"){
    PERIOD = "in the evening";
  }
    if (MINUTE == 5){
      console.log("It's", MINUTE, "past", HOUR, PERIOD);
    }else if(MINUTE < 15){
      console.log("It's just after", HOUR, PERIOD);
    }else if(MINUTE == 15){
      console.log("It's a quarter after", HOUR, PERIOD);
    }else if(MINUTE == 30){
      console.log("It's", HOUR, MINUTE, PERIOD);
    }else if(MINUTE == 45){
      console.log("It's a quarter until", HOUR + 1, PERIOD);
    }else{
      console.log("It's almost", HOUR + 1, PERIOD);
    }
}

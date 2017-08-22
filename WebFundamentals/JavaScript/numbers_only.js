var arr = [1, "apple", -3, "orange", .5];

var newArray = [];

function numbersOnly(arr){
  for (var i = 0; i < arr.length; i++){
    if (typeof arr[i] === "number"){
      newArray.push(arr[i]);
    }
  }
  console.log(newArray);
  return(newArray);
}

numbersOnly(arr);



//second function that removes
var arr = [1, "apple", -3, "orange", .5];

function numbersOnly(arr){
  for (var i = 0; i <arr.length; i++){
    if (typeof arr[i] != "number"){
      arr.splice(i, 1);
    }
  }
  console.log(arr);
}

numbersOnly(arr);

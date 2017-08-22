function fancyArray(arr){
  for (var i = 0; i < arr.length; i ++){
    console.log(i, '->', arr[i]);
  }
}

arr = ["James", "Jill", "Jane", "Jack"];

fancyArray(arr);

//user pass in symbol

function fancyArray(arr, symbol){
  for (var i = 0; i < arr.length; i ++){
    console.log(i, symbol, arr[i]);
  }
}

arr = ["James", "Jill", "Jane", "Jack"];
symbol = '::';

fancyArray(arr, symbol);

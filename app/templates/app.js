function getBathValue() {
  var uiBA = document.getElementsByName("uiBA");
  for(var i in uiBA) {
    if(uiBA[i].checked) {
      return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}
  
function getBRValue() {
  var uiBR = document.getElementsByName("uiBR");
  for(var i in uiBR) {
    if(uiBR[i].checked) {
      return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}
  
function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var sqft = document.getElementById("uiSqft");
  var bedrooms = getBRValue();
  var bathrooms = getBathValue();
  var location = document.getElementById("uiLocations");
  var lot_size = document.getElementById("uiAcres");
  var yr_built = document.getElementById("uiYR")
  var estPrice = document.getElementById("uiEstimatedPrice");
  
  var url = "http://127.0.0.1:5000/predict_home_price";
  
  $.post(url, {
    total_sqft: parseFloat(sqft.value),
    bedrooms: bedrooms,
    bathrooms: bathrooms,
    lot_size: parseFloat(lot_size.value),
    yr_built: parseInt(yr_built.value),
    location: location.value
  },function(data, status) {
    console.log(data.estimated_price);
    estPrice.innerHTML = `<h2>${data.estimated_price.toString()}</h2>`;
    console.log(status);
  });
}
  
function onPageLoad() {
  console.log( "document loaded" );
  var url = "http://127.0.0.1:5000/get_location_names"; 
  $.get(url,function(data, status) {
      console.log("got response for get_location_names request");
      if(data) {
        var locations = data.locations;
        var uiLocations = document.getElementById("uiLocations");
        $('#uiLocations').empty();
        for(var i in locations) {
            var opt = new Option(locations[i]);
            $('#uiLocations').append(opt);
        }
      }
  });
}
  
window.onload = onPageLoad;
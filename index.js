let map;
let service;
let infowindow;
let ltlg;
let c7;
let c8;
let completedRequests = 0;
let outputs = [];

function initMap() {
  ltlg = [
    { location: new google.maps.LatLng(40.475383, -74.477986), radius: 1000 },
    { location: new google.maps.LatLng(40.480835, -74.464977), radius: 1000 },
    { location: new google.maps.LatLng(40.492239, -74.451577), radius: 1000 },
    { location: new google.maps.LatLng(40.481883, -74.437079), radius: 1000 },
    { location: new google.maps.LatLng(40.484138, -74.420455), radius: 1000 },
    { location: new google.maps.LatLng(40.486770, -74.404346), radius: 1000 },
    { location: new google.maps.LatLng(40.479593, -74.451037), radius: 540 },
    { location: new google.maps.LatLng(40.503122, -74.460545), radius: 860 },
    //{ location: new google.maps.LatLngBounds(LatLng( 40.488259, -74.439453), LatLng( 40.507150, -74.447091))}
    
];

  for (i = 0; i < ltlg.length; i++) {
    var c = ltlg[i];
    map = new google.maps.Map(document.getElementById("map"), {
      center: c.location,
      zoom: 15,
    });

    var request = {
      location: c.location,
      radius: c.radius,
      //type: ['restaurant']
    };

    service = new google.maps.places.PlacesService(map);
    service.nearbySearch(request, callback);
  }
}

let count = 0;

function callback(results, status, pagetoken) {
  if (status == google.maps.places.PlacesServiceStatus.OK) {
    console.log("pagetoken:", pagetoken);

    for (var i = 0; i < results.length; i++) {
      let res = results[i];
      outputs.push(res);
      count++;
      console.log(count, res);
    }

    if (pagetoken && pagetoken.hasNextPage) {
      pagetoken.nextPage();
      console.log("nextpage");
    } else {
      completedRequests++;
      checkCompletion();
    }
  }
}

function checkCompletion() {
  console.log(`Completed request for circle ${completedRequests}`)
  if (completedRequests === ltlg.length) {
      console.log("All pages for each object have been printed!");
      // You can add any other notification logic here
      exportToJSON(); // Trigger the export
  }
}

function exportToJSON() {
  const jsonString = JSON.stringify(outputs, null, 2); // Convert array to JSON string
  const blob = new Blob([jsonString], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'outputs.json';
  a.click();
  URL.revokeObjectURL(url);
}

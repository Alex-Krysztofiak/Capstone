fetch('Match_Details.py')
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    appendData(data);
  })
  .catch(function (err) {
    // If an error occured, you will catch it here
  });
  function appendData(data) {
    var mainContainer = document.getElementById("myData");
    for (var i = 0; i < data.length; i++) {
        var div = document.createElement("div");
        div.innerHTML = 'Name: ' + data[i].match_id + ' ' + data[i].profile_name;
        mainContainer.appendChild(div);
    }
}


window.onload = init;

function init() {
 var map;

    DG.then(function () {
        map = DG.map('map', {
            center: [43.2261001, 76.90377749999999],
            zoom: 15
        });
        DG.marker([43.2261001, 76.90377749999999]).addTo(map);
    });
}